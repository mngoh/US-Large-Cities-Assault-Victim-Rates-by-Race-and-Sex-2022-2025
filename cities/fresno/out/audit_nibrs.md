# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/fresno.csv

183,009 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 148,495 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 5.3% | 24 |
| offense_id | 0.0% | 0.0% | 169,670 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 167,877 |
| victim_seq_num | 0.0% | 0.0% | 35 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 26.4% | 4 |
| race | 0.0% | 6.8% | 7 |
| ethnicity | 0.0% | 42.1% | 4 |
| resident_status | 67.8% | 1.6% | 3 |
| relationship | 68.7% | 0.0% | 258 |
| weapon | 80.1% | 0.4% | 135 |
| injury | 87.7% | 0.0% | 74 |

## Duplicates

15,132 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 25,805 |
| 13B | Simple Assault | 24,726 |
| 23F | Theft From Motor Vehicle | 16,417 |
| 240 | Motor Vehicle Theft | 13,013 |
| 220 | Burglary/Breaking & Entering | 12,334 |
| 23H | All Other Larceny | 12,080 |
| 13A | Aggravated Assault | 12,009 |
| 23C | Shoplifting | 11,401 |
| 520 | Weapon Law Violations | 7,208 |
| 13C | Intimidation | 4,821 |
| 120 | Robbery | 4,696 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 4,602 |
| 26B | Credit Card/Automated Teller Machine Fraud | 4,382 |
| 26A | False Pretenses/Swindle/Confidence Game | 4,016 |
| 23D | Theft From Building | 3,348 |
| 26F | Identity Theft | 3,306 |
| 35A | Drug/Narcotic Violations | 3,298 |
| 35B | Drug Equipment Violations | 3,094 |
| 100 | Kidnapping/Abduction | 2,351 |
| 26C | Impersonation | 1,847 |
| 280 | Stolen Property Offenses | 1,749 |
| 250 | Counterfeiting/Forgery | 1,357 |
| 11D | Criminal Sexual Contact | 725 |
| 200 | Arson | 713 |
| 11A | Rape | 661 |
| 270 | Embezzlement | 374 |
| 210 | Extortion/Blackmail | 302 |
| 11B | Sodomy | 297 |
| 23B | Purse-snatching | 274 |
| 23A | Pocket-picking | 256 |
| 11C | Sexual Assault With An Object | 235 |
| 11D | Fondling | 230 |
| 370 | Pornography/Obscene Material | 215 |
| 40A | Prostitution | 160 |
| 09A | Murder and Nonnegligent Manslaughter | 153 |
| 36B | Statutory Rape | 127 |
| 720 | Animal Cruelty | 114 |
| 40B | Assisting or Promoting Prostitution | 107 |
| 23E | Theft From Coin-Operated Machine or Device | 56 |
| 26G | Hacking/Computer Invasion | 45 |
| 64A | Human Trafficking, Commercial Sex Acts | 39 |
| 40C | Purchasing Prostitution | 21 |
| 64B | Human Trafficking, Involuntary Servitude | 11 |
| 26D | Welfare Fraud | 8 |
| 09B | Negligent Manslaughter | 8 |
| 39C | Gambling Equipment Violation | 7 |
| 39A | Betting/Wagering | 5 |
| 39B | Operating/Promoting/Assisting Gambling | 4 |
| 36A | Incest | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 3,897 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:3816 2022-02:3613 2022-03:3938 2022-04:3911 2022-05:3911 2022-06:3972 2022-07:4143 2022-08:3982 2022-09:4056 2022-10:4438 2022-11:3931 2022-12:4089 2023-01:4039 2023-02:3534 2023-03:3902 2023-04:3846 2023-05:4365 2023-06:3913 2023-07:3892 2023-08:3991 2023-09:3835 2023-10:3523 2023-11:3702 2023-12:3722 2024-01:4071 2024-02:3884 2024-03:4193 2024-04:4009 2024-05:4237 2024-06:4113 2024-07:4440 2024-08:4054 2024-09:4052 2024-10:3988 2024-11:3586 2024-12:3527 2025-01:3848 2025-02:3185 2025-03:3313 2025-04:3374 2025-05:3535 2025-06:3452 2025-07:3468 2025-08:3672 2025-09:3433 2025-10:3488 2025-11:3024 2025-12:2999

Use only full calendar years where you can; weight any partial year by its share of the year.