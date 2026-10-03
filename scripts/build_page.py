"""Render the national page (index.html) and the README results block from out/comparison.json and out/screen.json.

Built to be read at a glance: a two-line lede, three points, four tiles, then the charts, each with a one-line note.
Uses the kit's page template and conventions (dark theme, red for Black women's measure, blues for the comparison
groups, outlined marks, Chart.js, no em dashes), with forms that stay readable for 59 cities on a phone: one range bar
per city (lowest bound to the ratio as recorded, against a line at 1), a dot plot of the three groups' rates, and a
scatter against the line of no change for each test. White women's marks use #0b9fd0, which passes the six palette
checks beside the red and blue on the dark surface (the template's light blue reads gray there). Every number is
generated from the outputs, which scripts/compare.py and scripts/screen.py build from each city's own results.

Decisions (Martin, 2026-10-03): where a department does not record ethnicity, the ratio to White women is shown as a
floor and there is no Hispanic comparison; Columbus and Tucson stay in, flagged.

  python scripts/build_page.py      ->  index.html, README.md block between <!-- results:start --> and <!-- results:end -->
"""
import csv
import json
import os
import pathlib
import sys

sys.path.insert(0, os.path.expanduser(os.environ.get("DISPARITY_KIT", "~/.claude/disparity-kit/kit")))
from build_page import TEMPLATE, esc, listing, x  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME = "US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025"
REPO = f"https://github.com/mngoh/{NAME}"
LIVE = f"https://mngoh.github.io/{NAME}/"
OTHERS = ["Hispanic", "White", "Asian"]
WHITE = "#0b9fd0"
SMALL = 50  # comparison-group victims under which a ratio carries a note
HIDE = 10  # comparison-group victims under which a ratio is not shown at all
WINDOW = {1: "2022 to 2025", 2: "2024 to 2025"}
CSS = """
    .pts { margin: 6px 0 0 18px; color: var(--muted); font-size: 14px; line-height: 1.7; }
    .pts li + li { margin-top: 4px; }
    .what { margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--border); color: var(--text); font-size: 14px; }
    .sub-title { font-size: 12px; font-weight: 600; color: var(--muted); margin: 0 0 10px; }
    .tbl-wrap { overflow-x: auto; margin-bottom: 24px; border: 1px solid var(--border); border-radius: 8px; }
    .tbl { border-collapse: collapse; width: 100%; font-size: 12px; }
    .tbl th, .tbl td { padding: 8px 12px; border-bottom: 1px solid var(--border); text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }
    .tbl th { color: var(--muted); font-weight: 600; font-size: 11px; white-space: normal; vertical-align: bottom; }
    .tbl th:first-child, .tbl td:first-child, .tbl th:last-child, .tbl td:last-child { text-align: left; }
    .tbl td:last-child { white-space: normal; min-width: 180px; color: var(--muted); }
    .tbl tr:last-child td { border-bottom: none; }
    details { margin-top: 12px; } details summary { cursor: pointer; color: var(--muted); font-size: 12px; }
    details .tbl-wrap { margin: 10px 0 0; } details .tbl td:last-child { min-width: 0; color: inherit; }
    .ci { color: var(--muted); font-size: 10px; }
    .howto { background: var(--surface); border: 1px solid var(--border); border-left: 3px solid var(--blue); border-radius: 0 8px 8px 0; padding: 14px 20px; margin: 0 0 20px; max-width: 900px; }
    .howto h4 { font-size: 13px; font-weight: 600; margin-bottom: 6px; } .howto ul { margin-left: 18px; color: var(--muted); font-size: 12px; line-height: 1.6; } .howto li + li { margin-top: 3px; }
    .limits { margin: 0 0 40px 18px; color: var(--muted); font-size: 13px; line-height: 1.6; max-width: 900px; }
    .limits li + li { margin-top: 6px; } .limits strong { color: var(--text); font-weight: 600; }
"""


def label(r):
    return r["city"] if r["city"] == r["state"] else f"{r['city']}, {r['state']}"


def word(n, cap=False):
    """Small counts in words, as at the start of a sentence."""
    w = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}.get(n, str(n))
    return w[0].upper() + w[1:] if cap else w


def n_of(k, n):
    return f"all {n}" if k == n else f"{k} of {n}"


def why_low(r):
    """Why the lowest bound against Hispanic women reaches 1, in a few words."""
    if r["women_residents"]["Hispanic"] < 10000:
        return "few Hispanic residents"
    if r["bounds"]["Hispanic"][0] == r["race_coding_worst"].get("Hispanic"):
        return "race-coding worst case"
    return f"ethnicity unknown for {r['unknown_ethnicity_pct']:.0f}%"


