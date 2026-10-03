# Assault victims in 59 large US cities

Black women's reported assault rate against Hispanic, White and Asian women's, in every large US city whose own police department reports complete NIBRS data, measured exactly as in the Dallas analysis ([Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025](https://github.com/mngoh/Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025)). Built with [disparity-kit](https://github.com/mngoh/disparity-kit).

The full page is `index.html`. The comparison is `out/comparison.md` (numbers in `out/comparison.json`); the screen of what is unknown in each city is `out/screen.md`. Each city's config, victim files and kit outputs are in `cities/<city>/`. Decisions and run notes are in `PLAN.md`.

## Results

<!-- results:start -->
**In all 46 large US cities with complete police data for 2022 to 2025, Black women's reported assault rate is higher than White women's (about 3.8 times in the typical city) and, in all 41 that record ethnicity, higher than Hispanic women's (about 2.4 times). Nothing measured here explains why.**

Live page: https://mngoh.github.io/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/

- It holds even under the most cautious assumptions about race recording and missing data: against White women in every city, against Hispanic women in all but Cincinnati (few Hispanic residents).
- It survives the age and partner-assault checks: it stays above 1 after age standardization in every city and outside partner assault in every city. It is widest for aggravated assault in 45 of 46.
- Against Asian women it is larger still (about 10.2 times in the typical city), but on small counts, so it stays out of the headline.
- The 13 cities with complete data only for 2024 to 2025, shown apart, look the same: higher than White women's in all 13 and Hispanic women's in all 13.

2022 to 2025:

| City | Black women per 100,000 | vs Hispanic | vs White | Lowest bound vs Hispanic | Lowest bound vs White | Flags |
|---|---|---|---|---|---|---|
| [Arlington, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/arlington) | 3,582 | 2.38x | 2.58x | 2.12x | 2.32x |  |
| [Aurora, CO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/aurora) | 3,448 | 1.61x | 2.83x | 1.32x | 2.32x |  |
| [Austin, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/austin) | 4,197 | 2.07x | 4.86x | 1.66x | 3.89x |  |
| [Buffalo, NY](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/buffalo) | 3,717 | 1.51x | 2.36x | 1.33x | 2.08x | offense coding changed |
| [Charlotte, NC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/charlotte) | 3,614 | 2.12x | 4.57x | 1.25x | 4.22x | ethnicity unknown 60%; department 1.15x city |
| [Chesapeake, VA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/chesapeake) | 3,232 | 3.29x | 2.86x | 2.79x | 2.54x | few Hispanic residents; 3 Asian victims |
| [Chicago, IL](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/chicago) | 5,266 | 2.53x | 7.32x | 2.36x | 6.82x |  |
| [Cincinnati, OH](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/cincinnati) | 3,993 | 4.82x | 3.9x | 0.7x | 3.51x | ethnicity unknown 57%; few Hispanic residents; 43 Asian victims |
| [Cleveland, OH](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/cleveland) | 6,130 | n/a | at least 2.1x | n/a | 1.9x | no ethnicity data; race unknown 5% |
| [Colorado Springs, CO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/colorado_springs) | 3,025 | 3.07x | 3.38x | 1.97x | 2.17x | race unknown 6% |
| [Columbus, OH](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/columbus) | 2,991 | 3.05x | 3.04x | 2.7x | 2.7x | ethnicity coded only as Hispanic; race unknown 7%; offense coding changed; 2025 low |
| [DC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/dc) | 4,205 | 3.22x | 10.21x | 2.22x | 9.38x | ethnicity unknown 31%; race unknown 5% |
| [Dallas, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/dallas) | 3,798 | 2.26x | 3.91x | 2.11x | 3.64x |  |
| [Denver, CO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/denver) | 3,936 | 1.87x | 3.86x | 1.5x | 3.11x | ethnicity unknown 11% |
| [Detroit, MI](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/detroit) | 5,529 | n/a | at least 1.15x | n/a | 1.11x | no ethnicity data |
| [Durham, NC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/durham) | 2,634 | 1.6x | 5.44x | 1.44x | 4.97x |  |
| [El Paso, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/el_paso) | 2,036 | 1.67x | 1.83x | 1.18x | 1.29x |  |
| [Fort Wayne, IN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/fort_wayne) | 4,043 | 4.75x | 4.24x | 1.43x | 3.27x | ethnicity unknown 28% |
| [Fort Worth, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/fort_worth) | 2,675 | 2.19x | 3.06x | 1.95x | 2.72x |  |
| [Fresno, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/fresno) | 4,925 | 2.56x | 2.73x | 1.9x | 2.02x | ethnicity unknown 14% |
| [Henderson, NV](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/henderson) | 5,477 | 4.5x | 4.83x | 3.22x | 3.45x | department 1.08x city |
| [Houston, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/houston) | 4,193 | 2.43x | 3.76x | 2.23x | 3.44x |  |
| [Irving, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/irving) | 2,629 | 1.85x | 2.03x | 1.64x | 1.8x |  |
| [Jacksonville, FL](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/jacksonville) | 4,070 | 3.2x | 2.74x | 2.63x | 2.48x |  |
| [Kansas City, MO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/kansas_city) | 6,177 | 2.74x | 3.94x | 1.53x | 3.53x | ethnicity unknown 23% |
| [Lexington, KY](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/lexington) | 2,177 | 1.9x | 3.52x | 1.55x | 2.88x | 34 Asian victims |
| [Lubbock, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/lubbock) | 6,391 | 1.67x | 4.56x | 1.36x | 3.72x |  |
| [Memphis, TN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/memphis) | 6,371 | 2.41x | 3.8x | 2.34x | 3.7x |  |
| [Milwaukee, WI](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/milwaukee) | 4,435 | 3.11x | 5.51x | 2.85x | 5.07x |  |
| [Minneapolis, MN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/minneapolis) | 5,516 | 2.54x | 7.7x | 1.38x | 6.51x | ethnicity unknown 38%; race unknown 10% |
| [Nashville, TN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/nashville) | 5,374 | 2.11x | 3.46x | 1.9x | 3.12x |  |
| [Newark, NJ](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/newark) | 2,243 | 1.63x | 2.9x | 1.49x | 2.65x | race unknown 9%; 32 Asian victims |
| [Oklahoma City, OK](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/oklahoma_city) | 4,089 | n/a | at least 2.46x | n/a | 1.93x | no ethnicity data |
| [Philadelphia, PA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/philadelphia) | 2,738 | 1.85x | 3.36x | 1.5x | 3.08x | ethnicity unknown 14% |
| [Plano, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/plano) | 2,385 | 2.49x | 4.71x | 2.12x | 4.02x |  |
| [Portland, OR](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/portland) | 5,457 | 3.98x | 4.83x | 2.76x | 3.35x | ethnicity coded only as Hispanic |
| [Raleigh, NC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/raleigh) | 3,364 | 1.7x | 5.28x | 1.53x | 4.74x | ethnicity coded only as Hispanic |
| [San Antonio, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/san_antonio) | 3,872 | 1.84x | 2.22x | 1.43x | 1.73x |  |
| [San Diego, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/san_diego) | 2,837 | 2.74x | 4.39x | 2.02x | 3.24x |  |
| [Seattle, WA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/seattle) | 3,893 | 3.67x | 6.12x | 1.23x | 4.57x | ethnicity unknown 50%; race unknown 23% |
| [St. Louis, MO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/st_louis) | 3,676 | 2.47x | 3.58x | 1.21x | 3.37x | ethnicity unknown 14%; few Hispanic residents |
| [St. Paul, MN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/st_paul) | 4,227 | 3.58x | 5.91x | 1.95x | 4.68x | ethnicity unknown 25%; race unknown 11% |
| [Stockton, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/stockton) | 4,921 | 2.62x | 1.81x | 2.04x | 1.41x |  |
| [Toledo, OH](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/toledo) | 9,398 | n/a | at least 2.68x | n/a | 2.29x | no ethnicity data |
| [Tulsa, OK](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/tulsa) | 6,108 | n/a | at least 2.21x | n/a | 1.74x | no ethnicity data; offense coding changed |
| [Winston-Salem, NC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/winston_salem) | 5,672 | 2.63x | 2.85x | 2.17x | 2.57x |  |

2024 to 2025 only:

| City | Black women per 100,000 | vs Hispanic | vs White | Lowest bound vs Hispanic | Lowest bound vs White | Flags |
|---|---|---|---|---|---|---|
| [Bakersfield, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/bakersfield) | 4,005 | 3.25x | 3.31x | 2.53x | 2.57x |  |
| [Baltimore, MD](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/baltimore) | 3,450 | 1.48x | 2.63x | 0.87x | 2.5x | ethnicity unknown 32%; race unknown 6% |
| [Boston, MA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/boston) | 3,124 | 1.83x | 4.72x | 1.34x | 3.46x | ethnicity unknown 37%; race unknown 18% |
| [Jersey City, NJ](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/jersey_city) | 2,477 | 1.64x | 2.77x | 1.42x | 2.39x |  |
| [Long Beach, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/long_beach) | 3,326 | 2.57x | 2.96x | 2.09x | 2.41x | ethnicity unknown 20% |
| [Louisville, KY](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/louisville) | 4,242 | 2.83x | 3.41x | 2.12x | 2.97x | department 1.09x city |
| [New York, NY](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/new_york) | 2,216 | 1.41x | 4.92x | 1.17x | 4.09x | race unknown 11% |
| [North Las Vegas, NV](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/north_las_vegas) | 2,737 | 2.94x | 2.58x | 2.5x | 2.2x | 49 Asian victims; department 1.09x city |
| [Omaha, NE](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/omaha) | 5,127 | 3.54x | 5.4x | 2.18x | 4.18x | ethnicity unknown 19% |
| [Sacramento, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/sacramento) | 5,457 | 3.3x | 3.17x | 2.42x | 2.33x |  |
| [San Jose, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/san_jose) | 2,881 | 1.28x | 2.82x | 0.88x | 1.95x | race unknown 6% |
| [Tucson, AZ](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/tucson) | 3,171 | 2.49x | 2.96x | 1.76x | 2.09x | ethnicity unknown 34%; race unknown 15%; 2025 low; 43 Asian victims |
| [Virginia Beach, VA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/virginia_beach) | 2,658 | 3.3x | 3.1x | 1.18x | 2.59x | ethnicity unknown 26% |

Caveats:

- What, not why: Shows how often assaults are reported, not why. Nothing here measures causes or offenders.
- Reported crimes only: Willingness to report differs by group, place and time.
- Reports, not people: Someone assaulted twice counts twice.
- Where people live: Rates divide by residents, not where people spend time.
- Policing: More policing or more calls can look like more assaults.
- Race recorded by officers: The Census counts Black alone; 3% to 56% more residents are Black alone or in combination, which sets the lowest bound.
- Unknown race: Up to 23% of women victims (Seattle). If every one were in the comparison group, the gap with Hispanic women would vanish in Seattle and Boston; the gap with White women stays above 2x.
- Ethnicity: Five cities record none (Toledo, Cleveland, Tulsa, Detroit and Oklahoma City); three code only Hispanic (Portland, Raleigh and Columbus).
- Offense coding: Intimidation, left out, is 0.1% of assault-type victims in Newark and 51% in New York: compare patterns, not levels. Columbus changed its coding in November 2024; Tucson's 2025 looks incomplete.
- One department each: Transit, school, campus and county police are not counted.
- Small numbers: Asian women's counts are small, so their ratios stay out of the headline.
- Not national: Large cities with complete data, not a national sample.
<!-- results:end -->

## Which cities

Rule, fixed before any results: 250,000+ residents; at least 10,000 Black women residents; complete NIBRS data from the
city's own police department (every month present, none under 60% of the department's median month). The full window is
2022 to 2025 (tier 1, 46 cities); cities complete only for 2024 to 2025 are run on that window and shown apart (tier 2,
13 cities). Las Vegas is left out (its department covers 2.59 times the city's population), and four near misses
(Indianapolis, Atlanta, Riverside, Greensboro) are listed. See `out/eligibility.md`.

## Method

- Source: the FBI's NIBRS state files, 2022 to 2025, for 27 states. Each city is its own police department only; transit, school, campus and county agencies are left out.
- Offenses: aggravated (13A) and simple (13B) assault, individual victims of any age. Officers, intimidation and homicide are out.
- Groups: Hispanic of any race first, otherwise the recorded race. Partner flag from the victim-offender relationship.
- Population: ACS 2020 to 2024 five-year estimates via Census Reporter, for the Census place of each city.
- Screen: unknown race, ethnicity and relationship among women victims; how each department records ethnicity (recorded, only Hispanic, or not at all); bounds on the ratios to Hispanic and White women from the race-coding worst case and the ethnicity scenarios; thin months, yearly levels and the share of assault-type victims recorded as intimidation (coding changes the all-offense eligibility count cannot see). Flags, not exclusions.
- Not used: a race-only comparison (any ethnicity). Officers record most Hispanic victims as White while most Hispanic residents do not report White alone to the Census, so it overstates White women's rate (`out/race_only.json`).
- Not run: location tests (NIBRS has no victim location), city open-data replications and city-specific checks.

## Rebuild

Python from disparity-kit: `~/.claude/disparity-kit/.venv/bin/python`.

```bash
python scripts/fbi_months.py AZ CA ...      # monthly counts per agency (HTTP Range requests), for the eligibility count
python scripts/eligibility.py               # out/eligibility.md, out/eligibility.csv
python scripts/fetch_nibrs.py               # data/raw/<ST>-<year>.zip for the 27 states (Texas linked from the Dallas project)
python scripts/flatten_states.py            # data/interim/flat/<ST>-<year>.csv, each state's cities only, three at a time
python scripts/make_configs.py              # cities/<city>/analysis.json, the Dallas decisions for every city
python scripts/run_cities.py                # every city: audit and victims, then denominators one at a time (rate limit), then tests
python scripts/screen.py                    # out/screen.md, out/screen.json
python scripts/race_only.py                 # out/race_only.json, the check behind not using race alone
python scripts/compare.py                   # out/comparison.md, out/comparison.json, tiers apart, checked against earlier analyses
python scripts/build_page.py                # index.html and the results block above
```

`scripts/cities.py` holds the city list (tiers from `out/eligibility.csv`). The flatten needs disparity-kit from commit ee55000 on, which reads past a byte in California's agencies.csv that is not UTF-8.
