"""Every city side by side, tier 1 (2022 to 2025) and tier 2 (2024 to 2025) apart, from each city's outputs and the screen.

For each city: Black women's rate and the ratio to Hispanic, White and Asian women; the screen's bounds on the Hispanic and
White ratios (race-coding worst case and ethnicity scenarios); age-standardized ratios; aggravated against simple
assault; partner assault share and the ratios with and without it; women's rate against men's; the first half of the
window against the second; what is unknown. Then a check of the eight cities analyzed before (Houston, San Antonio,
Dallas, Austin, Fort Worth, DC, El Paso, Baltimore) against their earlier results, read from the Nine-Cities project's
out/comparison.json, and the cities left out with their reasons. All cities use the FBI's NIBRS files and the same
decisions; compare patterns, not levels.

  python scripts/compare.py      ->  out/comparison.json, out/comparison.md   (run screen.py first)
"""
import csv
import json
import pathlib

from cities import CITIES, LEFT_OUT, NEAR_MISSES

ROOT = pathlib.Path(__file__).resolve().parent.parent
NINE = ROOT.parent / "Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025/out/comparison.json"
OTHERS = ["Hispanic", "White", "Asian"]
SMALL = 50  # comparison-group victims under which a ratio is shown with its count
EARLIER = {"Houston": "houston", "San Antonio": "san_antonio", "Dallas": "dallas", "Austin": "austin", "Fort Worth": "fort_worth",
           "DC": "dc", "El Paso": "el_paso", "Baltimore": "baltimore"}


def rnd(v, n=2):
    return None if v is None else round(v, n)


def ratio(a, b):
    return rnd(a / b) if a and b else None