def main():
    C = json.loads((ROOT / "out/comparison.json").read_text())
    S = {s["slug"]: s for s in json.loads((ROOT / "out/screen.json").read_text())}
    rows = C["rows"]
    for r in rows:
        r["s"] = S[r["slug"]]
        r["floor"] = r["ethnicity_recording"] == "not recorded"
        r["h_only"] = r["ethnicity_recording"] == "Hispanic only"
    T = {t: [r for r in rows if r["tier"] == t] for t in (1, 2)}
    js = []

    # ---------- chart helpers ----------
    def box(cid, title, sub, height, extra=""):
        return (f'<div class="chart-box"><h3>{esc(title)}</h3><div class="chart-sub">{esc(sub)}</div>'
                f'<div class="chart-wrap" style="height:{height}px"><canvas id="{cid}" role="img" aria-label="{esc(title)}"></canvas></div>{extra}</div>')

    grid = lambda boxes, one=False: (f'<div class="charts section-end"{" style=\"grid-template-columns:1fr\"" if one else ""}>{"".join(boxes)}</div>')
    tall = lambda n: 70 + 20 * n

    def table(head, body):
        t = (f'<table class="tbl"><thead><tr>{"".join(f"<th>{esc(h)}</th>" for h in head)}</tr></thead><tbody>'
             + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in body) + "</tbody></table>")
        return f'<div class="tbl-wrap">{t}</div>'

    def ratio_chart(cid, rs, g, title, sub):
        """One range bar per city, from the lowest bound to the ratio as recorded; grey where it is a floor or unbounded."""
        rs = sorted(rs, key=lambda r: -r["ratio"][g])
        grey = (lambda r: r["floor"]) if g == "White" else (lambda r: r["h_only"])
        rng = lambda r: [r["bounds"][g][0], r["ratio"][g]]
        main_ = [None if grey(r) else rng(r) for r in rs]
        flag = [rng(r) if grey(r) else None for r in rs]
        flag_label = "Floor: no ethnicity data" if g == "White" else "Coded only as Hispanic"
        iv = lambda r: f", 95% interval {r['ci95'][g][0]} to {r['ci95'][g][1]}" if r["ci95"].get(g) else ""
        tips = {r["city"]: (f"at least {r['ratio'][g]}x{iv(r)}, lowest bound {r['bounds'][g][0]}x" if g == "White" and r["floor"]
                            else f"{r['ratio'][g]}x{iv(r)}, lowest bound {r['bounds'][g][0]}x") for r in rs}
        ds = [f"{{label:'Cautious estimate to recorded ratio',data:{json.dumps(main_)},...bar(C.red),grouped:false,maxBarThickness:12}}"]
        if any(flag):
            ds.append(f"{{label:{json.dumps(flag_label)},data:{json.dumps(flag)},...bar(C.muted),grouped:false,maxBarThickness:12}}")
        hi = max(r["ratio"][g] for r in rs)
        js.append(f"new Chart(document.getElementById('{cid}'),{{type:'bar',data:{{labels:{json.dumps([r['city'] for r in rs])},datasets:[{','.join(ds)}]}},"
                  f"options:{{...base,indexAxis:'y',layout:{{padding:{{top:16}}}},plugins:{{legend:{{display:true}},refLines:{{x:1,label:'1 = no gap'}},"
                  f"tooltip:{{callbacks:{{label:c=>({json.dumps(tips)})[c.label]}}}}}},"
                  f"scales:{{y:{{grid:{{display:false}},ticks:{{color:C.text,autoSkip:false}}}},x:{{min:0,suggestedMax:{max(2, round(hi + 0.5))},"
                  f"title:{{display:true,text:'Times {g} women\\'s rate'}}}}}}}}}});")
        return box(cid, title, sub, tall(len(rs)) + 24)

    def rate_chart(cid, rs, title, sub):
        """Dot plot: each city's rate for Black, Hispanic and White women."""
        rs = sorted(rs, key=lambda r: -r["black_women_rate"])
        labels = [r["city"] + (" †" if r["floor"] else "") for r in rs]
        series = [("Black women", [r["rates_women"]["Black"] for r in rs], "C.red"),
                  ("Hispanic women", [None if r["floor"] else r["rates_women"]["Hispanic"] for r in rs], "C.blue"),
                  ("White women", [r["rates_women"]["White"] for r in rs], "WHITE")]
        ds = ",".join(f"{{label:{json.dumps(lab)},data:{json.dumps(d)},...dot({col})}}" for lab, d, col in series)
        js.append(f"new Chart(document.getElementById('{cid}'),{{type:'line',data:{{labels:{json.dumps(labels)},datasets:[{ds}]}},"
                  f"options:{{...base,indexAxis:'y',interaction:{{mode:'nearest',axis:'y',intersect:false}},plugins:{{legend:{{display:true,labels:{{usePointStyle:true}}}},"
                  f"tooltip:{{callbacks:{{label:c=>c.dataset.label+': '+c.parsed.x.toLocaleString()}}}}}},"
                  f"scales:{{y:{{grid:{{display:false}},ticks:{{color:C.text,autoSkip:false}}}},x:{{min:0,title:{{display:true,text:'Victims per 100,000 a year'}},"
                  f"ticks:{{callback:v=>v.toLocaleString()}}}}}}}}}});")
        return box(cid, title, sub, tall(len(rs)) + 24)

    def test_chart(cid, rs, fx, fy, xt, yt, title, sub, g):
        """Scatter of each city's ratio before (x) and after (y) a cut, against the line where they are equal."""
        pts = lambda sel: [{"x": fx(r), "y": fy(r), "c": label(r)} for r in rs if sel(r) and fx(r) is not None and fy(r) is not None]
        sets = [("2022 to 2025", pts(lambda r: r["tier"] == 1 and not r["floor"]), "C.red", "circle"),
                ("2024 to 2025", pts(lambda r: r["tier"] == 2), "C.red", "triangle")]
        if g == "White":
            sets.append(("No ethnicity data", pts(lambda r: r["floor"]), "C.muted", "circle"))
        sets = [s for s in sets if s[1]]
        vals = [v for s in sets for p in s[1] for v in (p["x"], p["y"])]
        lo, hi = (int(min(vals)) - 0.5 if min(vals) > 1 else 0), int(max(vals)) + 1
        ds = ",".join(f"{{label:{json.dumps(lab)},data:{json.dumps(d)},...dot({col}),pointStyle:'{shape}'}}" for lab, d, col, shape in sets)
        js.append(f"new Chart(document.getElementById('{cid}'),{{type:'scatter',data:{{datasets:[{ds}]}},"
                  f"options:{{...base,plugins:{{legend:{{display:true,labels:{{usePointStyle:true}}}},refLines:{{diagonal:true}},"
                  f"tooltip:{{callbacks:{{label:c=>c.raw.c+': '+c.raw.x+'x, then '+c.raw.y+'x'}}}}}},"
                  f"scales:{{x:{{min:{lo},max:{hi},title:{{display:true,text:{json.dumps(xt)}}}}},y:{{min:{lo},max:{hi},title:{{display:true,text:{json.dumps(yt)}}}}}}}}}}});")
        body = [[esc(label(r)), WINDOW[r["tier"]], f"{fx(r)}x", f"{fy(r)}x"] for r in rs if fx(r) is not None and fy(r) is not None]
        return box(cid, title, sub, 300, f'<details><summary>Table</summary>{table(["City", "Years", xt, yt], body)}</details>')

    # ---------- numbers ----------
    stable = lambda rs, g: [r for r in rs if r["women_residents"][g] >= 10000]  # ranges in prose leave out unstable comparisons

    def stats(rs):
        withH = [r for r in rs if r["ratio"]["Hispanic"] is not None]
        recW = [r for r in rs if not r["floor"]]
        st = {
            "n": len(rs), "nH": len(withH), "floor": [r for r in rs if r["floor"]], "h_only": [r for r in rs if r["h_only"]],
            "aboveW": [r for r in rs if r["ratio"]["White"] > 1], "aboveH": [r for r in withH if r["ratio"]["Hispanic"] > 1],
            "holdW": [r for r in rs if r["bounds"]["White"][0] > 1], "failH": [r for r in withH if r["bounds"]["Hispanic"][0] <= 1],
            "loW": min(stable(recW, "White"), key=lambda r: r["ratio"]["White"]), "hiW": max(stable(recW, "White"), key=lambda r: r["ratio"]["White"]),
            "loH": min(stable(withH, "Hispanic"), key=lambda r: r["ratio"]["Hispanic"]), "hiH": max(stable(withH, "Hispanic"), key=lambda r: r["ratio"]["Hispanic"]),
            "sev": [r for r in rs if (r["aggravated"]["White"] or 0) > (r["simple"]["White"] or 0)],
            "age_std_above1": [r for r in rs if (r["age_standardized"]["White"] or 0) > 1],
            "age_down": [r for r in rs if r["age_standardized"]["White"] < r["ratio"]["White"] * 0.9],
        }
        rel = [r for r in withH if r["partner_ratio"] and r["partner_ratio"].get("Hispanic") and r["non_partner_ratio"].get("Hispanic")]
        st["rel"] = rel
        st["partner_smaller"] = [r for r in rel if r["partner_ratio"]["Hispanic"] < r["non_partner_ratio"]["Hispanic"]]
        st["non_partner_above1"] = [r for r in rel if r["non_partner_ratio"]["Hispanic"] > 1]
        med = lambda v: sorted(v)[len(v) // 2] if len(v) % 2 else (sorted(v)[len(v) // 2 - 1] + sorted(v)[len(v) // 2]) / 2
        st["medW"] = med([r["ratio"]["White"] for r in stable(recW, "White")])
        st["medH"] = med([r["ratio"]["Hispanic"] for r in stable(withH, "Hispanic")])
        asian = [r["ratio"]["Asian"] for r in rs if r["ratio"]["Asian"] is not None and r["women_victims"]["Asian"] >= SMALL]
        st["medA"], st["nA"] = (med(asian) if asian else None), len(asian)
        st["medRate"] = med([r["black_women_rate"] for r in rs])
        st["loRate"], st["hiRate"] = min(r["black_women_rate"] for r in rs), max(r["black_women_rate"] for r in rs)
        chg = lambda r: (r["halves"]["second"]["Hispanic"] / r["halves"]["first"]["Hispanic"] - 1) * 100
        st["narrowedH"] = [r for r in withH if chg(r) < -3]
        return st

    s1, s2 = stats(T[1]), stats(T[2])
    allr = rows
    total = sum(r["s"]["victims"] for r in allr)
    n_focus = sum(r["women_victims"]["Black"] for r in allr)
    n_other = sum(r["women_victims"][g] for r in allr for g in OTHERS if not (g == "Hispanic" and r["floor"]))
    every = lambda k, n: "every city" if k == n else f"{k} of {n} cities"
    cities_ = lambda rs: listing([r["city"] for r in rs])
    rngx = lambda lo, hi, g: f"{x(lo['ratio'][g])}x to {x(hi['ratio'][g])}x"

    lede = (f"In all {s1['n']} large US cities with complete police data for 2022 to 2025, Black women's reported assault rate is higher than White women's "
            f"(about {x(s1['medW'])} times in the typical city) and, in all {s1['nH']} that record ethnicity, higher than Hispanic women's (about {x(s1['medH'])} times). "
            "Nothing measured here explains why.")
    question = "Are Black women assaulted at a higher reported rate than Hispanic, White and Asian women across large US cities?"
    ivs = [r["ci95"][g] for r in rows for g in OTHERS if r["ci95"].get(g) and r["women_victims"][g] >= HIDE]
    n_above = sum(1 for c in ivs if c[0] > 1)
    points = [
        "It holds even under the most cautious assumptions about race recording and missing data: against White women in "
        + f"{every(len(s1['holdW']), s1['n'])}, against Hispanic women in "
        + (f"all but {listing([f'{r['city']} ({why_low(r)})' for r in s1['failH']])}." if s1["failH"] else "every city."),
        f"It survives the age and partner-assault checks: it stays above 1 after age standardization in {every(len(s1['age_std_above1']), s1['n'])} and outside partner assault "
        f"in {every(len(s1['non_partner_above1']), len(s1['rel']))}. It is widest for aggravated assault in {n_of(len(s1['sev']), s1['n'])}.",
        f"It is not chance: {('every one of the ' + str(len(ivs))) if n_above == len(ivs) else f'{n_above} of the {len(ivs)}'} ratios on this page has a 95% interval above 1.",
        f"Against Asian women it is larger still (about {x(s1['medA'])} times in the typical city), but on small counts, so it stays out of the headline.",
        f"The {s2['n']} cities with complete data only for 2024 to 2025, shown apart, look the same: higher than White women's in {n_of(len(s2['aboveW']), s2['n'])} "
        f"and Hispanic women's in {n_of(len(s2['aboveH']), s2['nH'])}.",
    ]
    FOLLOW = "https://github.com/mngoh/Police-Records-vs-Survey-Assault-Victims-by-Race-and-Sex-2015-2025"
    what = ("What this number measures: police reports, not how often women are hurt. In the national victimization survey, which counts assaults whether or not "
            "police learned of them, Black and White women describe being assaulted at about the same rate nationally and about 1.5 to 2 times in large cities. "
            "A follow-up tested why police records differ so much more: not reporting rates, not (or only a little) how police write up a call, not the same women counted repeatedly, "
            "but largely where assaults happen and who calls. Hospital emergency departments, which do not depend on a call to police, see a gap like the police one "
            "(about 5 times for women in 2022), which points to the survey undercounting assaults on Black women.")
    answer = ('<ul class="pts">' + "".join(f"<li>{esc(p)}</li>" for p in points) + "</ul>"
              + f'<p class="what">{esc(what)} <a href="{FOLLOW}">The follow-up.</a></p>')

    tiles = [("Higher than White women's", n_of(len(s1["aboveW"]), s1["n"]), f"typical gap {x(s1['medW'])}x ({rngx(s1['loW'], s1['hiW'], 'White')})"),
             ("Higher than Hispanic women's", n_of(len(s1["aboveH"]), s1["nH"]), f"typical gap {x(s1['medH'])}x, where ethnicity is recorded"),
             ("Black women's rate", f"about {round(s1['medRate'], -2):,.0f}", f"per 100,000 a year, typical city ({s1['loRate']:,} to {s1['hiRate']:,})"),
             ("2024 to 2025 cities", n_of(len([r for r in T[2] if r['ratio']['White'] > 1 and r['ratio']['Hispanic'] > 1]), s2["n"]), "higher than both groups")]
    cards_html = '<div class="cards">' + "".join(f'<div class="card"><div class="label">{esc(l_)}</div><div class="value">{esc(v)}</div><div class="sub">{esc(s)}</div></div>'
                                                 for l_, v, s in tiles) + "</div>"

    # ---------- overview ----------
    def tier_section(t, st, rs):
        head = f'<div class="section-title">{"2022 to 2025" if t == 1 else "2024 to 2025 only, shown apart"}: {len(rs)} cities</div>'
        w = ratio_chart(f"white{t}", rs, "White", "Against White women",
                        "Each bar: most cautious estimate to recorded ratio. Right of 1 = higher." + (" Grey = floor, no ethnicity data." if st["floor"] else ""))
        h = ratio_chart(f"hisp{t}", [r for r in rs if r["ratio"]["Hispanic"] is not None], "Hispanic", "Against Hispanic women",
                        "Each bar: most cautious estimate to recorded ratio." + (" Grey = ethnicity coded only as Hispanic." if st["h_only"] else ""))
        rate = rate_chart(f"rate{t}", rs, "Rates by city", "Victims per 100,000 residents a year. Red right of blue = higher for Black women." + (" † No ethnicity data." if st["floor"] else ""))
        return head + grid([rate], one=True) + grid([w, h])

    overview = tier_section(1, s1, T[1]) + tier_section(2, s2, T[2])

    # ---------- tests ----------
    withH = [r for r in allr if r["ratio"]["Hispanic"] is not None]
    rel_all = s1["rel"] + s2["rel"]
    sev = test_chart("sevChart", allr, lambda r: r["simple"]["White"], lambda r: r["aggravated"]["White"], "Simple assault", "Aggravated assault",
                     "Severity", f"Above the line = wider gap for aggravated assault ({len(s1['sev']) + len(s2['sev'])} of {len(allr)}).", "White")
    age = test_chart("ageChart", allr, lambda r: r["ratio"]["White"], lambda r: r["age_standardized"]["White"], "Crude", "Age-standardized",
                     "Age", "On the line = age changes nothing. Ratio to White women.", "White")
    par = test_chart("partnerChart", rel_all, lambda r: r["non_partner_ratio"]["Hispanic"], lambda r: r["partner_ratio"]["Hispanic"], "Other assault", "Partner assault",
                     "Partner assault", f"Below the line = smaller gap within partner assault ({len(s1['partner_smaller']) + len(s2['partner_smaller'])} of {len(rel_all)}).", "Hispanic")
    tim = test_chart("timeChart", withH, lambda r: r["halves"]["first"]["Hispanic"], lambda r: r["halves"]["second"]["Hispanic"], "First half", "Second half",
                     "Over time", f"Below the line = gap narrowed ({len(s1['narrowedH']) + len(s2['narrowedH'])} of {len(withH)}). Ratio to Hispanic women.", "Hispanic")
    tests = grid([sev, age, par, tim])

    # ---------- city by city ----------
    def notes(r):
        s = r["s"]
        out = []
        if r["floor"]:
            out.append("no ethnicity data")
        elif r["h_only"]:
            out.append("ethnicity coded only as Hispanic")
        elif s["unknown_ethnicity_pct"] >= 10:
            out.append(f"ethnicity unknown {s['unknown_ethnicity_pct']:.0f}%")
        if s["unknown_race_pct"] >= 5:
            out.append(f"race unknown {s['unknown_race_pct']:.0f}%")
        sh = s["intimidation_share_by_year"]
        if max(sh.values()) - min(sh.values()) >= 10:
            out.append("offense coding changed")
        off = [y for y, v in s["assault_level_by_year"].items() if v < 0.75]
        if off:
            out.append(f"{', '.join(off)} low")
        if r["women_residents"]["Hispanic"] < 10000 and r["ratio"]["Hispanic"] is not None:
            out.append("few Hispanic residents")
        for g in OTHERS:
            if r["ratio"][g] is not None and r["women_victims"][g] < SMALL:
                out.append(f"{r['women_victims'][g]} {g} victims")
        if s["department_over_city"] >= 1.08:
            out.append(f"department {s['department_over_city']}x city")
        return "; ".join(out)

    fx = lambda v: "n/a" if v is None else f"{v}x"
    shown = lambda r, g: "not shown" if r["ratio"][g] is not None and r["women_victims"][g] < HIDE else fx(r["ratio"][g])

    def cell(r, g):
        v = f"\u2265 {r['ratio'][g]}x" if g == "White" and r["floor"] else shown(r, g)
        ci = r["ci95"].get(g)
        return v + (f'<br><span class="ci">{ci[0]} to {ci[1]}</span>' if ci and v not in ("n/a", "not shown") else "")

    def city_rows(rs):
        return [[f'<a href="{REPO}/tree/main/cities/{r["slug"]}">{esc(label(r))}</a>', f"{r['black_women_rate']:,}", cell(r, "Hispanic"),
                 cell(r, "White"), cell(r, "Asian"),
                 fx(r["bounds"]["Hispanic"][0]) if r["bounds"]["Hispanic"] else "n/a", fx(r["bounds"]["White"][0]), esc(notes(r))]
                for r in sorted(rs, key=lambda r: r["city"])]

    head = ["City", "Black women per 100,000", "vs Hispanic", "vs White", "vs Asian", "Lowest bound vs Hispanic", "Lowest bound vs White", "Flags"]
    ex = next(r for r in rows if r["slug"] == "baltimore")
    howto = [
        "The ratio (for example 3x) is Black women's reported rate divided by the other group's.",
        "The small range under it is a 95% interval: where the true ratio probably sits given the counts. Chance alone does not explain a ratio whose interval is above 1.",
        "The lowest bound answers a different question: what if the recording is biased against the finding? It assumes every resident who is Black in combination is "
        "recorded as Black, and every White-race victim with unknown ethnicity is Hispanic. A gap that stays above 1 there survives both.",
        f"Example, {ex['city']}: {ex['ratio']['Hispanic']}x against Hispanic women, interval {ex['ci95']['Hispanic'][0]} to {ex['ci95']['Hispanic'][1]}, so not chance. "
        f"But ethnicity is unknown for {ex['unknown_ethnicity_pct']:.0f}% of its women victims, and the lowest bound is {ex['bounds']['Hispanic'][0]}x: the data cannot rule out that the gap is a recording artifact there.",
        "No bound is shown against Asian women; the counts are too small for it to mean much. A ratio on fewer than 10 victims is not shown. \u2265 marks a floor. Flags are not exclusions.",
    ]
    city_html = ('<div class="section-title">City by city</div>'
                 + '<div class="howto"><h4>How to read a row</h4><ul>'
                 + "".join(f"<li>{esc(t)}</li>" for t in howto) + '</ul></div>'
                 + "".join(f'<h3 class="sub-title">{WINDOW[t]}{"" if t == 1 else " only"}</h3>' + table(head, city_rows(T[t])) for t in (1, 2)))
    reporting = city_html

    # ---------- checked, and left out ----------
    chk = C["check_against_earlier"]
    same = [k["city"] for k in chk if k["like_for_like"] and k["same"]]
    elig = list(csv.DictReader(open(ROOT / "out/eligibility.csv")))
    left = [l_["city"].split(",")[0] for l_ in C["left_out"]]
    model = ('<div class="section-title">Checks</div><div class="findings">'
             f'<div class="finding"><h4>Earlier results reproduce</h4><p>{esc(f"{listing(same)}: same data and years, identical results.")}</p></div>'
             f'<div class="finding"><h4>Which cities</h4><p>{esc(f"{len(rows)} of {len(elig)} places of 250,000+ have 10,000+ Black women and complete police data. Left out: {listing(left)}.")}</p></div>'
             '</div>')

    # ---------- caveats ----------
    combo = [round((r["combo_ratio"] - 1) * 100) for r in rows if r.get("combo_ratio")]
    intim = {r["city"]: r["s"]["intimidation_share_pct"] for r in rows}
    i_lo, i_hi = min(intim, key=intim.get), max(intim, key=intim.get)
    floors = [r for r in rows if r["floor"]]
    unk = sorted([r for r in rows if r["s"]["unknown_race_pct"] >= 10], key=lambda r: -r["s"]["unknown_race_pct"])
    vanish = [r for r in unk if r["ratio"]["Hispanic"] is not None and (r["s"]["unknown_race_extreme"]["Hispanic"] or 0) <= 1.05]
    h_only = [r for r in rows if r["h_only"]]
    big = max(rows, key=lambda r: r["s"]["department_over_city"])
    smallH = [r for r in rows if r["women_residents"]["Hispanic"] < 10000 and r["ratio"]["Hispanic"] is not None]
    cav = [
        ("What, not why", "Shows how often assaults are reported, not why. Nothing here measures causes or offenders."),
        ("Police reports only", "Willingness to report, and where police patrol, differ by group, place and time. This data cannot separate them from differences in assaults."),
        ("Reports, not people", "Someone assaulted twice counts twice."),
        ("No neighborhood test here", "The FBI files have no victim location. Where neighborhoods were tested (Los Angeles, Baltimore, Dallas; New York's precincts in the follow-up), the gap narrowed but remained: about 3x within New York precincts of like composition."),
        ("Levels not comparable across cities", f"Departments code offenses differently: intimidation, left out, is {intim[i_lo]:.1f}% of assault-type victims in {i_lo} and {intim[i_hi]:.0f}% in {i_hi}. "
                                                "Compare ratios within a city, not rates across cities. Columbus changed its coding in November 2024; Tucson's 2025 looks incomplete."),
        ("Race recorded by officers", f"The Census counts Black alone; {min(combo)}% to {max(combo)}% more residents are Black alone or in combination, which sets the lowest bound."),
        ("Ethnicity", f"{word(len(floors), cap=True)} cities record none ({cities_(floors)}): no Hispanic comparison, and the ratio to White women is a floor. "
                      f"{word(len(h_only), cap=True)} code only Hispanic ({cities_(h_only)})."),
        ("Unknown race", f"Up to {unk[0]['s']['unknown_race_pct']:.0f}% of women victims ({unk[0]['city']}). If every one were in the comparison group, "
                         + (f"the gap with Hispanic women would vanish in {cities_(vanish)}; " if vanish else "")
                         + f"the gap with White women stays above {min(r['s']['unknown_race_extreme']['White'] for r in unk):.0f}x."),
        ("Intervals show counting noise only", "They leave out repeat victimization, coding error and the bounds above."),
        ("Where people live", f"Rates divide by residents, not where people spend time. A department serving more people than its city ({big['city']}, {big['s']['department_over_city']}x) runs high."),
        ("Small numbers", "Asian women's counts are small, so their ratios stay out of the headline"
                          + (f"; fewer than 10,000 Hispanic women live in {cities_(smallH)}." if smallH else ".")),
        ("Choices made after seeing the data", "The screen's thresholds, the typical-city medians and keeping Columbus and Tucson. All are disclosed; none were set in advance."),
        ("One department each", "Transit, school, campus and county police are not counted."),
        ("Not national", "Large cities with complete data, not a national sample."),
    ]
    limits_html = ('<div class="section-title">Limits</div><ul class="limits">'
                   + "".join(f"<li><strong>{esc(h)}.</strong> {esc(t)}</li>" for h, t in cav) + "</ul>")

    nav = f'<a href="{REPO}">Code</a><a href="https://martinngoh.com">martinngoh.com</a>'
    method = ("Women victims of aggravated and simple assault per 100,000 residents of each group a year, from each city's own police department in the FBI's NIBRS files; "
              "Hispanic of any race first. Population: ACS 2020 to 2024 via Census Reporter. Built with disparity-kit using the Dallas decisions.")

    pre = ("const WHITE = '" + WHITE + "';\n  "
           "const dot = c => ({ borderColor: C.surface, backgroundColor: c, borderWidth: 2, pointRadius: 5, pointHoverRadius: 7, pointHitRadius: 12, showLine: false });\n  "
           "Chart.register({ id: 'refLines', beforeDatasetsDraw(chart, args, o) {\n"
           "    const { ctx, chartArea: a, scales: { x, y } } = chart; if (!o || (!o.x && !o.diagonal)) return;\n"
           "    ctx.save(); ctx.strokeStyle = C.grey2; ctx.lineWidth = 1;\n"
           "    if (o.x) { const px = x.getPixelForValue(o.x); ctx.beginPath(); ctx.moveTo(px, a.top); ctx.lineTo(px, a.bottom); ctx.stroke();\n"
           "      if (o.label) { ctx.fillStyle = C.muted; ctx.font = '10px -apple-system, Segoe UI, Helvetica, Arial, sans-serif'; ctx.fillText(o.label, px + 4, a.top - 5); } }\n"
           "    if (o.diagonal) { const lo = Math.max(x.min, y.min), hi = Math.min(x.max, y.max); ctx.beginPath(); ctx.moveTo(x.getPixelForValue(lo), y.getPixelForValue(lo)); ctx.lineTo(x.getPixelForValue(hi), y.getPixelForValue(hi)); ctx.stroke(); }\n"
           "    ctx.restore(); } });")
    page = TEMPLATE.format(
        title=f"Assault victims in {len(rows)} large US cities", description=esc(lede), lede=esc(lede), author="Martin Ngoh", window="2022 to 2025", total=f"{total:,}",
        nav=nav, question=esc(question), answer=answer, cards=cards_html,
        overview=overview, tests=tests, reporting=reporting, model=model, replication="", caveats="", method=esc(method),
        js=pre + "\n  " + "\n  ".join(js), groups_n=f"{n_focus:,}", others_n=f"{n_other:,}", focus="Black women", sexw="women", sexw_cap="Women")
    page = page.replace("  </style>\n</head>", CSS + "  </style>\n</head>", 1)
    page = page.replace("</p>\n</div>\n<footer>", "</p>\n  " + limits_html + "\n</div>\n<footer>", 1)  # limits close the page
    page = page.replace('<div class="section-title">Dataset</div>', '<div class="section-title">At a glance</div>', 1)
    page = page.replace("Each cut asks whether a plain explanation accounts for the gap.", "Each chart tests one plain explanation.", 1)
    for bad in ["—", "–"]:
        page = page.replace(bad, ", " if bad == "—" else " to ")
    (ROOT / "index.html").write_text(page)
    print("wrote", ROOT / "index.html")
    print("\n" + lede + "\n\n" + "\n".join("- " + p for p in points))

    # ---------- README block ----------
    def md_rows(rs):
        ci = lambda r, g: f" ({r['ci95'][g][0]} to {r['ci95'][g][1]})" if r["ci95"].get(g) and shown(r, g) not in ("n/a", "not shown") else ""
        return [f"| [{label(r)}]({REPO}/tree/main/cities/{r['slug']}) | {r['black_women_rate']:,} | {shown(r, 'Hispanic')}{ci(r, 'Hispanic')} | "
                f"{('at least ' + fx(r['ratio']['White'])) if r['floor'] else fx(r['ratio']['White'])}{ci(r, 'White')} | "
                f"{fx(r['bounds']['Hispanic'][0]) if r['bounds']['Hispanic'] else 'n/a'} | {fx(r['bounds']['White'][0])} | {notes(r)} |" for r in sorted(rs, key=lambda r: r["city"])]
    hdr = ["| City | Black women per 100,000 | vs Hispanic (95% interval) | vs White (95% interval) | Lowest bound vs Hispanic | Lowest bound vs White | Flags |", "|---|---|---|---|---|---|---|"]
    L = ["<!-- results:start -->", f"**{lede}**", "", f"Live page: {LIVE}", ""] + [f"- {p}" for p in points] + ["", f"{what} [The follow-up]({FOLLOW})."]
    L += ["", "How to read a row:", ""] + [f"- {t}" for t in howto]
    L += ["", "2022 to 2025:", ""] + hdr + md_rows(T[1]) + ["", "2024 to 2025 only:", ""] + hdr + md_rows(T[2])
    L += ["", "Limits:", ""] + [f"- **{h}.** {t}" for h, t in cav] + ["<!-- results:end -->"]
    block = "\n".join(L)
    for bad in ["—", "–"]:
        block = block.replace(bad, ", " if bad == "—" else " to ")
    rd = ROOT / "README.md"
    s = rd.read_text()
    if "<!-- results:start -->" in s:
        a, b = s.index("<!-- results:start -->"), s.index("<!-- results:end -->") + len("<!-- results:end -->")
        s = s[:a] + block + s[b:]
    else:
        s = s.replace("## Which cities", "## Results\n\n" + block + "\n\n## Which cities", 1)
    rd.write_text(s)
    print("updated README results block")


if __name__ == "__main__":
    main()
