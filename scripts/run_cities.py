"""Run every city through the kit in three phases.

Needs data/interim/flat/<ST>-<year>.csv (flatten_states.py) and cities/<slug>/analysis.json (make_configs.py).
  0. each city's rows cut from its state's flat files into data/interim/cities/<slug>.csv
  1. in parallel, six at a time: the audit and the NIBRS victim files
  2. one city at a time: the city's Census place from out/eligibility.csv written to out/place.json (the place block is
     already in its config), then ACS denominators. Census Reporter rate-limits (HTTP 429 with Retry-After, about ten
     minutes, after roughly a hundred requests); on a 429 the run waits as told and goes on. The kit caches each
     download in cities/<slug>/out/cache/, so nothing is fetched twice.
  3. in parallel, six at a time: the tests
Steps 0 and 1 are skipped where their outputs are newer than their inputs, unless --fresh. Each city's log goes to
cities/<slug>/out/run.log.

  python scripts/run_cities.py                       # all cities
  python scripts/run_cities.py chicago new_york      # some
  python scripts/run_cities.py --fresh               # redo the cuts and victim files too
"""
import argparse
import concurrent.futures as cf
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.error
import urllib.request

import pandas as pd

from cities import CITIES

ROOT = pathlib.Path(__file__).resolve().parent.parent
KIT = pathlib.Path(os.path.expanduser(os.environ.get("DISPARITY_KIT", "~/.claude/disparity-kit/kit")))
PY = sys.executable
BY_SLUG = {c["slug"]: c for c in CITIES}
PROBE = "https://api.censusreporter.org/1.0/data/show/acs2024_5yr?table_ids=B01003&geo_ids=01000US"


def newer(out, inp):
    out = [pathlib.Path(o) for o in (out if isinstance(out, list) else [out])]
    inp = [pathlib.Path(i) for i in (inp if isinstance(inp, list) else [inp])]
    return all(o.exists() for o in out) and min(o.stat().st_mtime for o in out) > max(i.stat().st_mtime for i in inp)


def cut(slugs, fresh):
    """Each city's rows of its state's flat files."""
    dest = ROOT / "data/interim/cities"
    dest.mkdir(parents=True, exist_ok=True)
    for st in sorted({BY_SLUG[s]["state"] for s in slugs}):
        files = sorted((ROOT / "data/interim/flat").glob(f"{st}-*.csv"))
        todo = [s for s in slugs if BY_SLUG[s]["state"] == st and (fresh or not newer(dest / f"{s}.csv", files))]
        if not todo:
            continue
        flat = pd.concat([pd.read_csv(f, low_memory=False, dtype=str) for f in files])
        for s in todo:
            part = flat[flat["ori"] == BY_SLUG[s]["ori"]]
            part.to_csv(dest / f"{s}.csv", index=False)
            print(f"{s}: {len(part):,} rows", flush=True)


def call(cmd, log):
    return subprocess.run([str(a) for a in cmd], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT).returncode


def victims(slug, fresh):
    d = ROOT / "cities" / slug
    rows = ROOT / f"data/interim/cities/{slug}.csv"
    outs = [d / "out/audit_nibrs.md", d / f"data/{slug}_aggravated.csv", d / f"data/{slug}_simple.csv"]
    if not fresh and newer(outs, rows):
        with open(d / "out/run.log", "a") as log:
            log.write(f"--- {time.strftime('%Y-%m-%d %H:%M')} rerun: audit and victim files up to date, from denominators on ---\n")
        return slug, "victim files up to date"
    cfg = json.loads((d / "analysis.json").read_text())
    (d / "out").mkdir(parents=True, exist_ok=True)
    with open(d / "out/run.log", "w") as log:
        for cmd in ([PY, KIT / "audit.py", rows, "--code", "offense_code", "--desc", "offense_name", "--id", "victim_id", "--date", "incident_date",
                     "--out", outs[0]],
                    [PY, KIT / "nibrs.py", "victims", rows, "--ori", cfg["_ori"], "--kind", "aggravated=13A", "--kind", "simple=13B",
                     "--race-rule", "hispanic-first", "--out-dir", d / "data", "--prefix", f"{slug}_"]):
            if call(cmd, log):
                return slug, f"FAILED at {pathlib.Path(str(cmd[1])).name}, see cities/{slug}/out/run.log"
    return slug, "victim files written"


