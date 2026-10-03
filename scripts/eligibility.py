"""Which US cities qualify for the national run, and why the rest do not.

Rule, fixed before looking at any results:
  1. 250,000+ residents (ACS 2020 to 2024 five-year estimates, Census places).
  2. Complete NIBRS data from the city's police department for 2022 to 2025: incidents in all 48 months, and no month
     under 60% of the department's median month (the kit's audit rule for a records-system break or a thin period).
  3. At least 10,000 Black women residents, so the focus group's rate is stable. A comparison group (Hispanic, White)
     under 10,000 women is kept but flagged as unstable, as Asian women are.
Flagged, not excluded: a department whose area differs from the Census city (county-wide or metro departments), since
its rates need a denominator matched to its area; cities already analyzed.

Inputs: out/cache/places_250k.json and places_women.json (Census Reporter), out/cache/fbi_<ST>.json (fbi_months.py).

  python scripts/eligibility.py      ->  out/eligibility.csv, out/eligibility.md
"""
import json
import pathlib
import re
import statistics

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIPS = {"01": "AL", "02": "AK", "04": "AZ", "05": "AR", "06": "CA", "08": "CO", "09": "CT", "10": "DE", "11": "DC", "12": "FL", "13": "GA",
        "15": "HI", "16": "ID", "17": "IL", "18": "IN", "19": "IA", "20": "KS", "21": "KY", "22": "LA", "23": "ME", "24": "MD", "25": "MA",
        "26": "MI", "27": "MN", "28": "MS", "29": "MO", "30": "MT", "31": "NE", "32": "NV", "33": "NH", "34": "NJ", "35": "NM", "36": "NY",
        "37": "NC", "38": "ND", "39": "OH", "40": "OK", "41": "OR", "42": "PA", "44": "RI", "45": "SC", "46": "SD", "47": "TN", "48": "TX",
        "49": "UT", "50": "VT", "51": "VA", "53": "WA", "54": "WV", "55": "WI", "56": "WY"}
MONTHS = [f"{y}-{m:02d}" for y in range(2022, 2026) for m in range(1, 13)]
DONE = {"Los Angeles", "Washington", "Baltimore", "Dallas", "Houston", "San Antonio", "Austin", "Fort Worth", "El Paso"}
FLOOR = 10000
OVERRIDE = {"Nashville-Davidson metropolitan government (balance), TN": "TN0190100"}  # listed as "Metropolitan Nashville Police Department"
LATE = [f"{y}-{m:02d}" for y in (2024, 2025) for m in range(1, 13)]  # the fallback window: the latest two full years


CONSOLIDATED = {"Indianapolis city (balance)": "Indianapolis", "Nashville-Davidson metropolitan government (balance)": "Nashville",
                "Louisville/Jefferson County metro government (balance)": "Louisville", "Lexington-Fayette": "Lexington", "Urban Honolulu": "Honolulu"}


def city_name(full):
    n = full.rsplit(",", 1)[0].strip()
    return CONSOLIDATED.get(n, n)


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z]", " ", str(s).lower())).strip()  # "Charlotte-Mecklenburg" -> "charlotte mecklenburg"


