# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/colorado_springs.csv

156,844 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 113,834 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 8.1% | 24 |
| offense_id | 0.0% | 0.0% | 140,123 |
| offense_code | 0.0% | 0.0% | 46 |
| offense_name | 0.0% | 0.0% | 47 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 132,955 |
| victim_seq_num | 0.0% | 0.0% | 98 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 101 |
| age_num | 0.0% | 0.0% | 101 |
| sex | 0.0% | 27.9% | 4 |
| race | 0.0% | 13.6% | 6 |
| ethnicity | 0.0% | 36.7% | 4 |
| resident_status | 34.5% | 1.7% | 3 |
| relationship | 52.2% | 0.0% | 174 |
| weapon | 80.5% | 0.7% | 52 |
| injury | 89.9% | 0.0% | 64 |

## Duplicates

23,889 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 23,071 |
| 23F | Theft From Motor Vehicle | 16,580 |
| 23H | All Other Larceny | 13,434 |
| 240 | Motor Vehicle Theft | 13,356 |
| 220 | Burglary/Breaking & Entering | 12,798 |
| 23C | Shoplifting | 11,533 |
| 13A | Aggravated Assault | 10,009 |
| 13B | Simple Assault | 9,775 |
| 26F | Identity Theft | 6,277 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 5,940 |
| 35A | Drug/Narcotic Violations | 4,370 |
| 35B | Drug Equipment Violations | 3,372 |
| 26B | Credit Card/Automated Teller Machine Fraud | 3,325 |
| 23D | Theft From Building | 3,297 |
| 520 | Weapon Law Violations | 3,198 |
| 26A | False Pretenses/Swindle/Confidence Game | 2,514 |
| 120 | Robbery | 2,118 |
| 13C | Intimidation | 1,854 |
| 100 | Kidnapping/Abduction | 1,699 |
| 11A | Rape | 1,364 |
| 250 | Counterfeiting/Forgery | 1,285 |
| 200 | Arson | 836 |
| 11D | Criminal Sexual Contact | 828 |
| 210 | Extortion/Blackmail | 551 |
| 26C | Impersonation | 540 |
| 280 | Stolen Property Offenses | 538 |
| 370 | Pornography/Obscene Material | 481 |
| 11C | Sexual Assault With An Object | 348 |
| 23E | Theft From Coin-Operated Machine or Device | 279 |
| 11D | Fondling | 250 |
| 11B | Sodomy | 210 |
| 26G | Hacking/Computer Invasion | 138 |
| 09A | Murder and Nonnegligent Manslaughter | 131 |
| 720 | Animal Cruelty | 93 |
| 40B | Assisting or Promoting Prostitution | 84 |
| 23B | Purse-snatching | 63 |
| 09B | Negligent Manslaughter | 52 |
| 23A | Pocket-picking | 47 |
| 64A | Human Trafficking, Commercial Sex Acts | 46 |
| 40A | Prostitution | 39 |
| 270 | Embezzlement | 33 |
| 36A | Incest | 31 |
| 36B | Statutory Rape | 20 |
| 64B | Human Trafficking, Involuntary Servitude | 11 |
| 39B | Operating/Promoting/Assisting Gambling | 10 |
| 39C | Gambling Equipment Violation | 8 |
| 510 | Bribery | 8 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 3,303 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:3627 2022-02:3399 2022-03:3403 2022-04:3326 2022-05:3244 2022-06:2783 2022-07:3795 2022-08:3607 2022-09:3322 2022-10:3145 2022-11:2859 2022-12:2783 2023-01:3534 2023-02:3051 2023-03:3535 2023-04:3162 2023-05:3778 2023-06:3730 2023-07:3834 2023-08:3801 2023-09:3651 2023-10:3589 2023-11:3527 2023-12:3086 2024-01:3582 2024-02:3358 2024-03:2968 2024-04:3056 2024-05:3500 2024-06:3603 2024-07:3995 2024-08:3685 2024-09:3303 2024-10:3570 2024-11:2695 2024-12:2857 2025-01:3303 2025-02:2772 2025-03:3034 2025-04:3008 2025-05:3179 2025-06:2857 2025-07:2937 2025-08:2844 2025-09:3141 2025-10:2897 2025-11:2506 2025-12:2623

Use only full calendar years where you can; weight any partial year by its share of the year.