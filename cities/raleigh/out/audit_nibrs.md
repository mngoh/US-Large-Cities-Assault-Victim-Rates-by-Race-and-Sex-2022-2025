# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/raleigh.csv

145,646 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 114,506 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 4.4% | 24 |
| offense_id | 0.0% | 0.0% | 129,311 |
| offense_code | 0.0% | 0.0% | 46 |
| offense_name | 0.0% | 0.0% | 47 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 25 |
| victim_id | 0.0% | 0.0% | 132,985 |
| victim_seq_num | 0.0% | 0.0% | 35 |
| victim_type | 0.0% | 0.4% | 8 |
| age_code | 0.0% | 0.0% | 100 |
| age_num | 0.0% | 0.0% | 100 |
| sex | 0.0% | 37.7% | 4 |
| race | 0.0% | 3.8% | 6 |
| ethnicity | 0.0% | 91.0% | 2 |
| resident_status | 37.5% | 0.9% | 3 |
| relationship | 62.8% | 0.0% | 228 |
| weapon | 72.4% | 0.8% | 15 |
| injury | 90.4% | 0.0% | 7 |

## Duplicates

12,661 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 22,576 |
| 23F | Theft From Motor Vehicle | 15,759 |
| 35A | Drug/Narcotic Violations | 14,478 |
| 23C | Shoplifting | 11,378 |
| 23H | All Other Larceny | 8,631 |
| 520 | Weapon Law Violations | 8,376 |
| 35B | Drug Equipment Violations | 7,615 |
| 240 | Motor Vehicle Theft | 7,452 |
| 13A | Aggravated Assault | 6,882 |
| 220 | Burglary/Breaking & Entering | 6,074 |
| 13C | Intimidation | 5,784 |
| 26A | False Pretenses/Swindle/Confidence Game | 4,651 |
| 290 | Destruction/Damage/Vandalism of Property | 4,307 |
| 23D | Theft From Building | 3,676 |
| 26B | Credit Card/Automated Teller Machine Fraud | 3,143 |
| 26C | Impersonation | 2,620 |
| 120 | Robbery | 2,280 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,850 |
| 250 | Counterfeiting/Forgery | 1,537 |
| 280 | Stolen Property Offenses | 1,471 |
| 26E | Wire Fraud | 695 |
| 11D | Criminal Sexual Contact | 628 |
| 11A | Rape | 540 |
| 270 | Embezzlement | 488 |
| 370 | Pornography/Obscene Material | 430 |
| 210 | Extortion/Blackmail | 390 |
| 23A | Pocket-picking | 345 |
| 200 | Arson | 259 |
| 100 | Kidnapping/Abduction | 201 |
| 11D | Fondling | 195 |
| 26D | Welfare Fraud | 188 |
| 23B | Purse-snatching | 139 |
| 11B | Sodomy | 124 |
| 09A | Murder and Nonnegligent Manslaughter | 120 |
| 36B | Statutory Rape | 99 |
| 23E | Theft From Coin-Operated Machine or Device | 75 |
| 720 | Animal Cruelty | 51 |
| 26G | Hacking/Computer Invasion | 30 |
| 11C | Sexual Assault With An Object | 22 |
| 36A | Incest | 20 |
| 40A | Prostitution | 19 |
| 09C | Justifiable Homicide | 12 |
| 39A | Betting/Wagering | 11 |
| 39B | Operating/Promoting/Assisting Gambling | 10 |
| 40B | Assisting or Promoting Prostitution | 8 |
| 09B | Negligent Manslaughter | 5 |
| 39C | Gambling Equipment Violation | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 3,070 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:2726 2022-02:2637 2022-03:3063 2022-04:2924 2022-05:2930 2022-06:2913 2022-07:2749 2022-08:2679 2022-09:2634 2022-10:2803 2022-11:2439 2022-12:2640 2023-01:3067 2023-02:2622 2023-03:2940 2023-04:2944 2023-05:3354 2023-06:3249 2023-07:3453 2023-08:3199 2023-09:3242 2023-10:3360 2023-11:3055 2023-12:3074 2024-01:3117 2024-02:3142 2024-03:3271 2024-04:3051 2024-05:3258 2024-06:3101 2024-07:3445 2024-08:3462 2024-09:3396 2024-10:3386 2024-11:3223 2024-12:3191 2025-01:3194 2025-02:2590 2025-03:3101 2025-04:2915 2025-05:3366 2025-06:3080 2025-07:3137 2025-08:3126 2025-09:2856 2025-10:3048 2025-11:2961 2025-12:2533

Use only full calendar years where you can; weight any partial year by its share of the year.