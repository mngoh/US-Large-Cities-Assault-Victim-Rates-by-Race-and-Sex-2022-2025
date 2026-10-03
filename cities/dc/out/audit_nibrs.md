# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/dc.csv

308,795 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 241,242 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 7.7% | 24 |
| offense_id | 0.0% | 0.0% | 282,022 |
| offense_code | 0.0% | 0.0% | 45 |
| offense_name | 0.0% | 0.0% | 46 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 279,088 |
| victim_seq_num | 0.0% | 0.0% | 49 |
| victim_type | 0.0% | 1.3% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 21.5% | 4 |
| race | 0.0% | 13.6% | 7 |
| ethnicity | 0.0% | 52.8% | 4 |
| resident_status | 54.8% | 2.3% | 3 |
| relationship | 58.4% | 0.0% | 242 |
| weapon | 71.7% | 0.5% | 112 |
| injury | 86.5% | 0.0% | 53 |

## Duplicates

29,707 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 62,094 |
| 13B | Simple Assault | 48,022 |
| 23F | Theft From Motor Vehicle | 29,167 |
| 240 | Motor Vehicle Theft | 21,235 |
| 23H | All Other Larceny | 19,464 |
| 13C | Intimidation | 19,223 |
| 23C | Shoplifting | 15,692 |
| 520 | Weapon Law Violations | 15,048 |
| 120 | Robbery | 14,435 |
| 13A | Aggravated Assault | 11,137 |
| 23D | Theft From Building | 9,984 |
| 35A | Drug/Narcotic Violations | 8,915 |
| 220 | Burglary/Breaking & Entering | 7,203 |
| 26B | Credit Card/Automated Teller Machine Fraud | 4,593 |
| 26F | Identity Theft | 4,496 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 3,856 |
| 26A | False Pretenses/Swindle/Confidence Game | 3,479 |
| 250 | Counterfeiting/Forgery | 2,170 |
| 280 | Stolen Property Offenses | 2,117 |
| 11D | Criminal Sexual Contact | 958 |
| 26E | Wire Fraud | 857 |
| 11A | Rape | 783 |
| 09A | Murder and Nonnegligent Manslaughter | 755 |
| 210 | Extortion/Blackmail | 423 |
| 26D | Welfare Fraud | 420 |
| 11D | Fondling | 357 |
| 26G | Hacking/Computer Invasion | 334 |
| 35B | Drug Equipment Violations | 311 |
| 370 | Pornography/Obscene Material | 289 |
| 100 | Kidnapping/Abduction | 191 |
| 26C | Impersonation | 143 |
| 270 | Embezzlement | 134 |
| 23A | Pocket-picking | 116 |
| 23B | Purse-snatching | 93 |
| 11B | Sodomy | 79 |
| 11C | Sexual Assault With An Object | 76 |
| 40C | Purchasing Prostitution | 42 |
| 39A | Betting/Wagering | 31 |
| 23E | Theft From Coin-Operated Machine or Device | 27 |
| 720 | Animal Cruelty | 21 |
| 40A | Prostitution | 9 |
| 510 | Bribery | 5 |
| 36B | Statutory Rape | 4 |
| 200 | Arson | 3 |
| 40B | Assisting or Promoting Prostitution | 2 |
| 09B | Negligent Manslaughter | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 6,420 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:5792 2022-02:5332 2022-03:5924 2022-04:5816 2022-05:6291 2022-06:6237 2022-07:6439 2022-08:6318 2022-09:6111 2022-10:6462 2022-11:6105 2022-12:6259 2023-01:7132 2023-02:6451 2023-03:6815 2023-04:6585 2023-05:7774 2023-06:8027 2023-07:7649 2023-08:8371 2023-09:6959 2023-10:7624 2023-11:6887 2023-12:6455 2024-01:6176 2024-02:5992 2024-03:5974 2024-04:5983 2024-05:6875 2024-06:6859 2024-07:6793 2024-08:6691 2024-09:7067 2024-10:7181 2024-11:6635 2024-12:6455 2025-01:5687 2025-02:5180 2025-03:6392 2025-04:6303 2025-05:6728 2025-06:6402 2025-07:6576 2025-08:6005 2025-09:5561 2025-10:5445 2025-11:5173 2025-12:4847

Use only full calendar years where you can; weight any partial year by its share of the year.