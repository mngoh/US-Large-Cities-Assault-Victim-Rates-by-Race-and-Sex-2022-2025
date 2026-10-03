# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/nashville.csv

309,706 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 241,461 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 6.5% | 24 |
| offense_id | 0.0% | 0.0% | 277,630 |
| offense_code | 0.0% | 0.0% | 51 |
| offense_name | 0.0% | 0.0% | 52 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 290,810 |
| victim_seq_num | 0.0% | 0.0% | 37 |
| victim_type | 0.0% | 0.0% | 7 |
| age_code | 0.0% | 0.0% | 102 |
| age_num | 0.0% | 0.0% | 102 |
| sex | 0.0% | 28.1% | 4 |
| race | 0.0% | 1.6% | 7 |
| ethnicity | 0.0% | 30.5% | 4 |
| resident_status | 27.9% | 2.0% | 3 |
| relationship | 67.0% | 0.0% | 288 |
| weapon | 71.2% | 0.2% | 124 |
| injury | 89.3% | 0.0% | 63 |

## Duplicates

18,896 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 23F | Theft From Motor Vehicle | 43,847 |
| 13B | Simple Assault | 42,914 |
| 290 | Destruction/Damage/Vandalism of Property | 26,688 |
| 13A | Aggravated Assault | 23,717 |
| 23C | Shoplifting | 21,403 |
| 13C | Intimidation | 18,545 |
| 240 | Motor Vehicle Theft | 18,434 |
| 23H | All Other Larceny | 14,721 |
| 220 | Burglary/Breaking & Entering | 14,486 |
| 520 | Weapon Law Violations | 13,225 |
| 23D | Theft From Building | 10,957 |
| 35A | Drug/Narcotic Violations | 9,628 |
| 26A | False Pretenses/Swindle/Confidence Game | 8,035 |
| 26B | Credit Card/Automated Teller Machine Fraud | 7,474 |
| 35B | Drug Equipment Violations | 6,535 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 6,386 |
| 120 | Robbery | 5,590 |
| 26C | Impersonation | 3,143 |
| 23A | Pocket-picking | 1,906 |
| 26E | Wire Fraud | 1,545 |
| 250 | Counterfeiting/Forgery | 1,434 |
| 270 | Embezzlement | 1,371 |
| 11A | Rape | 1,254 |
| 11D | Criminal Sexual Contact | 1,185 |
| 210 | Extortion/Blackmail | 1,150 |
| 100 | Kidnapping/Abduction | 928 |
| 370 | Pornography/Obscene Material | 690 |
| 11B | Sodomy | 513 |
| 11D | Fondling | 357 |
| 09A | Murder and Nonnegligent Manslaughter | 344 |
| 200 | Arson | 320 |
| 11C | Sexual Assault With An Object | 266 |
| 36B | Statutory Rape | 138 |
| 23E | Theft From Coin-Operated Machine or Device | 100 |
| 23B | Purse-snatching | 96 |
| 720 | Animal Cruelty | 95 |
| 64A | Human Trafficking, Commercial Sex Acts | 43 |
| 26G | Hacking/Computer Invasion | 42 |
| 40A | Prostitution | 36 |
| 40C | Purchasing Prostitution | 33 |
| 280 | Stolen Property Offenses | 30 |
| 39C | Gambling Equipment Violation | 29 |
| 09C | Justifiable Homicide | 22 |
| 40B | Assisting or Promoting Prostitution | 13 |
| 39B | Operating/Promoting/Assisting Gambling | 10 |
| 39A | Betting/Wagering | 9 |
| 26D | Welfare Fraud | 7 |
| 64B | Human Trafficking, Involuntary Servitude | 6 |
| 510 | Bribery | 3 |
| 26F | Identity Theft | 1 |
| 36A | Incest | 1 |
| 09B | Negligent Manslaughter | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 6,385 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:6668 2022-02:5866 2022-03:6212 2022-04:6541 2022-05:5707 2022-06:6333 2022-07:6074 2022-08:6070 2022-09:5716 2022-10:5857 2022-11:5086 2022-12:5639 2023-01:6371 2023-02:5885 2023-03:6388 2023-04:5449 2023-05:7281 2023-06:7212 2023-07:7244 2023-08:6916 2023-09:7084 2023-10:6852 2023-11:6363 2023-12:6706 2024-01:6382 2024-02:6449 2024-03:6868 2024-04:6546 2024-05:7256 2024-06:7558 2024-07:7288 2024-08:7462 2024-09:7217 2024-10:7094 2024-11:6373 2024-12:6858 2025-01:7092 2025-02:5680 2025-03:6045 2025-04:6267 2025-05:6620 2025-06:6599 2025-07:6352 2025-08:6052 2025-09:6390 2025-10:6129 2025-11:5772 2025-12:5837

Use only full calendar years where you can; weight any partial year by its share of the year.