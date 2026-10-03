"""Monthly NIBRS incident counts for every city-sized police agency in a state, 2022 to 2025, without downloading
the whole state files.

The FBI's Crime Data Explorer serves each state-year zip through a signed S3 link that honors HTTP Range requests.
zipfile reads the archive's directory from the end of the file, so only two members are fetched: agencies.csv and
NIBRS_incident.csv (a tenth to a quarter of the zip). For each agency the script counts incidents by month.

  python scripts/fbi_months.py TX CA NY ...   ->  out/cache/fbi_<ST>.json  {ori: {name, type, population, county,
                                                  nibrs_start, months: {"2022-01": n, ...}}} for agencies of 50,000+
"""
import concurrent.futures as cf
import io
import json
import pathlib
import sys
import urllib.parse
import urllib.request
import zipfile

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
CDE = "https://cde.ucr.cjis.gov/LATEST/s3/signedurl"
UA = {"User-Agent": "disparity-kit"}
YEARS = [2022, 2023, 2024, 2025]
MIN_POP = 50000


class RangeFile(io.RawIOBase):
    """A read-only, seekable view of a remote file, fetched in blocks with HTTP Range requests."""

    def __init__(self, url, block=8 << 20):
        self.url, self.block, self.pos, self.cache = url, block, 0, {}
        r = urllib.request.urlopen(urllib.request.Request(url, headers={**UA, "Range": "bytes=0-0"}), timeout=120)
        self.size = int(r.headers["Content-Range"].split("/")[1])
        self.fetched = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else self.pos + off if whence == 1 else self.size + off
        return self.pos

    def _get(self, i):
        if i not in self.cache:
            a = i * self.block
            b = min(self.size, a + self.block) - 1
            req = urllib.request.Request(self.url, headers={**UA, "Range": f"bytes={a}-{b}"})
            self.cache[i] = urllib.request.urlopen(req, timeout=300).read()
            self.fetched += len(self.cache[i])
            while len(self.cache) > 6:
                self.cache.pop(next(iter(self.cache)))
        return self.cache[i]

    def readinto(self, buf):
        n = min(len(buf), self.size - self.pos)
        done = 0
        while done < n:
            i, off = divmod(self.pos, self.block)
            chunk = self._get(i)[off:off + n - done]
            if not chunk:
                break
            buf[done:done + len(chunk)] = chunk
            done += len(chunk)
            self.pos += len(chunk)
        return done


def signed(st, year):
    key = f"nibrs/incident/{year}/{st}-{year}.zip"
    req = urllib.request.Request(f"{CDE}?{urllib.parse.urlencode({'key': key})}", headers=UA)
    return json.load(urllib.request.urlopen(req, timeout=60)).get(key)


def one_year(st, year):
    url = signed(st, year)
    if not url:
        return None, {"state": st, "year": year, "error": "no file"}
    rf = RangeFile(url)
    z = zipfile.ZipFile(io.BufferedReader(rf, buffer_size=1 << 20))
    names = {pathlib.PurePosixPath(n).name.lower(): n for n in z.namelist()}
    ag = pd.read_csv(z.open(names["agencies.csv"]), low_memory=False, encoding_errors="replace")  # a few state files carry non-UTF-8 names
    ag.columns = [c.lower() for c in ag.columns]
    inc = pd.read_csv(z.open(names["nibrs_incident.csv"]), usecols=lambda c: c.lower() in ("agency_id", "incident_date"), low_memory=False, encoding_errors="replace")
    inc.columns = [c.lower() for c in inc.columns]
    inc["month"] = inc["incident_date"].astype(str).str[:7]
    counts = inc.groupby(["agency_id", "month"]).size()
    return (ag, counts), {"state": st, "year": year, "zip_mb": round(rf.size / 1e6, 1), "fetched_mb": round(rf.fetched / 1e6, 1)}


def state(st):
    agencies, months, log = {}, {}, []
    for y in YEARS:
        try:
            res, info = one_year(st, y)
        except Exception as e:  # keep going; the gap shows up as missing months
            res, info = None, {"state": st, "year": y, "error": repr(e)[:200]}
        log.append(info)
        if res is None:
            continue
        ag, counts = res
        for _, a in ag.iterrows():
            if (a.get("population") or 0) < MIN_POP and a.get("agency_type_name") != "City":
                continue
            o = a["ori"]
            agencies[o] = {"name": a.get("pub_agency_name"), "unit": a.get("pub_agency_unit"), "type": a.get("agency_type_name"),
                           "population": None if pd.isna(a.get("population")) else int(a["population"]), "county": a.get("county_name"),
                           "nibrs_start": str(a.get("nibrs_start_date"))[:10]}
            for (aid, m), n in counts[counts.index.get_level_values(0) == a["agency_id"]].items():
                if m[:4].isdigit() and 2022 <= int(m[:4]) <= 2025:
                    months.setdefault(o, {})[m] = months.get(o, {}).get(m, 0) + int(n)
    out = {o: {**agencies[o], "months": dict(sorted(months.get(o, {}).items()))} for o in agencies if (agencies[o]["population"] or 0) >= MIN_POP}
    (ROOT / f"out/cache/fbi_{st}.json").write_text(json.dumps({"agencies": out, "log": log}, indent=1, default=str))
    return st, log


def main():
    sts = [s for s in sys.argv[1:] if not (ROOT / f"out/cache/fbi_{s}.json").exists()]
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for st, log in ex.map(state, sts):
            print(st, "; ".join(f"{l['year']}: " + (l.get("error") or f"{l['fetched_mb']} of {l['zip_mb']} MB") for l in log), flush=True)


if __name__ == "__main__":
    main()
