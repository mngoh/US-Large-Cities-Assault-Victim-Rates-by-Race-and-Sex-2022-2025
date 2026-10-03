# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/milwaukee.csv

190,488 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 159,134 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 7.8% | 24 |
| offense_id | 0.0% | 0.0% | 175,959 |
| offense_code | 0.0% | 0.0% | 49 |
| offense_name | 0.0% | 0.0% | 50 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 179,869 |
| victim_seq_num | 0.0% | 0.0% | 45 |
| victim_type | 0.0% | 0.2% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 23.0% | 4 |
| race | 0.0% | 1.2% | 7 |
| ethnicity | 0.0% | 28.6% | 4 |
| resident_status | 24.3% | 1.4% | 3 |
| relationship | 60.4% | 0.0% | 160 |
| weapon | 60.6% | 0.7% | 109 |
| injury | 82.7% | 0.0% | 68 |

## Duplicates

10,619 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 240 | Motor Vehicle Theft | 24,566 |
| 13A | Aggravated Assault | 22,835 |
| 290 | Destruction/Damage/Vandalism of Property | 21,967 |
| 520 | Weapon Law Violations | 21,802 |
| 13B | Simple Assault | 21,231 |
| 23F | Theft From Motor Vehicle | 13,446 |
| 13C | Intimidation | 12,544 |
| 220 | Burglary/Breaking & Entering | 10,032 |
| 120 | Robbery | 7,631 |
| 23H | All Other Larceny | 6,276 |
| 23D | Theft From Building | 4,726 |
| 35A | Drug/Narcotic Violations | 4,702 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 4,085 |
| 23C | Shoplifting | 3,132 |
| 280 | Stolen Property Offenses | 2,026 |
| 11A | Rape | 1,200 |
| 26A | False Pretenses/Swindle/Confidence Game | 1,195 |
| 200 | Arson | 1,037 |
| 100 | Kidnapping/Abduction | 888 |
| 26F | Identity Theft | 841 |
| 11D | Criminal Sexual Contact | 684 |
| 09A | Murder and Nonnegligent Manslaughter | 663 |
| 26B | Credit Card/Automated Teller Machine Fraud | 399 |
| 270 | Embezzlement | 307 |
| 250 | Counterfeiting/Forgery | 303 |
| 11B | Sodomy | 286 |
| 11D | Fondling | 265 |
| 35B | Drug Equipment Violations | 242 |
| 370 | Pornography/Obscene Material | 191 |
| 36B | Statutory Rape | 187 |
| 23B | Purse-snatching | 122 |
| 64A | Human Trafficking, Commercial Sex Acts | 91 |
| 23A | Pocket-picking | 90 |
| 09B | Negligent Manslaughter | 89 |
| 210 | Extortion/Blackmail | 82 |
| 11C | Sexual Assault With An Object | 68 |
| 09C | Justifiable Homicide | 60 |
| 23E | Theft From Coin-Operated Machine or Device | 49 |
| 720 | Animal Cruelty | 30 |
| 26E | Wire Fraud | 26 |
| 26C | Impersonation | 25 |
| 40B | Assisting or Promoting Prostitution | 15 |
| 26G | Hacking/Computer Invasion | 13 |
| 40A | Prostitution | 13 |
| 36A | Incest | 6 |
| 510 | Bribery | 5 |
| 64B | Human Trafficking, Involuntary Servitude | 5 |
| 26D | Welfare Fraud | 4 |
| 39A | Betting/Wagering | 3 |
| 39B | Operating/Promoting/Assisting Gambling | 3 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 3,946 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:4612 2022-02:3964 2022-03:4446 2022-04:4439 2022-05:4819 2022-06:4506 2022-07:4880 2022-08:4635 2022-09:4089 2022-10:4401 2022-11:3832 2022-12:3787 2023-01:4087 2023-02:3471 2023-03:3838 2023-04:3989 2023-05:4356 2023-06:4130 2023-07:4252 2023-08:3937 2023-09:3806 2023-10:3955 2023-11:3562 2023-12:3809 2024-01:3649 2024-02:3519 2024-03:3535 2024-04:3693 2024-05:4300 2024-06:4287 2024-07:5062 2024-08:4757 2024-09:3957 2024-10:4353 2024-11:3520 2024-12:3559 2025-01:3450 2025-02:2763 2025-03:3695 2025-04:3886 2025-05:4078 2025-06:3901 2025-07:4040 2025-08:3724 2025-09:3451 2025-10:3692 2025-11:3165 2025-12:2850

Use only full calendar years where you can; weight any partial year by its share of the year.