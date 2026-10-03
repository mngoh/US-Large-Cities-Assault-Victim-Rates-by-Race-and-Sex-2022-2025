"""Screen each city's outputs before comparing: what is unknown, and how far the two main ratios could move.

For every city with cities/<slug>/out/results.json, among women victims in the city's window:
  unknown race (race U or blank), and race outside the four compared groups (I, P, or unknown; the kit's count)
  unknown ethnicity (anything but H or N: U, X or blank), and the share coded N: a department that codes only H or leaves
  ethnicity unspecified (Columbus) makes unspecified the default, and the ethnicity scenarios then cannot bound anything
  unknown relationship (no relationship recorded, or only RU), overall and by group
  victims by month: months with no victims, and months under 60% of the window's median month
  a 95% interval for every ratio from counting noise alone (exact Poisson, conditional on the two counts); it leaves out
  repeat victimization, coding error and the bounds
  coding changes: each year's assault victims (13A and 13B) against the median year's, flagged outside 0.75 to 1.25; and
  the share of assault-type victims (13A, 13B, 13C) recorded as intimidation, flagged where it moves 10 points or more
  bounds on the Hispanic and White ratios, as in the Nine-Cities compare.py: the lowest and highest of the ratio as
  mapped, the race-coding worst case (every Black-in-combination resident counted as Black), and the ethnicity
  scenarios (White-race women with unknown ethnicity left as White, left out, split in the known proportion, or all
  Hispanic). A scenario that leaves a group with no victims has no ratio and is left out of the bounds; the split is
  left out where no White-race woman is coded N; and where N is coded for under 5% of women victims the scenarios are
  left out entirely (bounds from race coding only). A bound that reaches 1 or below is flagged.
  the department's population (FBI) against the city's (ACS): above 1 where the department also covers land outside the
  Census place, or where the city grew past the ACS five-year average; either way the rates run high by up to that factor
Flags, not exclusions. Thresholds: unknown race 5%+, unknown ethnicity 10%+, "not Hispanic" coded for under 5%, unknown
relationship 25%+, a compared group under 10,000 women, any thin or empty month, a year 25% above or below the median
year, intimidation share moving 10 points, a department population 1.08 times the city's or more.

  python scripts/screen.py      ->  out/screen.json, out/screen.md
"""
import json
import pathlib

import pandas as pd
from scipy.stats import beta

from cities import CITIES

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIMITS = {"unknown_race": 5, "unknown_ethnicity": 10, "unknown_relationship": 25, "small_group": 10000, "department_over_city": 1.08,
          "not_hispanic_codes": 5, "ethnicity_known": 5, "small_count": 50, "year_level": 0.25, "intimidation_shift": 10}
SHORT = {"Black": "B", "Hispanic": "H", "White": "W", "Asian": "A"}


def rnd(v, n=2):
    return None if v is None else round(v, n)


def rr_ci(a, pa, b, pb, level=0.95):
    """Exact 95% interval for the rate ratio (a/pa)/(b/pb) of two Poisson counts, conditional on a + b (Clopper-Pearson)."""
    if not a or not b:
        return None
    lo = beta.ppf((1 - level) / 2, a, b + 1)
    hi = beta.ppf(1 - (1 - level) / 2, a + 1, b)
    return [round(lo / (1 - lo) * pb / pa, 2), round(hi / (1 - hi) * pb / pa, 2)]


def pct(mask):
    return round(float(mask.mean() * 100), 1) if len(mask) else None


