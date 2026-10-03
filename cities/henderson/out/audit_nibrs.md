# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/henderson.csv

64,624 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 52,375 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 3.9% | 24 |
| offense_id | 0.0% | 0.0% | 59,994 |
| offense_code | 0.0% | 0.0% | 47 |
| offense_name | 0.0% | 0.0% | 48 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 59,706 |
| victim_seq_num | 0.0% | 0.0% | 29 |
| victim_type | 0.0% | 0.1% | 9 |
| age_code | 0.0% | 0.0% | 102 |
| age_num | 0.0% | 0.0% | 102 |
| sex | 0.0% | 30.1% | 4 |
| race | 0.0% | 1.8% | 7 |
| ethnicity | 0.0% | 34.4% | 4 |
| resident_status | 29.7% | 1.6% | 3 |
| relationship | 33.6% | 0.0% | 193 |
| weapon | 74.5% | 0.2% | 80 |
| injury | 87.9% | 0.0% | 38 |

## Duplicates

4,918 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 12,306 |
| 290 | Destruction/Damage/Vandalism of Property | 5,740 |
| 23C | Shoplifting | 5,192 |
| 240 | Motor Vehicle Theft | 4,939 |
| 23F | Theft From Motor Vehicle | 4,857 |
| 220 | Burglary/Breaking & Entering | 3,885 |
| 23H | All Other Larceny | 3,615 |
| 35B | Drug Equipment Violations | 2,986 |
| 35A | Drug/Narcotic Violations | 2,566 |
| 13A | Aggravated Assault | 2,563 |
| 26A | False Pretenses/Swindle/Confidence Game | 2,087 |
| 23D | Theft From Building | 2,070 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,005 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,331 |
| 26F | Identity Theft | 1,324 |
| 13C | Intimidation | 1,250 |
| 120 | Robbery | 1,138 |
| 280 | Stolen Property Offenses | 1,095 |
| 520 | Weapon Law Violations | 836 |
| 250 | Counterfeiting/Forgery | 515 |
| 270 | Embezzlement | 317 |
| 11A | Rape | 313 |
| 26E | Wire Fraud | 277 |
| 11D | Criminal Sexual Contact | 256 |
| 720 | Animal Cruelty | 205 |
| 200 | Arson | 155 |
| 100 | Kidnapping/Abduction | 98 |
| 370 | Pornography/Obscene Material | 93 |
| 11D | Fondling | 93 |
| 23A | Pocket-picking | 89 |
| 210 | Extortion/Blackmail | 87 |
| 11B | Sodomy | 69 |
| 26G | Hacking/Computer Invasion | 56 |
| 26C | Impersonation | 55 |
| 11C | Sexual Assault With An Object | 40 |
| 09A | Murder and Nonnegligent Manslaughter | 28 |
| 23B | Purse-snatching | 25 |
| 36B | Statutory Rape | 16 |
| 23E | Theft From Coin-Operated Machine or Device | 13 |
| 64A | Human Trafficking, Commercial Sex Acts | 7 |
| 36A | Incest | 6 |
| 09B | Negligent Manslaughter | 6 |
| 40A | Prostitution | 5 |
| 40B | Assisting or Promoting Prostitution | 4 |
| 09C | Justifiable Homicide | 4 |
| 40C | Purchasing Prostitution | 3 |
| 26D | Welfare Fraud | 2 |
| 64B | Human Trafficking, Involuntary Servitude | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 1,371 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1351 2022-02:1149 2022-03:1419 2022-04:1414 2022-05:1391 2022-06:1275 2022-07:1319 2022-08:1327 2022-09:1250 2022-10:1359 2022-11:1140 2022-12:1384 2023-01:1364 2023-02:1171 2023-03:1397 2023-04:1427 2023-05:1560 2023-06:1585 2023-07:1618 2023-08:1538 2023-09:1446 2023-10:1518 2023-11:1393 2023-12:1413 2024-01:1352 2024-02:1383 2024-03:1469 2024-04:1408 2024-05:1435 2024-06:1445 2024-07:1462 2024-08:1378 2024-09:1275 2024-10:1391 2024-11:1182 2024-12:1257 2025-01:1109 2025-02:1202 2025-03:1381 2025-04:1339 2025-05:1422 2025-06:1289 2025-07:1232 2025-08:1229 2025-09:1138 2025-10:1212 2025-11:1148 2025-12:1278

Use only full calendar years where you can; weight any partial year by its share of the year.