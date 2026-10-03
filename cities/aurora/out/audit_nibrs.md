# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/aurora.csv

133,566 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 107,981 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 5.2% | 24 |
| offense_id | 0.0% | 0.0% | 119,352 |
| offense_code | 0.0% | 0.0% | 47 |
| offense_name | 0.0% | 0.0% | 48 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 125,291 |
| victim_seq_num | 0.0% | 0.0% | 74 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 23.5% | 4 |
| race | 0.0% | 8.3% | 7 |
| ethnicity | 0.0% | 34.2% | 4 |
| resident_status | 24.0% | 1.7% | 3 |
| relationship | 59.4% | 0.0% | 284 |
| weapon | 71.2% | 0.2% | 54 |
| injury | 87.6% | 0.0% | 53 |

## Duplicates

8,275 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 240 | Motor Vehicle Theft | 18,805 |
| 13B | Simple Assault | 17,382 |
| 290 | Destruction/Damage/Vandalism of Property | 16,163 |
| 13A | Aggravated Assault | 11,374 |
| 23C | Shoplifting | 7,610 |
| 23F | Theft From Motor Vehicle | 7,363 |
| 220 | Burglary/Breaking & Entering | 7,349 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 7,251 |
| 23H | All Other Larceny | 6,170 |
| 26A | False Pretenses/Swindle/Confidence Game | 4,237 |
| 23D | Theft From Building | 4,148 |
| 120 | Robbery | 3,489 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,940 |
| 520 | Weapon Law Violations | 2,885 |
| 35A | Drug/Narcotic Violations | 2,655 |
| 26F | Identity Theft | 2,363 |
| 35B | Drug Equipment Violations | 1,964 |
| 280 | Stolen Property Offenses | 1,100 |
| 11A | Rape | 905 |
| 250 | Counterfeiting/Forgery | 879 |
| 100 | Kidnapping/Abduction | 769 |
| 13C | Intimidation | 737 |
| 370 | Pornography/Obscene Material | 730 |
| 26E | Wire Fraud | 631 |
| 11D | Criminal Sexual Contact | 604 |
| 200 | Arson | 533 |
| 210 | Extortion/Blackmail | 494 |
| 270 | Embezzlement | 355 |
| 11D | Fondling | 269 |
| 11B | Sodomy | 236 |
| 26C | Impersonation | 176 |
| 09A | Murder and Nonnegligent Manslaughter | 172 |
| 11C | Sexual Assault With An Object | 121 |
| 40A | Prostitution | 117 |
| 26G | Hacking/Computer Invasion | 116 |
| 720 | Animal Cruelty | 108 |
| 23A | Pocket-picking | 68 |
| 23E | Theft From Coin-Operated Machine or Device | 63 |
| 23B | Purse-snatching | 61 |
| 36B | Statutory Rape | 40 |
| 64A | Human Trafficking, Commercial Sex Acts | 40 |
| 26D | Welfare Fraud | 23 |
| 09B | Negligent Manslaughter | 18 |
| 40B | Assisting or Promoting Prostitution | 17 |
| 09C | Justifiable Homicide | 17 |
| 36A | Incest | 10 |
| 64B | Human Trafficking, Involuntary Servitude | 8 |
| 510 | Bribery | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,780 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:3326 2022-02:3159 2022-03:3580 2022-04:3366 2022-05:3512 2022-06:3194 2022-07:3584 2022-08:3110 2022-09:3053 2022-10:2918 2022-11:2865 2022-12:2774 2023-01:3119 2023-02:2849 2023-03:3224 2023-04:2960 2023-05:2999 2023-06:3024 2023-07:2858 2023-08:2964 2023-09:2817 2023-10:2805 2023-11:2764 2023-12:2933 2024-01:2785 2024-02:2512 2024-03:2598 2024-04:2595 2024-05:2468 2024-06:2776 2024-07:2606 2024-08:2828 2024-09:2766 2024-10:2593 2024-11:2407 2024-12:2619 2025-01:2436 2025-02:2289 2025-03:2400 2025-04:2315 2025-05:2336 2025-06:2173 2025-07:2492 2025-08:2477 2025-09:2292 2025-10:2431 2025-11:2322 2025-12:2293

Use only full calendar years where you can; weight any partial year by its share of the year.