def screen(c):
    d = ROOT / "cities" / c["slug"]
    cfg = json.loads((d / "analysis.json").read_text())
    R = json.loads((d / "out/results.json").read_text())
    pop = json.loads((d / "out/population.json").read_text())
    raw = pd.concat([pd.read_csv(d / s["path"], dtype=str) for s in cfg["incidents"]])
    raw = raw[(raw["incident_date"] >= cfg["window"]["start"]) & (raw["incident_date"] <= cfg["window"]["end"] + " 23:59:59")]
    w = raw[raw["sex"] == "F"]
    group = w["race_group"].map(cfg["race_map"])
    n = {g: int((group == g).sum()) for g in cfg["groups"]}

    eth_unknown = ~w["ethnicity"].isin(["H", "N"])
    rel = w["relationship"].fillna("").str.split(";").apply(set)
    rel_unknown = rel.apply(lambda s: s <= {"RU", ""})

    # how the department records ethnicity: recorded (N coded for 5%+ of women victims), Hispanic only (H coded but hardly
    # ever N: unspecified is the default, as in Columbus), or not recorded (H or N for under 5%: Hispanic victims are not
    # identified, so there is no Hispanic rate, and White victims include Hispanic White victims against a non-Hispanic
    # White denominator, which pushes the White ratio down)
    not_hispanic_pct = pct(w["ethnicity"] == "N")
    known_eth_pct = pct(w["ethnicity"].isin(["H", "N"]))
    ethnicity = ("not recorded" if (known_eth_pct or 0) < LIMITS["ethnicity_known"] else
                 "Hispanic only" if (not_hispanic_pct or 0) < LIMITS["not_hispanic_codes"] else "recorded")

    # ethnicity scenarios and race-coding bound, as in the Nine-Cities compare.py, where ethnicity is recorded
    yrs = R["years"]
    popF = {g: pop["city"][g]["F"] for g in cfg["groups"]}
    rate = lambda k, g: k / popF[g] / yrs * 1e5
    fr = rate(n["Black"], "Black")
    ratio_of = lambda k, g: rnd(fr / rate(k, g)) if k > 0 else None  # a group left with no victims has no ratio
    wr = w[w["race"] == "W"]
    h, nn = int((wr["ethnicity"] == "H").sum()), int((wr["ethnicity"] == "N").sum())
    u = int((~wr["ethnicity"].isin(["H", "N"])).sum())
    sh = h / (h + nn) if h + nn else 0
    scen = None
    if ethnicity == "recorded":
        scen = {"as mapped": (n["Hispanic"], n["White"]), "unknown ethnicity left out": (n["Hispanic"], n["White"] - u),
                "split in known proportion": (n["Hispanic"] + sh * u, n["White"] - sh * u), "all Hispanic": (n["Hispanic"] + u, n["White"] - u)}
        scen = {k: {"Hispanic": ratio_of(a, "Hispanic"), "White": ratio_of(b, "White")} for k, (a, b) in scen.items()}
    ratio = {g: R["ratios"].get(g) for g in ("Hispanic", "White", "Asian")}
    worst = R["race_coding_bound"]["ratios_worst_case"]
    bounds = {}
    for g in ("Hispanic", "White"):
        if ratio[g] is None or (g == "Hispanic" and ethnicity == "not recorded"):
            bounds[g] = None
            continue
        vals = [ratio[g], worst[g]] + ([v[g] for v in scen.values() if v[g] is not None] if scen else [])
        bounds[g] = [min(vals), max(vals)]
    # unknown race at its most extreme: every unknown-race woman victim in the comparison group
    k_unknown = int((w["race"].isna() | (w["race"] == "U")).sum())
    unknown_extreme = {g: ratio_of(n[g] + k_unknown, g) for g in ("Hispanic", "White")}
    # counting noise: Poisson intervals for every ratio (they leave out repeat victimization, coding error and the bounds)
    ci95 = {g: (rr_ci(n["Black"], popF["Black"], n[g], popF[g]) if ratio[g] is not None and not (g == "Hispanic" and ethnicity == "not recorded") else None)
            for g in ("Hispanic", "White", "Asian")}

    months = pd.period_range(cfg["window"]["start"][:7], cfg["window"]["end"][:7], freq="M").astype(str)
    by_month = raw["incident_date"].str[:7].value_counts().reindex(months, fill_value=0)
    med = float(by_month.median())
    thin = [m for m, v in by_month.items() if v < 0.6 * med]

    # coding changes the all-offense eligibility count cannot see: the yearly level of assault victims, and the share of
    # assault-type victims recorded as intimidation (13C, left out by decision), year by year (Columbus moved simple
    # assaults to intimidation from November 2024)
    a = pd.read_csv(ROOT / f"data/interim/cities/{c['slug']}.csv", dtype=str, usecols=["victim_id", "incident_date", "offense_code", "victim_type"])
    a = a[(a["victim_type"] == "Individual") & a["offense_code"].isin(["13A", "13B", "13C"])
          & (a["incident_date"] >= cfg["window"]["start"]) & (a["incident_date"] <= cfg["window"]["end"] + " 23:59:59")]
    yearly = a.drop_duplicates(["victim_id", "offense_code"]).groupby([a["incident_date"].str[:4], "offense_code"]).size().unstack(fill_value=0)
    yearly = yearly.reindex(columns=["13A", "13B", "13C"], fill_value=0)
    level = (yearly["13A"] + yearly["13B"]) / float((yearly["13A"] + yearly["13B"]).median())
    share_13c = (yearly["13C"] / yearly.sum(axis=1) * 100).round(1)

    row = {
        "slug": c["slug"], "city": c["name"], "state": c["state"], "tier": c["tier"], "window": f"{c['start'][:4]} to {c['end'][:4]}",
        "ori": c["ori"], "department_over_city": c["area_ratio"], "victims": len(raw), "women_victims": len(w), "women_by_group": n,
        "women_residents": popF,
        "unknown_race_pct": pct(w["race"].isna() | (w["race"] == "U")),
        "outside_groups_pct": R["counts"]["unknown_race_share_by_sex"].get("F"),
        "unknown_ethnicity_pct": pct(eth_unknown),
        "unknown_ethnicity_pct_by_race": {g: pct(eth_unknown[w["race"] == SHORT[g]]) for g in ("Black", "White", "Asian")},
        "unknown_relationship_pct": pct(rel_unknown),
        "unknown_relationship_pct_by_group": {g: pct(rel_unknown[group == g]) for g in cfg["groups"]},
        "ethnicity_codes_women": {str(k): int(v) for k, v in w["ethnicity"].value_counts(dropna=False).items()},
        "ethnicity_recording": ethnicity, "not_hispanic_pct": not_hispanic_pct, "known_ethnicity_pct": known_eth_pct,
        "white_unknown_ethnicity": u, "unknown_race_extreme": unknown_extreme,
        "months_empty": [m for m, v in by_month.items() if v == 0], "months_thin": thin,
        "month_min_over_median": round(float(by_month.min()) / med, 2) if med else None,
        "assault_level_by_year": {y: round(float(v), 2) for y, v in level.items()},
        "intimidation_share_by_year": {y: float(v) for y, v in share_13c.items()},
        "intimidation_share_pct": round(float(yearly["13C"].sum() / yearly.values.sum() * 100), 1),
        "black_women_rate": R["rates"]["Black"]["F"], "ratio": ratio,
        "race_coding_worst": worst, "combo_ratio": R["race_coding_bound"]["combo_ratio"],
        "ethnicity_scenarios": scen, "bounds": bounds, "ci95": ci95,
    }
    flags = []
    if (row["unknown_race_pct"] or 0) >= LIMITS["unknown_race"]:
        ext = ", ".join(f"{g} {v}" for g, v in unknown_extreme.items() if v is not None and bounds.get(g))
        flags.append(f"unknown race {row['unknown_race_pct']}% of women victims (if all were in the comparison group: {ext})")
    if (row["unknown_ethnicity_pct"] or 0) >= LIMITS["unknown_ethnicity"]:
        flags.append(f"unknown ethnicity {row['unknown_ethnicity_pct']}% of women victims")
    if ethnicity == "not recorded":
        flags.append(f"ethnicity not recorded (Hispanic or not Hispanic for {known_eth_pct}% of women victims): no Hispanic comparison, "
                     "and White victims include Hispanic White victims, so the ratio to White women runs low")
    elif ethnicity == "Hispanic only":
        flags.append(f"'not Hispanic' coded for only {not_hispanic_pct}% of women victims: unspecified ethnicity is the default, "
                     "so the Hispanic comparison cannot be bounded (bounds from race coding only)")
    if (row["unknown_relationship_pct"] or 0) >= LIMITS["unknown_relationship"]:
        flags.append(f"unknown relationship {row['unknown_relationship_pct']}% of women victims")
    for g in ("Hispanic", "White", "Asian"):
        if popF[g] < LIMITS["small_group"]:
            flags.append(f"{g} women residents {popF[g]:,.0f}, under 10,000")
        if ratio[g] is not None and n[g] < LIMITS["small_count"]:
            flags.append(f"{g} ratio rests on {n[g]} women victims")
    for g in ("Hispanic", "White"):
        if bounds[g] and bounds[g][0] <= 1:
            flags.append(f"lowest bound vs {g} {bounds[g][0]}, at or below 1")
    if c["area_ratio"] >= LIMITS["department_over_city"]:
        flags.append(f"department population {c['agency_population']:,} is {c['area_ratio']}x the city's")
    off = {y: v for y, v in level.items() if not 1 - LIMITS["year_level"] <= v <= 1 + LIMITS["year_level"]}
    if off:
        flags.append("assault victims a year against the median year: " + ", ".join(f"{y} {v:.2f}x" for y, v in off.items()))
    if share_13c.max() - share_13c.min() >= LIMITS["intimidation_shift"]:
        flags.append(f"intimidation (13C, left out) moves from {share_13c.min()}% to {share_13c.max()}% of assault-type victims across years "
                     f"({', '.join(f'{y} {v}%' for y, v in share_13c.items())}): a coding change")
    if row["months_empty"] or thin:
        flags.append(f"{len(row['months_empty'])} empty and {len(thin)} thin months in the window ({', '.join(thin[:6])}{', ...' if len(thin) > 6 else ''})")
    row["flags"] = flags
    return row