def retry_after():
    """Seconds Census Reporter asks us to wait (0 if it answers now)."""
    try:
        urllib.request.urlopen(urllib.request.Request(PROBE, headers={"User-Agent": "disparity-kit"}), timeout=60)
        return 0
    except urllib.error.HTTPError as e:
        return int(e.headers.get("Retry-After") or 300) if e.code == 429 else 300
    except OSError:
        return 120


def denominators(slug, tries=12):
    c = BY_SLUG[slug]
    d = ROOT / "cities" / slug
    cfg = json.loads((d / "analysis.json").read_text())
    assert cfg["place"]["census_geoid"] == c["geoid"], f"{slug}: config place differs from eligibility"
    place = {"query": c["place"], "census_geoid": c["geoid"], "display_name": c["place"], "population": c["population"],
             "source": "out/eligibility.csv (Census Reporter, ACS 2020 to 2024), matched in the eligibility count"}
    (d / "out/place.json").write_text(json.dumps(place, indent=1) + "\n")
    for attempt in range(tries):
        with open(d / "out/run.log", "a") as log:
            start = log.tell()
            if call([PY, KIT / "denominators.py", d / "analysis.json"], log) == 0:
                return "denominators written"
        if b"HTTP Error 429" not in (d / "out/run.log").read_bytes()[start:]:
            return f"FAILED at denominators.py, see cities/{slug}/out/run.log"
        wait = retry_after()
        print(f"  {slug}: Census Reporter rate limit, waiting {wait}s (try {attempt + 1})", flush=True)
        time.sleep(wait + 5)
    return f"FAILED at denominators.py after {tries} tries (rate limit)"


def analyze(slug):
    d = ROOT / "cities" / slug
    with open(d / "out/run.log", "a") as log:
        if call([PY, KIT / "analyze.py", d / "analysis.json"], log):
            return slug, f"FAILED at analyze.py, see cities/{slug}/out/run.log"
    return slug, (d / "out/run.log").read_text().strip().splitlines()[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cities", nargs="*")
    ap.add_argument("--fresh", action="store_true")
    a = ap.parse_args()
    slugs = a.cities or [c["slug"] for c in CITIES]
    unknown = [s for s in slugs if s not in BY_SLUG]
    if unknown:
        sys.exit(f"unknown cities: {unknown}")
    cut(slugs, a.fresh)
    ok = []
    with cf.ProcessPoolExecutor(max_workers=6) as ex:
        for fut in cf.as_completed([ex.submit(victims, s, a.fresh) for s in slugs]):
            slug, msg = fut.result()
            if "FAILED" in msg:
                print(f"{slug}: {msg}", flush=True)
            else:
                ok.append(slug)
    print(f"phase 1: {len(ok)} of {len(slugs)} cities have victim files", flush=True)
    ready = []
    for i, s in enumerate([s for s in slugs if s in ok], 1):
        msg = denominators(s)
        print(f"{s}: {msg} ({i} of {len(ok)})", flush=True)
        if "FAILED" not in msg:
            ready.append(s)
    with cf.ProcessPoolExecutor(max_workers=6) as ex:
        for fut in cf.as_completed([ex.submit(analyze, s) for s in ready]):
            slug, last = fut.result()
            print(f"{slug}: {last}", flush=True)
    print(f"done: {len(ready)} of {len(slugs)} cities through the tests", flush=True)


if __name__ == "__main__":
    main()
