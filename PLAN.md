# National run: plan and decisions

Handoff from the session that built Dallas, the nine-city page and the eligibility count (2026-10-02).

## Decisions (made by Martin)

- **City set.** From `out/eligibility.csv`:
  - Tier 1: the 46 cities with `status=yes` and `window=2022-2025`, excluding Las Vegas. They run on 2022-01-01 to 2025-12-31.
  - Tier 2: the 13 cities with `window=2024-2025`. They run on 2024-01-01 to 2025-12-31 and are shown apart.
- **Left out but listed:** Las Vegas, whose department (NV0020100) covers 1.71 million people, 2.59x the city. Also the four near misses: Indianapolis, Atlanta, Riverside, Greensboro.
- **Method:** the same decisions as Dallas, unchanged.
  - Each city's own police department only.
  - Aggravated (13A) and simple (13B) assault, individual victims of any age. Officers, intimidation (13C) and homicide are out.
  - Hispanic of any race first. Partner flag from the relationship codes.
  - Black women against Hispanic, White and Asian women.
  - ACS 2020 to 2024 five-year population via Census Reporter.
- **Cities already analyzed** (Houston, San Antonio, Dallas, Austin, Fort Worth, DC, El Paso, and Baltimore in tier 2) are re-run through this pipeline. Their earlier results then serve as a check.
- **Flags, not exclusions:** a comparison group under 10,000 women (Cincinnati, St. Louis and Chesapeake for Hispanic women). Per-city unknown race and ethnicity found in step 5.

## Steps

1. **Fetch** the 27 states' FBI zips for 2022 to 2025 (about 3.5 GB) into `data/raw/<ST>-<year>.zip` with `.source.json`.
   - The states: AZ CA CO DC FL IL IN KY MA MD MI MN MO NC NE NJ NV NY OH OK OR PA TN TX VA WA WI.
   - Generalize `scripts/fetch_nibrs.py` from `~/Desktop/GIT/Nine-Cities-Assault-Victim-Rates-by-Race-and-Sex-2020-2025` (key `nibrs/incident/<year>/<ST>-<year>.zip`).
   - Symlink TX from the Dallas project instead of downloading it again.
2. **Flatten** each state-year with `nibrs.py flatten --ori ...` for that state's qualifying ORIs. Run at most 3 or 4 at once: the machine has 16 GB of RAM, and big states load large tables.
3. **Write configs.** Generalize the Nine-Cities `scripts/make_configs.py`: one `<city>/analysis.json` per city, with ORI, Census geoid and window by tier, all from `out/eligibility.csv`.
4. **Run the cities.** Generalize the Nine-Cities `scripts/run_cities.py` (audit, victims, denominators, tests in parallel). Before denominators, copy each city's place into its config. Keep `min_pop` at the kit default.
5. **Screen each city** from its outputs:
   - Unknown race, and unknown ethnicity among women victims (DC was 31%, Baltimore 42%).
   - Unknown relationship.
   - Bounds on the Hispanic and White ratios, as in the Nine-Cities `scripts/compare.py`.
   - Flag where a bound crosses 1.
6. **Compare.** Generalize `compare.py` to all cities, tiers apart. Build a page with `build_page.py` only when Martin asks.
7. **Publish only after his yes:** branch commit, fast-forward main, push, Pages, verify. No Claude co-author line. Name the repo for what it holds and its years, keeping the folder and repo names the same.

## Already here

- `out/eligibility.md` and `out/eligibility.csv`: every city's verdict, ORI, Census geoid, women by group, months and window.
- `scripts/fbi_months.py`: monthly counts from the FBI zips through HTTP Range requests (only agencies.csv and NIBRS_incident.csv), cached in `out/cache/fbi_<ST>.json`.
- `scripts/eligibility.py`: the rule.

## Status (2026-10-02, second session)

Steps 1 to 6 are done for all 59 cities (46 tier 1, 13 tier 2). No page, no repo, nothing published.

