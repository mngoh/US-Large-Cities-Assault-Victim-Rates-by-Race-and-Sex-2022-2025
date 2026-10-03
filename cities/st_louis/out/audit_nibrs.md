# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/st_louis.csv

178,377 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 126,501 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.4% | 5.7% | 24 |
| offense_id | 0.0% | 0.0% | 160,540 |
| offense_code | 0.0% | 0.0% | 46 |
| offense_name | 0.0% | 0.0% | 47 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 153,690 |
| victim_seq_num | 0.0% | 0.0% | 34 |
| victim_type | 0.0% | 0.3% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 25.7% | 4 |
| race | 0.0% | 2.4% | 7 |
| ethnicity | 0.0% | 40.1% | 4 |
| resident_status | 36.6% | 0.7% | 3 |
| relationship | 77.6% | 0.0% | 296 |
| weapon | 77.4% | 0.3% | 90 |
| injury | 94.2% | 0.0% | 60 |

## Duplicates

24,687 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 39,105 |
| 240 | Motor Vehicle Theft | 21,467 |
| 23F | Theft From Motor Vehicle | 18,791 |
| 520 | Weapon Law Violations | 15,917 |
| 13B | Simple Assault | 11,862 |
| 13A | Aggravated Assault | 11,694 |
| 220 | Burglary/Breaking & Entering | 10,041 |
| 23H | All Other Larceny | 10,011 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 7,388 |
| 23D | Theft From Building | 6,323 |
| 35A | Drug/Narcotic Violations | 4,447 |
| 13C | Intimidation | 3,399 |
| 120 | Robbery | 3,376 |
| 280 | Stolen Property Offenses | 3,117 |
| 23C | Shoplifting | 2,870 |
| 35B | Drug Equipment Violations | 1,390 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,003 |
| 26A | False Pretenses/Swindle/Confidence Game | 851 |
| 250 | Counterfeiting/Forgery | 787 |
| 09A | Murder and Nonnegligent Manslaughter | 649 |
| 100 | Kidnapping/Abduction | 611 |
| 200 | Arson | 533 |
| 26F | Identity Theft | 490 |
| 11A | Rape | 383 |
| 11B | Sodomy | 347 |
| 26E | Wire Fraud | 253 |
| 23A | Pocket-picking | 244 |
| 23B | Purse-snatching | 177 |
| 370 | Pornography/Obscene Material | 167 |
| 11D | Criminal Sexual Contact | 147 |
| 720 | Animal Cruelty | 118 |
| 270 | Embezzlement | 104 |
| 26C | Impersonation | 76 |
| 36B | Statutory Rape | 39 |
| 09C | Justifiable Homicide | 39 |
| 09B | Negligent Manslaughter | 38 |
| 23E | Theft From Coin-Operated Machine or Device | 37 |
| 11D | Fondling | 36 |
| 26G | Hacking/Computer Invasion | 17 |
| 64A | Human Trafficking, Commercial Sex Acts | 10 |
| 40A | Prostitution | 7 |
| 40B | Assisting or Promoting Prostitution | 5 |
| 40C | Purchasing Prostitution | 3 |
| 510 | Bribery | 3 |
| 26D | Welfare Fraud | 2 |
| 39A | Betting/Wagering | 2 |
| 39B | Operating/Promoting/Assisting Gambling | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 3,732 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:3394 2022-02:2906 2022-03:3813 2022-04:3774 2022-05:3674 2022-06:4299 2022-07:5212 2022-08:5017 2022-09:4726 2022-10:4556 2022-11:4015 2022-12:4111 2023-01:4614 2023-02:3905 2023-03:3489 2023-04:3603 2023-05:4030 2023-06:3789 2023-07:4140 2023-08:3812 2023-09:4051 2023-10:4520 2023-11:3906 2023-12:3839 2024-01:3323 2024-02:3056 2024-03:3207 2024-04:3409 2024-05:4108 2024-06:4215 2024-07:4115 2024-08:3660 2024-09:3534 2024-10:3452 2024-11:3442 2024-12:3016 2025-01:2563 2025-02:2587 2025-03:2920 2025-04:3375 2025-05:3783 2025-06:3848 2025-07:3689 2025-08:3503 2025-09:3173 2025-10:3235 2025-11:3003 2025-12:2966

Use only full calendar years where you can; weight any partial year by its share of the year.