# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/baltimore.csv

121,754 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 104,522 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 5.4% | 24 |
| offense_id | 0.0% | 0.0% | 113,688 |
| offense_code | 0.0% | 0.0% | 49 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 114,085 |
| victim_seq_num | 0.0% | 0.0% | 21 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 24.1% | 4 |
| race | 0.0% | 8.4% | 7 |
| ethnicity | 0.0% | 51.5% | 4 |
| resident_status | 62.2% | 1.2% | 3 |
| relationship | 68.7% | 0.0% | 244 |
| weapon | 67.1% | 0.4% | 138 |
| injury | 85.7% | 0.0% | 72 |

## Duplicates

7,669 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 19,135 |
| 290 | Destruction/Damage/Vandalism of Property | 16,644 |
| 240 | Motor Vehicle Theft | 10,538 |
| 13A | Aggravated Assault | 10,262 |
| 23H | All Other Larceny | 8,279 |
| 23F | Theft From Motor Vehicle | 8,047 |
| 23C | Shoplifting | 7,563 |
| 120 | Robbery | 7,356 |
| 220 | Burglary/Breaking & Entering | 6,667 |
| 35A | Drug/Narcotic Violations | 6,446 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 3,781 |
| 23D | Theft From Building | 3,059 |
| 13C | Intimidation | 2,738 |
| 520 | Weapon Law Violations | 2,397 |
| 35B | Drug Equipment Violations | 1,839 |
| 26A | False Pretenses/Swindle/Confidence Game | 1,510 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,005 |
| 26E | Wire Fraud | 535 |
| 26F | Identity Theft | 449 |
| 250 | Counterfeiting/Forgery | 441 |
| 11A | Rape | 427 |
| 11D | Criminal Sexual Contact | 423 |
| 26D | Welfare Fraud | 375 |
| 09A | Murder and Nonnegligent Manslaughter | 331 |
| 200 | Arson | 216 |
| 280 | Stolen Property Offenses | 205 |
| 11B | Sodomy | 156 |
| 720 | Animal Cruelty | 147 |
| 100 | Kidnapping/Abduction | 99 |
| 370 | Pornography/Obscene Material | 98 |
| 23B | Purse-snatching | 87 |
| 270 | Embezzlement | 81 |
| 210 | Extortion/Blackmail | 76 |
| 23A | Pocket-picking | 62 |
| 11C | Sexual Assault With An Object | 58 |
| 40A | Prostitution | 55 |
| 26C | Impersonation | 51 |
| 26G | Hacking/Computer Invasion | 31 |
| 40C | Purchasing Prostitution | 17 |
| 64A | Human Trafficking, Commercial Sex Acts | 17 |
| 36B | Statutory Rape | 13 |
| 09C | Justifiable Homicide | 13 |
| 23E | Theft From Coin-Operated Machine or Device | 10 |
| 39A | Betting/Wagering | 6 |
| 40B | Assisting or Promoting Prostitution | 3 |
| 39C | Gambling Equipment Violation | 2 |
| 09B | Negligent Manslaughter | 2 |
| 39B | Operating/Promoting/Assisting Gambling | 1 |
| 64B | Human Trafficking, Involuntary Servitude | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 5,128 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:5129 2024-02:4987 2024-03:5261 2024-04:5049 2024-05:5201 2024-06:5515 2024-07:5710 2024-08:5547 2024-09:5560 2024-10:5360 2024-11:4847 2024-12:4635 2025-01:4363 2025-02:4205 2025-03:5013 2025-04:4968 2025-05:5193 2025-06:5120 2025-07:5295 2025-08:5178 2025-09:5195 2025-10:5127 2025-11:4705 2025-12:4591

Use only full calendar years where you can; weight any partial year by its share of the year.