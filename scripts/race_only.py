"""Why the comparison does not fall back on recorded race alone: a check, not part of the comparison.

Where a department does not record ethnicity (Oklahoma City, Detroit, Tulsa, Cleveland, Toledo), Hispanic victims stay
in their recorded race while the White denominator (ACS B01001H) is non-Hispanic White women. A race-only measure, every
woman victim recorded as White over White-alone women of any ethnicity (B01001A), looks like the like-for-like fix. It is
not: officers record most Hispanic victims as White, while most Hispanic residents do not report White alone to the
Census (many report some other race, or two or more). For every city this records the race-only White ratio beside the
main one, and the two shares that explain the gap: the share of Hispanic residents who are White alone (ACS B03002, from
the kit's cache) and the share of Hispanic women victims recorded as White (where the department records ethnicity).
B01001A is fetched for 20 places per request into out/cache/acs_white_any.json; on a 429 the script waits as told.

  python scripts/race_only.py      ->  out/race_only.json   (after run_cities.py and screen.py)
"""
import json
import pathlib
import time
import urllib.request

import pandas as pd

from cities import CITIES
from run_cities import retry_after

ROOT = pathlib.Path(__file__).resolve().parent.parent
CR = "https://api.censusreporter.org/1.0"


def white_any(geoids, tries=12):
    """Women who are White alone, any ethnicity (B01001A017), for every place, in batches of 20 places per request."""
    path = ROOT / "out/cache/acs_white_any.json"
    have = json.loads(path.read_text()) if path.exists() else {}
    todo = [g for g in geoids if g not in have]
    for i in range(0, len(todo), 20):
        url = f"{CR}/data/show/acs2024_5yr?table_ids=B01001A&geo_ids={','.join(todo[i:i + 20])}"
        for attempt in range(tries):
            try:
                data = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "disparity-kit"}), timeout=300))["data"]
                break
            except urllib.error.HTTPError as e:
                if e.code != 429 or attempt == tries - 1:
                    raise
                wait = retry_after()
                print(f"  Census Reporter rate limit, waiting {wait}s", flush=True)
                time.sleep(wait + 5)
        have.update({g: float(v["B01001A"]["estimate"]["B01001A017"]) for g, v in data.items()})
        path.write_text(json.dumps(have, indent=1) + "\n")
    return have


def main():
    out = []
    done = [c for c in CITIES if (ROOT / "cities" / c["slug"] / "out/results.json").exists()]
    white = white_any([c["geoid"] for c in CITIES])  # all places at once: three requests
    for c in done:
        d = ROOT / "cities" / c["slug"]
        cfg = json.loads((d / "analysis.json").read_text())
        R = json.loads((d / "out/results.json").read_text())
        pop = json.loads((d / "out/population.json").read_text())["city"]
        hisp = json.loads((d / "out/cache/acs_place_hispanic.json").read_text())["data"][c["geoid"]]["B03002"]["estimate"]
        v = pd.concat([pd.read_csv(d / s["path"], dtype=str, usecols=["incident_date", "sex", "race", "ethnicity"]) for s in cfg["incidents"]])
        v = v[(v["incident_date"] >= cfg["window"]["start"]) & (v["incident_date"] <= cfg["window"]["end"] + " 23:59:59") & (v["sex"] == "F")]
        nb, nw = int((v["race"] == "B").sum()), int((v["race"] == "W").sum())
        hv = v[v["ethnicity"] == "H"]
        black_f, white_f = pop["Black"]["F"], white[c["geoid"]]
        rb, rw = nb / black_f / R["years"] * 1e5, nw / white_f / R["years"] * 1e5
        out.append({"slug": c["slug"], "city": c["name"], "tier": c["tier"],
                    "ratio_white_main": R["ratios"].get("White"), "ratio_white_race_only": round(rb / rw, 2),
                    "hispanic_residents_white_alone_pct": round(hisp["B03002013"] / hisp["B03002012"] * 100, 1),
                    "hispanic_women_victims_recorded_white_pct": round(float((hv["race"] == "W").mean() * 100), 1) if len(hv) >= 50 else None,
                    "black_women_victims": nb, "white_women_victims_any_ethnicity": nw, "black_women": black_f, "white_women_any_ethnicity": white_f})
    (ROOT / "out/race_only.json").write_text(json.dumps(out, indent=1) + "\n")
    recorded = {x["slug"] for x in json.loads((ROOT / "out/screen.json").read_text()) if x["ethnicity_recording"] == "recorded"}
    rec = [r for r in out if r["slug"] in recorded and r["hispanic_women_victims_recorded_white_pct"] is not None]
    print(f"{len(out)} cities. Hispanic residents who are White alone: {min(r['hispanic_residents_white_alone_pct'] for r in out)}% to "
          f"{max(r['hispanic_residents_white_alone_pct'] for r in out)}%; Hispanic women victims recorded White: "
          f"{min(r['hispanic_women_victims_recorded_white_pct'] for r in rec)}% to {max(r['hispanic_women_victims_recorded_white_pct'] for r in rec)}% "
          f"({len(rec)} cities that record ethnicity, median {sorted(r['hispanic_women_victims_recorded_white_pct'] for r in rec)[len(rec) // 2]}%).")


if __name__ == "__main__":
    main()
