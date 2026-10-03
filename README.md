# Assault victims in 59 large US cities

Black women's reported assault rate against Hispanic, White and Asian women's, in every large US city whose own police department reports complete NIBRS data, measured exactly as in the Dallas analysis ([Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025](https://github.com/mngoh/Dallas-TX-Assault-Victim-Rates-by-Race-and-Sex-2022-2025)). Built with [disparity-kit](https://github.com/mngoh/disparity-kit).

The full page is `index.html`. The comparison is `out/comparison.md` (numbers in `out/comparison.json`); the screen of what is unknown in each city is `out/screen.md`. Each city's config, victim files and kit outputs are in `cities/<city>/`. Decisions and run notes are in `PLAN.md`.

## Results

<!-- results:start -->
**In all 46 large US cities with complete police data for 2022 to 2025, Black women's reported assault rate is higher than White women's (about 3.8 times in the typical city) and, in all 41 that record ethnicity, higher than Hispanic women's (about 2.4 times). Nothing measured here explains why.**

Live page: https://mngoh.github.io/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/

- It holds even under the most cautious assumptions about race recording and missing data: against White women in every city, against Hispanic women in all but Cincinnati (few Hispanic residents).
- It survives the age and partner-assault checks: it stays above 1 after age standardization in every city and outside partner assault in every city. It is widest for aggravated assault in 45 of 46.
- It is not chance: every one of the 170 ratios on this page has a 95% interval above 1.
- Against Asian women it is larger still (about 10.2 times in the typical city), but on small counts, so it stays out of the headline.
- The 13 cities with complete data only for 2024 to 2025, shown apart, look the same: higher than White women's in all 13 and Hispanic women's in all 13.

What this number measures: police reports, not how often women are hurt. In the national victimization survey, which counts assaults whether or not police learned of them, Black and White women describe being assaulted at about the same rate nationally and about 1.5 to 2 times in large cities. A follow-up tested why police records differ so much more: not reporting rates, not how police write up a call, not the same women counted repeatedly, but largely where assaults happen and who calls. Within New York precincts of like composition the gap is about 3 times, not 5. [The follow-up](https://github.com/mngoh/Police-Records-vs-Survey-Assault-Victims-by-Race-and-Sex-2015-2025).

How to read a row:

- The ratio (for example 3x) is Black women's reported rate divided by the other group's.
- The small range under it is a 95% interval: where the true ratio probably sits given the counts. Chance alone does not explain a ratio whose interval is above 1.
- The lowest bound answers a different question: what if the recording is biased against the finding? It assumes every resident who is Black in combination is recorded as Black, and every White-race victim with unknown ethnicity is Hispanic. A gap that stays above 1 there survives both.
- Example, Baltimore: 1.48x against Hispanic women, interval 1.39 to 1.58, so not chance. But ethnicity is unknown for 32% of its women victims, and the lowest bound is 0.87x: the data cannot rule out that the gap is a recording artifact there.
- No bound is shown against Asian women; the counts are too small for it to mean much. A ratio on fewer than 10 victims is not shown. ≥ marks a floor. Flags are not exclusions.

2022 to 2025:

| City | Black women per 100,000 | vs Hispanic (95% interval) | vs White (95% interval) | Lowest bound vs Hispanic | Lowest bound vs White | Flags |
|---|---|---|---|---|---|---|
| [Arlington, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/arlington) | 3,582 | 2.38x (2.29 to 2.48) | 2.58x (2.48 to 2.69) | 2.12x | 2.32x |  |
| [Aurora, CO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/aurora) | 3,448 | 1.61x (1.55 to 1.68) | 2.83x (2.71 to 2.96) | 1.32x | 2.32x |  |
| [Austin, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/austin) | 4,197 | 2.07x (2.01 to 2.14) | 4.86x (4.7 to 5.03) | 1.66x | 3.89x |  |
| [Buffalo, NY](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/buffalo) | 3,717 | 1.51x (1.43 to 1.59) | 2.36x (2.27 to 2.46) | 1.33x | 2.08x | offense coding changed |
| [Charlotte, NC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/charlotte) | 3,614 | 2.12x (2.05 to 2.18) | 4.57x (4.44 to 4.7) | 1.25x | 4.22x | ethnicity unknown 60%; department 1.15x city |
| [Chesapeake, VA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/chesapeake) | 3,232 | 3.29x (2.97 to 3.66) | 2.86x (2.73 to 2.99) | 2.79x | 2.54x | few Hispanic residents; 3 Asian victims |
| [Chicago, IL](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/chicago) | 5,266 | 2.53x (2.5 to 2.56) | 7.32x (7.19 to 7.46) | 2.36x | 6.82x |  |
| [Cincinnati, OH](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/cincinnati) | 3,993 | 4.82x (4.3 to 5.41) | 3.9x (3.75 to 4.06) | 0.7x | 3.51x | ethnicity unknown 57%; few Hispanic residents; 43 Asian victims |
| [Cleveland, OH](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/cleveland) | 6,130 | n/a | at least 2.1x (2.04 to 2.16) | n/a | 1.9x | no ethnicity data; race unknown 5% |
| [Colorado Springs, CO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/colorado_springs) | 3,025 | 3.07x (2.87 to 3.29) | 3.38x (3.2 to 3.58) | 1.97x | 2.17x | race unknown 6% |
| [Columbus, OH](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/columbus) | 2,991 | 3.05x (2.89 to 3.22) | 3.04x (2.96 to 3.11) | 2.7x | 2.7x | ethnicity coded only as Hispanic; race unknown 7%; offense coding changed; 2025 low |
| [DC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/dc) | 4,205 | 3.22x (3.08 to 3.37) | 10.21x (9.75 to 10.67) | 2.22x | 9.38x | ethnicity unknown 31%; race unknown 5% |
| [Dallas, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/dallas) | 3,798 | 2.26x (2.22 to 2.31) | 3.91x (3.8 to 4.01) | 2.11x | 3.64x |  |
| [Denver, CO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/denver) | 3,936 | 1.87x (1.81 to 1.94) | 3.86x (3.73 to 4.0) | 1.5x | 3.11x | ethnicity unknown 11% |
| [Detroit, MI](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/detroit) | 5,529 | n/a | at least 1.15x (1.12 to 1.18) | n/a | 1.11x | no ethnicity data |
| [Durham, NC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/durham) | 2,634 | 1.6x (1.51 to 1.7) | 5.44x (5.11 to 5.8) | 1.44x | 4.97x |  |
| [El Paso, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/el_paso) | 2,036 | 1.67x (1.56 to 1.79) | 1.83x (1.68 to 1.99) | 1.18x | 1.29x |  |
| [Fort Wayne, IN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/fort_wayne) | 4,043 | 4.75x (4.31 to 5.24) | 4.24x (4.04 to 4.45) | 1.43x | 3.27x | ethnicity unknown 28% |
| [Fort Worth, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/fort_worth) | 2,675 | 2.19x (2.13 to 2.25) | 3.06x (2.97 to 3.16) | 1.95x | 2.72x |  |
| [Fresno, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/fresno) | 4,925 | 2.56x (2.46 to 2.66) | 2.73x (2.62 to 2.85) | 1.9x | 2.02x | ethnicity unknown 14% |
| [Henderson, NV](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/henderson) | 5,477 | 4.5x (4.21 to 4.8) | 4.83x (4.59 to 5.07) | 3.22x | 3.45x | department 1.08x city |
| [Houston, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/houston) | 4,193 | 2.43x (2.39 to 2.46) | 3.76x (3.69 to 3.84) | 2.23x | 3.44x |  |
| [Irving, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/irving) | 2,629 | 1.85x (1.75 to 1.96) | 2.03x (1.89 to 2.19) | 1.64x | 1.8x |  |
| [Jacksonville, FL](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/jacksonville) | 4,070 | 3.2x (3.09 to 3.33) | 2.74x (2.69 to 2.8) | 2.63x | 2.48x |  |
| [Kansas City, MO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/kansas_city) | 6,177 | 2.74x (2.63 to 2.85) | 3.94x (3.84 to 4.05) | 1.53x | 3.53x | ethnicity unknown 23% |
| [Lexington, KY](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/lexington) | 2,177 | 1.9x (1.74 to 2.08) | 3.52x (3.32 to 3.73) | 1.55x | 2.88x | 34 Asian victims |
| [Lubbock, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/lubbock) | 6,391 | 1.67x (1.6 to 1.75) | 4.56x (4.35 to 4.79) | 1.36x | 3.72x |  |
| [Memphis, TN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/memphis) | 6,371 | 2.41x (2.32 to 2.49) | 3.8x (3.69 to 3.92) | 2.34x | 3.7x |  |
| [Milwaukee, WI](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/milwaukee) | 4,435 | 3.11x (3.0 to 3.22) | 5.51x (5.3 to 5.73) | 2.85x | 5.07x |  |
| [Minneapolis, MN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/minneapolis) | 5,516 | 2.54x (2.42 to 2.68) | 7.7x (7.41 to 8.02) | 1.38x | 6.51x | ethnicity unknown 38%; race unknown 10% |
| [Nashville, TN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/nashville) | 5,374 | 2.11x (2.04 to 2.18) | 3.46x (3.38 to 3.54) | 1.9x | 3.12x |  |
| [Newark, NJ](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/newark) | 2,243 | 1.63x (1.57 to 1.71) | 2.9x (2.62 to 3.21) | 1.49x | 2.65x | race unknown 9%; 32 Asian victims |
| [Oklahoma City, OK](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/oklahoma_city) | 4,089 | n/a | at least 2.46x (2.4 to 2.54) | n/a | 1.93x | no ethnicity data |
| [Philadelphia, PA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/philadelphia) | 2,738 | 1.85x (1.81 to 1.9) | 3.36x (3.28 to 3.44) | 1.5x | 3.08x | ethnicity unknown 14% |
| [Plano, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/plano) | 2,385 | 2.49x (2.29 to 2.71) | 4.71x (4.36 to 5.08) | 2.12x | 4.02x |  |
| [Portland, OR](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/portland) | 5,457 | 3.98x (3.77 to 4.2) | 4.83x (4.66 to 5.02) | 2.76x | 3.35x | ethnicity coded only as Hispanic |
| [Raleigh, NC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/raleigh) | 3,364 | 1.7x (1.62 to 1.77) | 5.28x (5.07 to 5.5) | 1.53x | 4.74x | ethnicity coded only as Hispanic |
| [San Antonio, TX](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/san_antonio) | 3,872 | 1.84x (1.8 to 1.89) | 2.22x (2.16 to 2.28) | 1.43x | 1.73x |  |
| [San Diego, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/san_diego) | 2,837 | 2.74x (2.64 to 2.84) | 4.39x (4.22 to 4.56) | 2.02x | 3.24x |  |
| [Seattle, WA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/seattle) | 3,893 | 3.67x (3.45 to 3.91) | 6.12x (5.87 to 6.39) | 1.23x | 4.57x | ethnicity unknown 50%; race unknown 23% |
| [St. Louis, MO](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/st_louis) | 3,676 | 2.47x (2.24 to 2.73) | 3.58x (3.43 to 3.74) | 1.21x | 3.37x | ethnicity unknown 14%; few Hispanic residents |
| [St. Paul, MN](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/st_paul) | 4,227 | 3.58x (3.3 to 3.89) | 5.91x (5.62 to 6.23) | 1.95x | 4.68x | ethnicity unknown 25%; race unknown 11% |
| [Stockton, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/stockton) | 4,921 | 2.62x (2.52 to 2.73) | 1.81x (1.72 to 1.9) | 2.04x | 1.41x |  |
| [Toledo, OH](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/toledo) | 9,398 | n/a | at least 2.68x (2.61 to 2.74) | n/a | 2.29x | no ethnicity data |
| [Tulsa, OK](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/tulsa) | 6,108 | n/a | at least 2.21x (2.14 to 2.27) | n/a | 1.74x | no ethnicity data; offense coding changed |
| [Winston-Salem, NC](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/winston_salem) | 5,672 | 2.63x (2.51 to 2.76) | 2.85x (2.75 to 2.95) | 2.17x | 2.57x |  |

2024 to 2025 only:

| City | Black women per 100,000 | vs Hispanic (95% interval) | vs White (95% interval) | Lowest bound vs Hispanic | Lowest bound vs White | Flags |
|---|---|---|---|---|---|---|
| [Bakersfield, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/bakersfield) | 4,005 | 3.25x (3.02 to 3.48) | 3.31x (3.06 to 3.59) | 2.53x | 2.57x |  |
| [Baltimore, MD](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/baltimore) | 3,450 | 1.48x (1.39 to 1.58) | 2.63x (2.51 to 2.76) | 0.87x | 2.5x | ethnicity unknown 32%; race unknown 6% |
| [Boston, MA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/boston) | 3,124 | 1.83x (1.74 to 1.92) | 4.72x (4.48 to 4.98) | 1.34x | 3.46x | ethnicity unknown 37%; race unknown 18% |
| [Jersey City, NJ](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/jersey_city) | 2,477 | 1.64x (1.51 to 1.77) | 2.77x (2.52 to 3.05) | 1.42x | 2.39x |  |
| [Long Beach, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/long_beach) | 3,326 | 2.57x (2.42 to 2.73) | 2.96x (2.76 to 3.18) | 2.09x | 2.41x | ethnicity unknown 20% |
| [Louisville, KY](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/louisville) | 4,242 | 2.83x (2.64 to 3.04) | 3.41x (3.28 to 3.54) | 2.12x | 2.97x | department 1.09x city |
| [New York, NY](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/new_york) | 2,216 | 1.41x (1.39 to 1.42) | 4.92x (4.83 to 5.03) | 1.17x | 4.09x | race unknown 11% |
| [North Las Vegas, NV](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/north_las_vegas) | 2,737 | 2.94x (2.72 to 3.17) | 2.58x (2.36 to 2.83) | 2.5x | 2.2x | 49 Asian victims; department 1.09x city |
| [Omaha, NE](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/omaha) | 5,127 | 3.54x (3.3 to 3.8) | 5.4x (5.13 to 5.69) | 2.18x | 4.18x | ethnicity unknown 19% |
| [Sacramento, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/sacramento) | 5,457 | 3.3x (3.14 to 3.47) | 3.17x (3.01 to 3.33) | 2.42x | 2.33x |  |
| [San Jose, CA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/san_jose) | 2,881 | 1.28x (1.19 to 1.38) | 2.82x (2.6 to 3.06) | 0.88x | 1.95x | race unknown 6% |
| [Tucson, AZ](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/tucson) | 3,171 | 2.49x (2.3 to 2.7) | 2.96x (2.73 to 3.21) | 1.76x | 2.09x | ethnicity unknown 34%; race unknown 15%; 2025 low; 43 Asian victims |
| [Virginia Beach, VA](https://github.com/mngoh/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/tree/main/cities/virginia_beach) | 2,658 | 3.3x (2.94 to 3.71) | 3.1x (2.93 to 3.29) | 1.18x | 2.59x | ethnicity unknown 26% |

Limits:

- **What, not why.** Shows how often assaults are reported, not why. Nothing here measures causes or offenders.
- **Police reports only.** Willingness to report, and where police patrol, differ by group, place and time. This data cannot separate them from differences in assaults.
- **Reports, not people.** Someone assaulted twice counts twice.
- **No neighborhood test.** The FBI files have no victim location, so income and segregation are untested here. Where they were tested before (Los Angeles, Baltimore, Dallas), the gap remained.
- **Levels not comparable across cities.** Departments code offenses differently: intimidation, left out, is 0.1% of assault-type victims in Newark and 51% in New York. Compare ratios within a city, not rates across cities. Columbus changed its coding in November 2024; Tucson's 2025 looks incomplete.
- **Race recorded by officers.** The Census counts Black alone; 3% to 56% more residents are Black alone or in combination, which sets the lowest bound.
- **Ethnicity.** Five cities record none (Toledo, Cleveland, Tulsa, Detroit and Oklahoma City): no Hispanic comparison, and the ratio to White women is a floor. Three code only Hispanic (Portland, Raleigh and Columbus).
- **Unknown race.** Up to 23% of women victims (Seattle). If every one were in the comparison group, the gap with Hispanic women would vanish in Seattle and Boston; the gap with White women stays above 2x.
- **Intervals show counting noise only.** They leave out repeat victimization, coding error and the bounds above.
- **Where people live.** Rates divide by residents, not where people spend time. A department serving more people than its city (Charlotte, 1.15x) runs high.
- **Small numbers.** Asian women's counts are small, so their ratios stay out of the headline; fewer than 10,000 Hispanic women live in Cincinnati, St. Louis and Chesapeake.
- **Choices made after seeing the data.** The screen's thresholds, the typical-city medians and keeping Columbus and Tucson. All are disclosed; none were set in advance.
- **One department each.** Transit, school, campus and county police are not counted.
- **Not national.** Large cities with complete data, not a national sample.
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
