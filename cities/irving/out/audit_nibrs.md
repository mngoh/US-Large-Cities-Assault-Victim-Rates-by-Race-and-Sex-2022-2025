# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/irving.csv

68,400 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 51,272 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 9.5% | 4.6% | 24 |
| offense_id | 0.0% | 0.0% | 63,277 |
| offense_code | 0.0% | 0.0% | 47 |
| offense_name | 0.0% | 0.0% | 48 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 58,151 |
| victim_seq_num | 0.0% | 0.0% | 48 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 101 |
| age_num | 0.0% | 0.0% | 101 |
| sex | 0.0% | 36.8% | 4 |
| race | 0.0% | 0.8% | 7 |
| ethnicity | 0.0% | 39.0% | 4 |
| resident_status | 36.7% | 1.8% | 3 |
| relationship | 36.7% | 0.0% | 139 |
| weapon | 78.7% | 0.3% | 56 |
| injury | 89.9% | 0.0% | 32 |

## Duplicates

10,249 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 9,739 |
| 13B | Simple Assault | 9,207 |
| 35A | Drug/Narcotic Violations | 6,635 |
| 23F | Theft From Motor Vehicle | 4,804 |
| 35B | Drug Equipment Violations | 4,729 |
| 23H | All Other Larceny | 4,236 |
| 23C | Shoplifting | 4,157 |
| 240 | Motor Vehicle Theft | 3,871 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 3,052 |
| 220 | Burglary/Breaking & Entering | 2,961 |
| 13C | Intimidation | 2,345 |
| 26F | Identity Theft | 1,982 |
| 13A | Aggravated Assault | 1,851 |
| 520 | Weapon Law Violations | 1,500 |
| 23D | Theft From Building | 1,215 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,064 |
| 120 | Robbery | 858 |
| 26C | Impersonation | 689 |
| 26A | False Pretenses/Swindle/Confidence Game | 670 |
| 250 | Counterfeiting/Forgery | 655 |
| 11A | Rape | 369 |
| 11D | Criminal Sexual Contact | 217 |
| 370 | Pornography/Obscene Material | 209 |
| 100 | Kidnapping/Abduction | 204 |
| 23B | Purse-snatching | 126 |
| 11B | Sodomy | 125 |
| 26E | Wire Fraud | 110 |
| 40C | Purchasing Prostitution | 101 |
| 11D | Fondling | 95 |
| 11C | Sexual Assault With An Object | 89 |
| 270 | Embezzlement | 79 |
| 26G | Hacking/Computer Invasion | 65 |
| 280 | Stolen Property Offenses | 57 |
| 23A | Pocket-picking | 56 |
| 40A | Prostitution | 51 |
| 23E | Theft From Coin-Operated Machine or Device | 50 |
| 09A | Murder and Nonnegligent Manslaughter | 47 |
| 720 | Animal Cruelty | 36 |
| 200 | Arson | 32 |
| 64A | Human Trafficking, Commercial Sex Acts | 27 |
| 09B | Negligent Manslaughter | 8 |
| 40B | Assisting or Promoting Prostitution | 7 |
| 26D | Welfare Fraud | 6 |
| 64B | Human Trafficking, Involuntary Servitude | 6 |
| 210 | Extortion/Blackmail | 5 |
| 36A | Incest | 1 |
| 39A | Betting/Wagering | 1 |
| 510 | Bribery | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 1,412 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1560 2022-02:1365 2022-03:1751 2022-04:1559 2022-05:1750 2022-06:1663 2022-07:1717 2022-08:1865 2022-09:1688 2022-10:1479 2022-11:1396 2022-12:1616 2023-01:1617 2023-02:1404 2023-03:1515 2023-04:1469 2023-05:1648 2023-06:1443 2023-07:1534 2023-08:1577 2023-09:1609 2023-10:1561 2023-11:1473 2023-12:1325 2024-01:1326 2024-02:1341 2024-03:1527 2024-04:1404 2024-05:1358 2024-06:1323 2024-07:1412 2024-08:1443 2024-09:1464 2024-10:1413 2024-11:1322 2024-12:1240 2025-01:1269 2025-02:1232 2025-03:1252 2025-04:1187 2025-05:1239 2025-06:1135 2025-07:1167 2025-08:1275 2025-09:1195 2025-10:1205 2025-11:1066 2025-12:1021

Use only full calendar years where you can; weight any partial year by its share of the year.