def main():
    rows, missing = [], []
    for c in CITIES:
        if (ROOT / "cities" / c["slug"] / "out/results.json").exists():
            rows.append(screen(c))
        else:
            missing.append(c["slug"])
    (ROOT / "out/screen.json").write_text(json.dumps(rows, indent=1) + "\n")

    f = lambda v: "n/a" if v is None else f"{v}"
    rb = lambda r, g: "n/a" if r["bounds"][g] is None else f"{r['ratio'][g]} ({r['bounds'][g][0]} to {r['bounds'][g][1]})"
    L = ["# Screen: what is unknown, and how far the ratios could move", "",
         "Women victims of aggravated and simple assault in each city's window. Generated by `scripts/screen.py` from each city's outputs. "
         "Bounds span the ratio as mapped, the race-coding worst case and the four ethnicity scenarios; where ethnicity is recorded only as Hispanic "
         "or not at all, the race-coding worst case only, and no Hispanic ratio where it is not recorded. Flags, not exclusions: "
         "unknown race 5%+, unknown ethnicity 10%+, ethnicity recorded only as Hispanic or not at all, unknown relationship 25%+, a compared group under 10,000 women, a bound at or below 1, "
         "a thin (under 60% of the median) or empty month, a year of assault victims 25% above or below the median year, "
         "intimidation (13C) share of assault-type victims moving 10 points or more across years, a department population 1.08 times the city's or more.", ""]
    for t in (1, 2):
        tr = [r for r in rows if r["tier"] == t]
        if not tr:
            continue
        L += [f"## Tier {t}: {'2022 to 2025' if t == 1 else '2024 to 2025'} ({len(tr)} cities)", "",
              "| City | Department / city population | Intimidation share % | Women victims | Unknown race % | Outside groups % | Ethnicity | Unknown ethnicity % | Unknown relationship % | Lowest month / median | Black women rate | vs Hispanic (bounds) | vs White (bounds) | Flags |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in tr:
            L.append(f"| {r['city'] if r['city'] == r['state'] else r['city'] + ', ' + r['state']} | {r['department_over_city']} | {r['intimidation_share_pct']} | {r['women_victims']:,} | {f(r['unknown_race_pct'])} | {f(r['outside_groups_pct'])} | "
                     f"{r['ethnicity_recording']} | {f(r['unknown_ethnicity_pct'])} | {f(r['unknown_relationship_pct'])} | {f(r['month_min_over_median'])} | {r['black_women_rate']:,} | "
                     f"{rb(r, 'Hispanic')} | {rb(r, 'White')} | {'; '.join(r['flags']) or 'none'} |")
        L.append("")
    if missing:
        L += [f"Not yet run: {', '.join(missing)}.", ""]
    (ROOT / "out/screen.md").write_text("\n".join(L) + "\n")
    print(f"screened {len(rows)} cities" + (f"; not yet run: {', '.join(missing)}" if missing else ""))
    for r in rows:
        if r["flags"]:
            print(f"  {r['city']}: {'; '.join(r['flags'])}")


if __name__ == "__main__":
    main()