def main():
    places = json.loads((ROOT / "out/cache/places_250k.json").read_text())
    women = json.loads((ROOT / "out/cache/places_women.json").read_text())
    fbi = {}
    rows = []
    for geo, full, pop in places:
        st = FIPS[geo.split("US")[1][:2]]
        if st not in fbi:
            f = ROOT / f"out/cache/fbi_{st}.json"
            fbi[st] = json.loads(f.read_text()) if f.exists() else None
        name = city_name(full)
        w = women[geo]
        r = {"city": name, "state": st, "place": full, "census_geoid": geo, "population": int(pop),
             "black_women": int(w["Black"]), "hispanic_women": int(w["Hispanic"]), "white_women": int(w["White"]), "asian_women": int(w["Asian"])}
        ag = (fbi[st] or {}).get("agencies", {})
        if full in OVERRIDE:
            cands = [(OVERRIDE[full], ag.get(OVERRIDE[full]))]
        else:
            cands = [(o, a) for o, a in ag.items() if norm(a["name"]) == norm(name) or norm(a["name"]).startswith(norm(name) + " ")]
            city_type = [c for c in cands if c[1]["type"] == "City"]
            cands = sorted(city_type or cands, key=lambda c: -(c[1]["population"] or 0))
        if fbi[st] is None or not cands or cands[0][1] is None:
            r.update(status="no", reason="the police department does not report to NIBRS (not in the FBI's files)" if fbi[st] else "state files not read")
            rows.append(r)
            continue
        ori, a = cands[0]
        m = a["months"]
        counts = [m.get(k, 0) for k in MONTHS]
        present = sum(1 for c in counts if c > 0)
        med = statistics.median([c for c in counts if c > 0]) if present else 0
        thin = [k for k, c in zip(MONTHS, counts) if c < 0.6 * med]
        thin_late = [k for k in thin if k in LATE]
        ok = [c >= 0.6 * med for c in counts]  # longest stretch of complete months, for a per-city window
        best, run_start = (0, None), None
        for i, good in enumerate(ok + [False]):
            if good and run_start is None:
                run_start = i
            elif not good and run_start is not None:
                best = max(best, (i - run_start, run_start))
                run_start = None
        longest = best[0]
        longest_span = f"{MONTHS[best[1]]} to {MONTHS[best[1] + best[0] - 1]}" if best[0] else None
        ratio = (a["population"] or 0) / pop
        r.update(ori=ori, agency=a["name"] + (f" ({a['unit']})" if a.get("unit") and str(a["unit"]) != "nan" else ""), agency_type=a["type"],
                 agency_population=a["population"], nibrs_start=a["nibrs_start"], months_with_data=present,
                 thin_months=len(thin), first_full=next((k for k, c in zip(MONTHS, counts) if c >= 0.6 * med), None),
                 thin_list=";".join(thin[:6]) + (";..." if len(thin) > 6 else ""), area_ratio=round(ratio, 2),
                 longest_complete_months=longest, longest_complete_span=longest_span)
        reasons = []
        window = "2022-2025" if not thin else "2024-2025" if not thin_late else None
        if window is None:
            reasons.append(f"NIBRS incomplete in 2024 to 2025: {len(thin_late)} thin or missing months (" + ", ".join(thin_late[:4]) + (", ..." if len(thin_late) > 4 else "") + ")")
        if w["Black"] < FLOOR:
            reasons.append(f"{int(w['Black']):,} Black women, under {FLOOR:,}")
        flags = []
        if not 0.85 <= ratio <= 1.15:
            flags.append(f"department population {a['population']:,} is {ratio:.2f}x the city's")
        small = [g for g, k in (("Hispanic", "hispanic_women"), ("White", "white_women")) if r[k] < FLOOR]
        if small:
            flags.append(f"{' and '.join(small)} women under {FLOOR:,} (comparison unstable)")
        if name in DONE:
            flags.append("already analyzed")
        if window == "2024-2025":
            flags.append(f"2022 to 2025 incomplete: {len(thin)} thin or missing months, last {thin[-1]}")
        r.update(status="yes" if not reasons else "no", window=window if not reasons else None, reason="; ".join(reasons), flags="; ".join(flags))
        rows.append(r)
    df = pd.DataFrame(rows)
    df.to_csv(ROOT / "out/eligibility.csv", index=False)

    yes, no = df[df["status"] == "yes"], df[df["status"] == "no"]
    area = yes[yes["flags"].fillna("").str.contains("department population")]
    full, late = yes[yes["window"] == "2022-2025"], yes[yes["window"] == "2024-2025"]
    new = lambda d: d[~d["flags"].fillna("").str.contains("already analyzed")]
    L = ["# Which large US cities qualify", "",
         f"{len(df)} US cities have 250,000+ residents. With at least {FLOOR:,} Black women residents and complete NIBRS data from their own police department "
         f"(every month present, none under 60% of the department's median month), {len(full)} qualify for 2022 to 2025 ({len(new(full))} not yet analyzed), "
         f"and {len(late)} more qualify only for the latest two full years, 2024 to 2025. {len(no)} do not qualify. Generated by `scripts/eligibility.py`.", ""]
    for title, part in (("Qualify for 2022 to 2025", full), ("Qualify for 2024 to 2025 only", late)):
        L += [f"## {title}", "", "| City | Department (ORI) | Population | Black women | Hispanic women | White women | Flags |", "|---|---|---|---|---|---|---|"]
        for _, r in part.sort_values("population", ascending=False).iterrows():
            L.append(f"| {r['city']}, {r['state']} | {r['agency']} ({r['ori']}) | {r['population']:,} | {r['black_women']:,} | {r['hispanic_women']:,} | {r['white_women']:,} | {r['flags'] or ''} |")
        L.append("")
    L += ["## Do not qualify", "", "| City | Reason | Department (ORI) | NIBRS since |", "|---|---|---|---|"]
    for _, r in no.sort_values("population", ascending=False).iterrows():
        L.append(f"| {r['city']}, {r['state']} | {r['reason']} | {r.get('agency') if isinstance(r.get('agency'), str) else ''} ({r.get('ori') if isinstance(r.get('ori'), str) else ''}) | {r.get('nibrs_start') if isinstance(r.get('nibrs_start'), str) else ''} |")
    near = no[(no["longest_complete_months"].fillna(0) >= 24) & (no["black_women"] >= FLOOR)]
    L += ["", f"Near misses: {len(near)} cities that fail only on gaps still have at least two years of complete months in a row: "
          + "; ".join(f"{r['city']} ({int(r['longest_complete_months'])} months, {r['longest_complete_span']})" for _, r in near.sort_values("population", ascending=False).iterrows())
          + ". A per-city window over that stretch would bring them in, at the cost of windows that differ by city."]
    L += ["", f"{len(area)} qualifying departments cover an area that differs from the Census city by more than 15% (county or metro departments). "
               "Their rates need a population matched to the department's area, or they are left out."]
    (ROOT / "out/eligibility.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
