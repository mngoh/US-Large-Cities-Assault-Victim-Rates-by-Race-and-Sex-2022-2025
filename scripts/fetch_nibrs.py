"""Download the FBI's NIBRS incident files, one zip per state and year, as received.

The Crime Data Explorer (Documents & Downloads, "Download NIBRS data by state and year") serves each file through a
signed link from /LATEST/s3/signedurl?key=nibrs/incident/<year>/<ST>-<year>.zip. Each zip is saved to
data/raw/<ST>-<year>.zip with <ST>-<year>.zip.source.json beside it (key, time, size, sha256). A file that already has
its .source.json is skipped, so a run can be repeated after a failure. Texas is linked from the Dallas project.

  python scripts/fetch_nibrs.py                    # the 27 states, 2022 to 2025
  python scripts/fetch_nibrs.py CA NY --years 2024 2025
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import pathlib
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CDE = "https://cde.ucr.cjis.gov/LATEST/s3/signedurl"
UA = {"User-Agent": "disparity-kit"}
STATES = "AZ CA CO DC FL IL IN KY MA MD MI MN MO NC NE NJ NV NY OH OK OR PA TN TX VA WA WI".split()
YEARS = ["2022", "2023", "2024", "2025"]
DALLAS = ROOT.parent / "Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/raw"
RAW = ROOT / "data/raw"


def get(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout)


def link_texas(year):
    src = DALLAS / f"TX-{year}.zip"
    dest = RAW / f"TX-{year}.zip"
    if not dest.exists():
        dest.symlink_to(src)
    side = pathlib.Path(str(dest) + ".source.json")
    if not side.exists():
        side.write_text((DALLAS / f"TX-{year}.zip.source.json").read_text())
    return f"TX-{year}: linked to {src}"


def fetch(st, year, tries=3):
    if st == "TX":
        return link_texas(year)
    dest = RAW / f"{st}-{year}.zip"
    side = pathlib.Path(str(dest) + ".source.json")
    if side.exists():
        return f"{st}-{year}: have it"
    key = f"nibrs/incident/{year}/{st}-{year}.zip"
    for attempt in range(1, tries + 1):
        try:
            signed = json.load(get(f"{CDE}?{urllib.parse.urlencode({'key': key})}")).get(key)
            if not signed:
                return f"{st}-{year}: no file at {key}"
            part = pathlib.Path(str(dest) + ".part")
            h = hashlib.sha256()
            with get(signed, timeout=1800) as r, open(part, "wb") as fh:
                expect = int(r.headers.get("Content-Length") or 0)
                while chunk := r.read(1 << 20):
                    h.update(chunk)
                    fh.write(chunk)
            if expect and part.stat().st_size != expect:
                raise IOError(f"got {part.stat().st_size:,} of {expect:,} bytes")
            part.rename(dest)
            info = {"url": "https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads", "platform": "fbi-cde", "api": f"{CDE}?key={key}", "key": key,
                    "fetched_at": dt.datetime.now().isoformat(timespec="seconds"), "bytes": dest.stat().st_size, "sha256": h.hexdigest(),
                    "note": f"FBI Crime Data Explorer, NIBRS incident data by state and year, {st} {year}, as received"}
            side.write_text(json.dumps(info, indent=1))
            return f"{st}-{year}: wrote {dest.stat().st_size:,} bytes"
        except Exception as e:  # network errors: try again with a fresh signed link
            if attempt == tries:
                return f"{st}-{year}: FAILED after {tries} tries ({e})"
            time.sleep(10 * attempt)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("states", nargs="*", default=STATES)
    ap.add_argument("--years", nargs="+", default=YEARS)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    jobs = [(st, y) for st in a.states for y in a.years]
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        for fut in cf.as_completed([ex.submit(fetch, *j) for j in jobs]):
            print(fut.result(), flush=True)


if __name__ == "__main__":
    main()