- **Outputs:** `out/comparison.md` (tiers apart, check against earlier results, cities left out, caveats), `out/screen.md`, `out/race_only.json`, `out/bias_review.md` (kit bias scan of the write-up: required caveats present). Each city's kit outputs are in `cities/<slug>/out/`.
- **Changes from the steps above:** configs live in `cities/<slug>/`, not the repo root. Census Reporter rate-limits (429, Retry-After about 10 minutes after about 100 requests), so `run_cities.py` runs denominators one city at a time and waits. `flatten_states.py` flattens only the years in each city's window.
- **Kit fix (committed to disparity-kit as ee55000, 2026-10-03):** `kit/nibrs.py` reads tables with `encoding_errors="replace"`. California's agencies.csv has a Latin-1 byte, which crashed the flatten.
- **Check:** the seven like-for-like re-runs (Houston, San Antonio, Dallas, Austin, Fort Worth, DC, El Paso) match their earlier rates and ratios exactly. Baltimore (now NIBRS 2024 to 2025, before legacy records 2022 to 2024) moves from 3,605, 1.62, 2.58 to 3,450, 1.48, 2.63.
- **Screen added beyond step 5:**
  - How each department records ethnicity.
  - The yearly level of assault victims.
  - The share of assault-type victims recorded as intimidation (13C), year by year.
  - Ratios resting on fewer than 50 victims.
  - The department's population against the city's.

### Decided (2026-10-03)

The five no-ethnicity cities stay, with the White ratio shown as a floor (≥) and no Hispanic comparison. Columbus stays on its full window, flagged. Tucson stays, flagged. The page is built (`scripts/build_page.py` → `index.html`, README results block) and checked:
- desktop and 375px render: no overflow, 10 of 10 charts;
- racial-discrimination check: required caveats present, unknown-race caveat added, prose ranges use only comparisons with 10,000+ women.

Published 2026-10-03 (step 7): commit 5f6cd30 on main, https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025, live at https://mngoh.github.io/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/ (Pages built 5f6cd30). PLAN.md is in the repo; .claude/ stays local (gitignored).

- **Added 2026-10-03:** exact Poisson 95% intervals on every ratio (`scripts/screen.py`; all 170 shown sit above 1) and a Limits list closing the page, which replaces the caveat cards.

### Decisions waiting for Martin (resolved above)

1. **Five cities do not record ethnicity:** Oklahoma City, Detroit, Tulsa, Cleveland, Toledo. Hispanic or not Hispanic is coded for under 2% of women victims. There is no Hispanic comparison. The ratio to White women runs low, because White victims include Hispanic White victims while the denominator is non-Hispanic White women (Detroit 1.15). A race-only fallback does not fix it: police record a median 96% of Hispanic women victims as White, while 9% to 37% of Hispanic residents report White alone (`out/race_only.json`). The options are to keep them with the flag or to leave them out of the White comparison too.
2. **Three record only Hispanic:** Columbus, Raleigh, Portland. "Not Hispanic" is almost never coded, so the Hispanic ratios cannot be bounded for ethnicity.
3. **Columbus coding change.** From November 2024 simple assault (13B) falls from about 950 to 530 victims a month while intimidation (13C) rises from about 330 to 800. Their sum is steady. Intimidation is 21% of assault-type victims in 2022 and 57% in 2025, and 2025 assault victims are 0.61 times the median year. The options:
   - Keep Columbus with the flag.
   - Cut Columbus to January 2022 to October 2024.
   - Count 13C in Columbus only, which breaks "same decisions".
4. **Tucson (tier 2).** All offenses, not only assaults, fall about 40% from late 2024; December 2024 has 1,458 incidents against about 3,500 earlier. It passed eligibility because the lower 2025 level pulled its own median down. This looks like incomplete reporting. Keep with the flag, or move it to the near-miss list?
5. **Smaller flags:**
   - Unknown race among women victims: Seattle 23.1%, Boston 17.5%, Tucson 14.7%, St. Paul 11.1%, New York 10.6%, Minneapolis 10.4%.
   - Lowest bound against Hispanic women at or below 1: Cincinnati 0.70 (under 10,000 Hispanic women), Baltimore 0.87, San Jose 0.88.
   - Intimidation drifting up: Buffalo, from 26.5% to 41.2%; Tulsa, from 21.3% to 32.5%.
   - Intimidation share overall runs from 0.1% (Newark) to 51% (New York), so compare levels across cities with care.
6. **Next, when Martin asks:** a page (`build_page.py`), then step 7.
