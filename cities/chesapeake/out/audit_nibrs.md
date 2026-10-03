# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/chesapeake.csv

64,494 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 48,806 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 8.2% | 24 |
| offense_id | 0.0% | 0.0% | 57,711 |
| offense_code | 0.0% | 0.0% | 51 |
| offense_name | 0.0% | 0.0% | 52 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 57,135 |
| victim_seq_num | 0.0% | 0.0% | 24 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 101 |
| age_num | 0.0% | 0.0% | 101 |
| sex | 0.0% | 29.7% | 4 |
| race | 0.0% | 2.8% | 7 |
| ethnicity | 0.0% | 36.0% | 4 |
| resident_status | 30.8% | 2.1% | 3 |
| relationship | 53.2% | 0.0% | 292 |
| weapon | 71.8% | 0.5% | 59 |
| injury | 90.0% | 0.0% | 33 |

## Duplicates

7,359 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 12,215 |
| 290 | Destruction/Damage/Vandalism of Property | 7,375 |
| 23C | Shoplifting | 5,513 |
| 23F | Theft From Motor Vehicle | 3,457 |
| 13C | Intimidation | 3,323 |
| 13A | Aggravated Assault | 3,065 |
| 35A | Drug/Narcotic Violations | 3,032 |
| 23H | All Other Larceny | 2,640 |
| 26A | False Pretenses/Swindle/Confidence Game | 2,637 |
| 23D | Theft From Building | 2,218 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,061 |
| 35B | Drug Equipment Violations | 2,034 |
| 26E | Wire Fraud | 1,813 |
| 220 | Burglary/Breaking & Entering | 1,802 |
| 520 | Weapon Law Violations | 1,738 |
| 240 | Motor Vehicle Theft | 1,439 |
| 26F | Identity Theft | 1,369 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,164 |
| 250 | Counterfeiting/Forgery | 1,096 |
| 26C | Impersonation | 639 |
| 120 | Robbery | 605 |
| 280 | Stolen Property Offenses | 597 |
| 100 | Kidnapping/Abduction | 346 |
| 210 | Extortion/Blackmail | 331 |
| 270 | Embezzlement | 279 |
| 11D | Criminal Sexual Contact | 279 |
| 370 | Pornography/Obscene Material | 276 |
| 720 | Animal Cruelty | 207 |
| 26G | Hacking/Computer Invasion | 196 |
| 11A | Rape | 194 |
| 11D | Fondling | 104 |
| 26D | Welfare Fraud | 78 |
| 11B | Sodomy | 73 |
| 09A | Murder and Nonnegligent Manslaughter | 57 |
| 200 | Arson | 52 |
| 11C | Sexual Assault With An Object | 41 |
| 23E | Theft From Coin-Operated Machine or Device | 32 |
| 23A | Pocket-picking | 30 |
| 36B | Statutory Rape | 21 |
| 23B | Purse-snatching | 17 |
| 39A | Betting/Wagering | 8 |
| 40C | Purchasing Prostitution | 8 |
| 40A | Prostitution | 7 |
| 64A | Human Trafficking, Commercial Sex Acts | 6 |
| 40B | Assisting or Promoting Prostitution | 6 |
| 510 | Bribery | 4 |
| 36A | Incest | 3 |
| 09C | Justifiable Homicide | 2 |
| 39C | Gambling Equipment Violation | 2 |
| 39B | Operating/Promoting/Assisting Gambling | 1 |
| 64B | Human Trafficking, Involuntary Servitude | 1 |
| 09B | Negligent Manslaughter | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 1,331 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1310 2022-02:1334 2022-03:1502 2022-04:1393 2022-05:1597 2022-06:1533 2022-07:1498 2022-08:1340 2022-09:1364 2022-10:1445 2022-11:1436 2022-12:1601 2023-01:1601 2023-02:1278 2023-03:1267 2023-04:1575 2023-05:1655 2023-06:1445 2023-07:1526 2023-08:1468 2023-09:1328 2023-10:1490 2023-11:1186 2023-12:1318 2024-01:1339 2024-02:1203 2024-03:1267 2024-04:1262 2024-05:1309 2024-06:1493 2024-07:1393 2024-08:1471 2024-09:1347 2024-10:1343 2024-11:1261 2024-12:1215 2025-01:1183 2025-02:1101 2025-03:1232 2025-04:1138 2025-05:1266 2025-06:1186 2025-07:1271 2025-08:1217 2025-09:1225 2025-10:1218 2025-11:1071 2025-12:993

Use only full calendar years where you can; weight any partial year by its share of the year.