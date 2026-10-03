"""The cities in the national run, from out/eligibility.csv, as decided before any results.

Tier 1: every city with status yes and window 2022-2025, except Las Vegas, whose department (NV0020100) covers 1.71
million people, 2.59 times the city. Window 2022-01-01 to 2025-12-31.
Tier 2: every city with status yes and window 2024-2025. Window 2024-01-01 to 2025-12-31, shown apart.

  from cities import CITIES      # [{slug, city, state, name, ori, geoid, tier, start, end, ...}], in eligibility order
"""
import csv
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEFT_OUT = {"NV0020100": "Las Vegas: department population 1,712,136 is 2.59x the city's"}
NEAR_MISSES = ["Indianapolis", "Atlanta", "Riverside", "Greensboro"]
WINDOWS = {"2022-2025": (1, "2022-01-01", "2025-12-31"), "2024-2025": (2, "2024-01-01", "2025-12-31")}
ALREADY = {"Houston": "Nine-Cities", "San Antonio": "Nine-Cities", "Austin": "Nine-Cities", "Fort Worth": "Nine-Cities",
           "El Paso": "Nine-Cities", "Dallas": "Dallas", "Washington": "DC-Assault", "Baltimore": "Baltimore-Assault-Victims"}


def slug(city):
    return re.sub(r"[^a-z0-9]+", "_", city.lower().replace(".", "")).strip("_")


def load():
    rows = list(csv.DictReader(open(ROOT / "out/eligibility.csv")))
    out = []
    for r in rows:
        if r["status"] != "yes" or r["window"] not in WINDOWS or r["ori"] in LEFT_OUT:
            continue
        tier, start, end = WINDOWS[r["window"]]
        name = "DC" if r["state"] == "DC" else r["city"]
        out.append({"slug": slug(name), "city": r["city"], "state": r["state"], "name": name, "place": r["place"],
                    "ori": r["ori"], "agency": r["agency"], "geoid": r["census_geoid"], "tier": tier, "start": start, "end": end,
                    "population": int(r["population"]), "agency_population": int(float(r["agency_population"])),
                    "area_ratio": float(r["area_ratio"]), "black_women": int(r["black_women"]),
                    "hispanic_women": int(r["hispanic_women"]), "white_women": int(r["white_women"]),
                    "asian_women": int(r["asian_women"]), "flags": r["flags"], "already": ALREADY.get(r["city"])})
    return out


CITIES = load()
STATES = sorted({c["state"] for c in CITIES})

if __name__ == "__main__":
    for t in (1, 2):
        cs = [c for c in CITIES if c["tier"] == t]
        print(f"tier {t}: {len(cs)} cities")
        for c in cs:
            print(f"  {c['slug']:18} {c['state']} {c['ori']} {c['geoid']} {c['start']} to {c['end']}" + (f"  [{c['already']}]" if c["already"] else ""))
    print(len(STATES), "states:", " ".join(STATES))
