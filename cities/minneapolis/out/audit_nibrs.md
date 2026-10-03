# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/minneapolis.csv

189,352 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 165,672 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 8.2% | 24 |
| offense_id | 0.0% | 0.0% | 175,517 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 46 |
| victim_id | 0.0% | 0.0% | 183,451 |
| victim_seq_num | 0.0% | 0.0% | 37 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 16.4% | 4 |
| race | 0.0% | 15.5% | 7 |
| ethnicity | 0.0% | 61.2% | 4 |
| resident_status | 14.7% | 14.3% | 3 |
| relationship | 72.9% | 0.0% | 233 |
| weapon | 76.5% | 0.8% | 100 |
| injury | 87.7% | 0.0% | 79 |

## Duplicates

5,901 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 29,578 |
| 240 | Motor Vehicle Theft | 26,122 |
| 23H | All Other Larceny | 24,192 |
| 13B | Simple Assault | 18,338 |
| 23F | Theft From Motor Vehicle | 16,524 |
| 13A | Aggravated Assault | 11,780 |
| 220 | Burglary/Breaking & Entering | 11,743 |
| 13C | Intimidation | 8,924 |
| 120 | Robbery | 7,241 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 6,839 |
| 520 | Weapon Law Violations | 4,726 |
| 35A | Drug/Narcotic Violations | 3,979 |
| 23C | Shoplifting | 3,196 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,860 |
| 26F | Identity Theft | 2,336 |
| 26A | False Pretenses/Swindle/Confidence Game | 1,618 |
| 280 | Stolen Property Offenses | 1,544 |
| 11A | Rape | 1,231 |
| 11D | Criminal Sexual Contact | 1,173 |
| 100 | Kidnapping/Abduction | 765 |
| 250 | Counterfeiting/Forgery | 758 |
| 200 | Arson | 579 |
| 23D | Theft From Building | 558 |
| 35B | Drug Equipment Violations | 458 |
| 23B | Purse-snatching | 409 |
| 370 | Pornography/Obscene Material | 390 |
| 11D | Fondling | 334 |
| 09A | Murder and Nonnegligent Manslaughter | 290 |
| 26E | Wire Fraud | 171 |
| 11B | Sodomy | 155 |
| 210 | Extortion/Blackmail | 131 |
| 11C | Sexual Assault With An Object | 90 |
| 720 | Animal Cruelty | 88 |
| 270 | Embezzlement | 68 |
| 09B | Negligent Manslaughter | 26 |
| 26G | Hacking/Computer Invasion | 24 |
| 26C | Impersonation | 21 |
| 64A | Human Trafficking, Commercial Sex Acts | 20 |
| 64B | Human Trafficking, Involuntary Servitude | 17 |
| 26D | Welfare Fraud | 9 |
| 23E | Theft From Coin-Operated Machine or Device | 9 |
| 23A | Pocket-picking | 8 |
| 09C | Justifiable Homicide | 8 |
| 39A | Betting/Wagering | 5 |
| 39B | Operating/Promoting/Assisting Gambling | 5 |
| 36B | Statutory Rape | 4 |
| 40A | Prostitution | 4 |
| 40B | Assisting or Promoting Prostitution | 3 |
| 36A | Incest | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 3,954 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:3351 2022-02:3117 2022-03:3425 2022-04:3351 2022-05:4041 2022-06:4623 2022-07:4851 2022-08:4476 2022-09:4242 2022-10:4125 2022-11:3724 2022-12:3306 2023-01:3529 2023-02:3310 2023-03:3884 2023-04:4023 2023-05:4434 2023-06:4068 2023-07:4612 2023-08:4461 2023-09:3905 2023-10:4031 2023-11:3854 2023-12:3904 2024-01:3574 2024-02:3412 2024-03:3472 2024-04:3695 2024-05:4304 2024-06:4257 2024-07:4676 2024-08:4594 2024-09:4512 2024-10:4567 2024-11:3902 2024-12:3403 2025-01:3500 2025-02:2943 2025-03:3347 2025-04:3423 2025-05:4004 2025-06:4079 2025-07:4471 2025-08:4833 2025-09:4196 2025-10:4599 2025-11:3682 2025-12:3260

Use only full calendar years where you can; weight any partial year by its share of the year.