def row(c, s):
    d = ROOT / "cities" / c["slug"]
    R = json.loads((d / "out/results.json").read_text())
    t = R["tests"]
    std = t["age"]["standardized"]
    fl = t.get("flags", {}).get("partner")
    time = t["time"]
    ys = sorted(time)
    # where the department does not record ethnicity there is no Hispanic rate: every Hispanic figure is left out
    groups = [g for g in OTHERS if not (g == "Hispanic" and s["ethnicity_recording"] == "not recorded")]
    keep = lambda d_: {g: (d_ or {}).get(g) if g in groups else None for g in OTHERS}
    half = lambda part: keep({g: ratio(sum(time[y]["Black"] for y in part), sum(time[y][g] for y in part)) for g in OTHERS})
    return {
        "slug": c["slug"], "city": c["name"], "state": c["state"], "tier": c["tier"], "window": s["window"], "ori": c["ori"],
        "black_women_rate": R["rates"]["Black"]["F"], "rates_women": {g: R["rates"][g]["F"] for g in R["rates"]},
        "black_men_rate": R["rates"]["Black"]["M"], "ratio": keep(s["ratio"]), "ci95": keep(s["ci95"]), "bounds": s["bounds"],
        "ethnicity_recording": s["ethnicity_recording"],
        "race_coding_worst": s["race_coding_worst"], "ethnicity_scenarios": s["ethnicity_scenarios"],
        "age_standardized": keep({g: ratio(std["Black"], std.get(g)) for g in OTHERS}),
        "aggravated": keep({g: ratio(t["type"]["aggravated"]["Black"], t["type"]["aggravated"][g]) for g in OTHERS}),
        "simple": keep({g: ratio(t["type"]["simple"]["Black"], t["type"]["simple"][g]) for g in OTHERS}),
        "partner_share": fl["share"] if fl else None,
        "partner_ratio": keep(fl["ratios"]["flagged"]) if fl else None, "non_partner_ratio": keep(fl["ratios"]["unflagged"]) if fl else None,
        "women_over_men": R["ratio_to_other_sex"],
        "halves": {"years": [ys[:len(ys) // 2], ys[len(ys) // 2:]], "first": half(ys[:len(ys) // 2]), "second": half(ys[len(ys) // 2:])},
        "women_victims": s["women_by_group"], "women_residents": s["women_residents"],
        "unknown_race_pct": s["unknown_race_pct"], "outside_groups_pct": s["outside_groups_pct"],
        "unknown_ethnicity_pct": s["unknown_ethnicity_pct"], "unknown_relationship_pct": s["unknown_relationship_pct"],
        "combo_ratio": s["combo_ratio"], "flags": s["flags"], "already": c["already"],
    }


def counts(rows):
    """Counts over the cities where each comparison exists (no Hispanic comparison where ethnicity is not recorded)."""
    has = {g: [r for r in rows if r["ratio"][g] is not None] for g in ("Hispanic", "White")}
    out = {"cities": len(rows), "with_comparison": {g: len(has[g]) for g in has},
           "ratio_above_1": {g: sum(r["ratio"][g] > 1 for r in has[g]) for g in has},
           "lowest_bound_above_1": {g: sum(r["bounds"][g][0] > 1 for r in has[g]) for g in has},
           "aggravated_gap_wider": {g: sum((r["aggravated"][g] or 0) > (r["simple"][g] or 0) for r in has[g]) for g in has},
           "ratio_range": {}}
    for g in has:  # ranges leave out cities that do not record ethnicity, whose White ratio runs low by construction
        pool = [r for r in has[g] if r["ethnicity_recording"] != "not recorded"]
        lo, hi = min(pool, key=lambda r: r["ratio"][g]), max(pool, key=lambda r: r["ratio"][g])
        out["ratio_range"][g] = [[lo["city"], lo["ratio"][g]], [hi["city"], hi["ratio"][g]]]
    out["white_ratio_not_recorded"] = {r["city"]: r["ratio"]["White"] for r in rows if r["ethnicity_recording"] == "not recorded"}
    rate_lo, rate_hi = min(rows, key=lambda r: r["black_women_rate"]), max(rows, key=lambda r: r["black_women_rate"])
    out["rate_range"] = [[rate_lo["city"], rate_lo["black_women_rate"]], [rate_hi["city"], rate_hi["black_women_rate"]]]
    return out


def race_only_note():
    """Why there is no race-only fallback, from out/race_only.json (scripts/race_only.py), if it has been run."""
    path = ROOT / "out/race_only.json"
    if not path.exists():
        return ""
    ro = json.loads(path.read_text())
    recorded = {r["slug"] for r in json.loads((ROOT / "out/screen.json").read_text()) if r["ethnicity_recording"] == "recorded"}
    police = sorted(r["hispanic_women_victims_recorded_white_pct"] for r in ro if r["slug"] in recorded and r["hispanic_women_victims_recorded_white_pct"] is not None)
    census = [r["hispanic_residents_white_alone_pct"] for r in ro]
    return ("A race-only fallback (recorded White against White-alone residents of any ethnicity) is not used: officers record most Hispanic victims as White "
            f"(median {police[len(police) // 2]:.0f}% of Hispanic women victims where ethnicity is recorded), while {min(census):.0f}% to {max(census):.0f}% of "
            "Hispanic residents report White alone to the Census, so it overstates the White rate wherever Hispanic residents are many "
            "(`out/race_only.json`). ")


def main():
    screen = {s["slug"]: s for s in json.loads((ROOT / "out/screen.json").read_text())}
    rows = [row(c, screen[c["slug"]]) for c in CITIES if c["slug"] in screen]
    rows.sort(key=lambda r: (r["tier"], -r["black_women_rate"]))
    tiers = {t: [r for r in rows if r["tier"] == t] for t in (1, 2)}
    summary = {f"tier_{t}": counts(tr) for t, tr in tiers.items() if tr}

    earlier = {r["city"]: r for r in json.loads(NINE.read_text())} if NINE.exists() else {}
    check = []
    for name, slug in EARLIER.items():
        now = next((r for r in rows if r["slug"] == slug), None)
        was = earlier.get(name)
        if now and was:
            check.append({"city": name, "earlier_source": f"{was['source']}, {was['window']}", "now": f"FBI NIBRS, {now['window']}",
                          "earlier": {"rate": was["black_women_rate"], **{g: was["ratio"][g] for g in ("Hispanic", "White")}},
                          "now_values": {"rate": now["black_women_rate"], **{g: now["ratio"][g] for g in ("Hispanic", "White")}},
                          "like_for_like": was["source"] == "FBI NIBRS" and was["window"] == now["window"],
                          "same": was["black_women_rate"] == now["black_women_rate"] and all(was["ratio"][g] == now["ratio"][g] for g in ("Hispanic", "White"))})

    elig = {r["city"]: r for r in csv.DictReader(open(ROOT / "out/eligibility.csv"))}
    left = [{"city": f"{e['city']}, {e['state']}", "ori": e["ori"], "reason": LEFT_OUT[e["ori"]].split(": ", 1)[1]}
            for e in elig.values() if e["ori"] in LEFT_OUT]
    left += [{"city": f"{m}, {elig[m]['state']}", "ori": elig[m]["ori"],
              "reason": f"{elig[m]['reason']}; complete {elig[m]['longest_complete_span']} ({int(float(elig[m]['longest_complete_months']))} months)"} for m in NEAR_MISSES]

    out = {"summary": summary, "rows": rows, "check_against_earlier": check, "left_out": left}
    (ROOT / "out/comparison.json").write_text(json.dumps(out, indent=1) + "\n")

    f = lambda v: "n/a" if v is None else (f"{v:,}" if isinstance(v, int) else f"{v}")
    rng = lambda b: "n/a" if b is None else f"{b[0]} to {b[1]}"
    L = ["# Large US cities: Black women's reported assault rate against other women's", "",
         "Women victims of aggravated and simple assault reported to each city's own police department, per 100,000 residents a year, from the FBI's NIBRS files. "
         "Generated by `scripts/compare.py` from each city's outputs and `out/screen.json`. Tiers apart: tier 1 covers 2022 to 2025, tier 2 only 2024 to 2025.", ""]
    for t, tr in tiers.items():
        if not tr:
            continue
        sm = summary[f"tier_{t}"]
        wc, rr = sm["with_comparison"], sm["ratio_range"]
        no_eth = [r["city"] for r in tr if r["ethnicity_recording"] == "not recorded"]
        h_only = [r["city"] for r in tr if r["ethnicity_recording"] == "Hispanic only"]
        L += [f"## Tier {t}: {'2022 to 2025' if t == 1 else '2024 to 2025'} ({len(tr)} cities)", "",
              f"Black women's rate is higher than White women's in {sm['ratio_above_1']['White']} of {wc['White']} and Hispanic women's in {sm['ratio_above_1']['Hispanic']} of {wc['Hispanic']}"
              + (f" ({len(no_eth)} do not record ethnicity: {', '.join(no_eth)})" if no_eth else "") + ". "
              + (f"{len(h_only)} record ethnicity only as Hispanic ({', '.join(h_only)}), so their Hispanic ratios cannot be bounded for ethnicity. " if h_only else "") +
              f"The lowest bound stays above 1 against White women in {sm['lowest_bound_above_1']['White']} cities and against Hispanic women in {sm['lowest_bound_above_1']['Hispanic']}. "
              f"Against White women the ratio runs from {rr['White'][0][1]} ({rr['White'][0][0]}) to {rr['White'][1][1]} ({rr['White'][1][0]})"
              + (" where ethnicity is recorded (" + ", ".join(f"{k} {v}" for k, v in sm["white_ratio_not_recorded"].items()) + " where it is not, which run low)" if sm["white_ratio_not_recorded"] else "")
              + f"; against Hispanic women from {rr['Hispanic'][0][1]} ({rr['Hispanic'][0][0]}) to {rr['Hispanic'][1][1]} ({rr['Hispanic'][1][0]}). "
              f"The gap with White women is wider for aggravated than simple assault in {sm['aggravated_gap_wider']['White']} of {wc['White']}.", "",
              "| City | Black women | vs Hispanic [95% interval] | vs White [95% interval] | vs Asian [95% interval] | Bounds vs Hispanic | Bounds vs White | Age-standardized vs Hispanic, White | Aggravated / simple vs White | Partner share, Black women vs others | vs Hispanic with / without partner | Halves vs Hispanic | Halves vs White | Black women victims | Ethnicity | Flags |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in tr:
            ps = r["partner_share"]
            known = [ps[g] for g in OTHERS if ps and ps.get(g) is not None and r["ratio"][g] is not None]
            share = (f"{ps['Black']}% vs " + (f"{min(known)}%" if min(known) == max(known) else f"{min(known)}% to {max(known)}%")) if known else "n/a"
            both = lambda a, b: "n/a" if a is None and b is None else f"{f(a)} then {f(b)}"
            # a ratio that rests on fewer than 50 victims in the comparison group carries its count
            rv = lambda g: f(r["ratio"][g]) + (f" ({r['women_victims'][g]} victims)" if r["ratio"][g] is not None and r["women_victims"][g] < SMALL else "")
            pr = f"{f(r['partner_ratio']['Hispanic'])} / {f(r['non_partner_ratio']['Hispanic'])}" if r["partner_ratio"] and r["partner_ratio"]["Hispanic"] else "n/a"
            h = r["halves"]
            eth = r["ethnicity_recording"] + (f", {r['unknown_ethnicity_pct']}% unknown" if r["ethnicity_recording"] == "recorded" else "")
            ci = lambda g: f" [{r['ci95'][g][0]}, {r['ci95'][g][1]}]" if r["ci95"].get(g) else ""
            L.append(f"| {r['city'] if r['city'] == r['state'] else r['city'] + ', ' + r['state']} | {r['black_women_rate']:,} | {rv('Hispanic')}{ci('Hispanic')} | {rv('White')}{ci('White')} | {rv('Asian')}{ci('Asian')} | "
                     f"{rng(r['bounds']['Hispanic'])} | {rng(r['bounds']['White'])} | {f(r['age_standardized']['Hispanic'])}, {f(r['age_standardized']['White'])} | "
                     f"{f(r['aggravated']['White'])} / {f(r['simple']['White'])} | {share} | {pr} | {both(h['first']['Hispanic'], h['second']['Hispanic'])} | "
                     f"{both(h['first']['White'], h['second']['White'])} | {f(r['women_victims']['Black'])} | {eth} | {'; '.join(r['flags']) or 'none'} |")
        L.append("")
    if check:
        L += ["## Check against the earlier analyses", "",
              "The eight cities analyzed before, re-run here. Rate is Black women per 100,000 a year; ratios against Hispanic and White women. "
              "Like for like means the same source and years, where the numbers should match exactly.", "",
              "| City | Earlier source | Earlier: rate, vs Hispanic, vs White | Now | Now: rate, vs Hispanic, vs White | Like for like | Same |", "|---|---|---|---|---|---|---|"]
        for k in check:
            e, n_ = k["earlier"], k["now_values"]
            L.append(f"| {k['city']} | {k['earlier_source']} | {e['rate']:,}, {e['Hispanic']}, {e['White']} | {k['now']} | {n_['rate']:,}, {n_['Hispanic']}, {n_['White']} | {'yes' if k['like_for_like'] else 'no'} | {'yes' if k['same'] else 'no'} |")
        L.append("")
    L += ["## Left out but listed", "", "| City | ORI | Reason |", "|---|---|---|"]
    L += [f"| {x['city']} | {x['ori']} | {x['reason']} |" for x in left]
    L += ["", "Bounds span the race-coding worst case (every resident who is Black in combination counted as Black) and the ethnicity scenarios "
          "(White-race women with unknown ethnicity left as White, left out, split in the known proportion, or all Hispanic); where ethnicity is recorded "
          "only as Hispanic or not at all, the race-coding worst case only. Where it is not recorded there is no Hispanic comparison, and the ratio to White women runs low "
          "(White victims include Hispanic White victims; the denominator is non-Hispanic White residents). "
          + race_only_note() +
          "", "Caveats, as on the earlier pages:", "",
          "- This shows what, not why: the data says Black women are assaulted at a higher reported rate in these cities. It does not say why; nothing here measures causes or circumstances.",
          "- Reported crimes only: every number is a report that reached the police. Willingness to report, and recording practice, differ by group, area, city and time.",
          "- Reports, not people: someone assaulted twice counts twice, so a rate is not the share of people assaulted.",
          "- Who is recorded as Black: race is recorded by officers; the Census counts residents who are Black alone. The lowest bounds assume every resident who is Black alone or in combination is recorded as Black.",
          "- Sources and definitions differ by city: each department codes offenses its own way (intimidation, left out, runs from under 1% to over half of assault-type victims), so compare patterns across cities, not levels.",
          "- Not a national rate: these are the large cities whose own departments report complete NIBRS data, not a sample of the country."]
    (ROOT / "out/comparison.md").write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
