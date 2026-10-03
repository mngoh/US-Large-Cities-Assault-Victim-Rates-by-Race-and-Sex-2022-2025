# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/arlington.csv

107,087 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 90,607 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 7.9% | 24 |
| offense_id | 0.0% | 0.0% | 99,398 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 100,810 |
| victim_seq_num | 0.0% | 0.0% | 43 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 29.6% | 4 |
| race | 0.0% | 1.8% | 7 |
| ethnicity | 0.0% | 35.7% | 4 |
| resident_status | 80.4% | 0.3% | 3 |
| relationship | 32.0% | 0.0% | 199 |
| weapon | 71.0% | 0.0% | 67 |
| injury | 85.5% | 0.0% | 52 |

## Duplicates

6,277 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 19,955 |
| 23H | All Other Larceny | 13,547 |
| 35A | Drug/Narcotic Violations | 10,714 |
| 290 | Destruction/Damage/Vandalism of Property | 8,036 |
| 23F | Theft From Motor Vehicle | 7,604 |
| 23C | Shoplifting | 6,095 |
| 13A | Aggravated Assault | 5,642 |
| 240 | Motor Vehicle Theft | 5,548 |
| 13C | Intimidation | 4,787 |
| 220 | Burglary/Breaking & Entering | 4,539 |
| 35B | Drug Equipment Violations | 3,273 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,735 |
| 26F | Identity Theft | 2,438 |
| 520 | Weapon Law Violations | 2,316 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,283 |
| 250 | Counterfeiting/Forgery | 1,267 |
| 120 | Robbery | 1,156 |
| 26A | False Pretenses/Swindle/Confidence Game | 1,151 |
| 11A | Rape | 1,024 |
| 23D | Theft From Building | 702 |
| 11D | Criminal Sexual Contact | 393 |
| 39C | Gambling Equipment Violation | 331 |
| 370 | Pornography/Obscene Material | 322 |
| 11D | Fondling | 172 |
| 11B | Sodomy | 122 |
| 40A | Prostitution | 101 |
| 100 | Kidnapping/Abduction | 75 |
| 39B | Operating/Promoting/Assisting Gambling | 75 |
| 23A | Pocket-picking | 70 |
| 26C | Impersonation | 66 |
| 09A | Murder and Nonnegligent Manslaughter | 63 |
| 64A | Human Trafficking, Commercial Sex Acts | 62 |
| 200 | Arson | 58 |
| 23B | Purse-snatching | 53 |
| 40C | Purchasing Prostitution | 52 |
| 40B | Assisting or Promoting Prostitution | 40 |
| 23E | Theft From Coin-Operated Machine or Device | 38 |
| 39A | Betting/Wagering | 35 |
| 720 | Animal Cruelty | 32 |
| 26E | Wire Fraud | 30 |
| 11C | Sexual Assault With An Object | 24 |
| 280 | Stolen Property Offenses | 11 |
| 09B | Negligent Manslaughter | 11 |
| 64B | Human Trafficking, Involuntary Servitude | 11 |
| 09C | Justifiable Homicide | 9 |
| 26D | Welfare Fraud | 9 |
| 510 | Bribery | 5 |
| 210 | Extortion/Blackmail | 3 |
| 36A | Incest | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,244 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:2385 2022-02:2147 2022-03:2624 2022-04:2459 2022-05:2694 2022-06:2363 2022-07:2608 2022-08:2403 2022-09:2453 2022-10:2248 2022-11:2115 2022-12:2332 2023-01:2260 2023-02:2084 2023-03:2406 2023-04:2313 2023-05:2496 2023-06:2396 2023-07:2339 2023-08:2241 2023-09:2359 2023-10:2426 2023-11:2210 2023-12:2252 2024-01:2105 2024-02:2035 2024-03:2166 2024-04:2259 2024-05:2330 2024-06:2184 2024-07:2262 2024-08:2148 2024-09:2233 2024-10:2441 2024-11:2275 2024-12:2159 2025-01:2099 2025-02:1849 2025-03:2149 2025-04:2028 2025-05:2183 2025-06:1979 2025-07:2028 2025-08:2075 2025-09:2056 2025-10:1882 2025-11:1767 2025-12:1782

Use only full calendar years where you can; weight any partial year by its share of the year.