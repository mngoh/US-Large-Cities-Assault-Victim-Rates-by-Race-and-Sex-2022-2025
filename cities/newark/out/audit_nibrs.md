# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/newark.csv

62,341 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 60,936 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 3.1% | 24 |
| offense_id | 0.0% | 0.0% | 62,113 |
| offense_code | 0.0% | 0.0% | 45 |
| offense_name | 0.0% | 0.0% | 46 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 39 |
| victim_id | 0.0% | 0.0% | 62,112 |
| victim_seq_num | 0.0% | 0.0% | 9 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 99 |
| age_num | 0.0% | 0.0% | 99 |
| sex | 0.0% | 15.5% | 4 |
| race | 0.0% | 8.5% | 7 |
| ethnicity | 0.0% | 27.8% | 4 |
| resident_status | 15.3% | 0.6% | 3 |
| relationship | 65.5% | 0.0% | 33 |
| weapon | 62.3% | 0.1% | 20 |
| injury | 70.6% | 0.0% | 7 |

## Duplicates

229 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 13,177 |
| 240 | Motor Vehicle Theft | 10,761 |
| 290 | Destruction/Damage/Vandalism of Property | 9,261 |
| 23F | Theft From Motor Vehicle | 5,412 |
| 23D | Theft From Building | 5,075 |
| 13A | Aggravated Assault | 4,266 |
| 520 | Weapon Law Violations | 3,246 |
| 35A | Drug/Narcotic Violations | 2,803 |
| 220 | Burglary/Breaking & Entering | 2,018 |
| 120 | Robbery | 1,636 |
| 280 | Stolen Property Offenses | 962 |
| 26F | Identity Theft | 492 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 476 |
| 40A | Prostitution | 387 |
| 11D | Criminal Sexual Contact | 345 |
| 11A | Rape | 314 |
| 23C | Shoplifting | 244 |
| 26B | Credit Card/Automated Teller Machine Fraud | 204 |
| 26A | False Pretenses/Swindle/Confidence Game | 178 |
| 09A | Murder and Nonnegligent Manslaughter | 178 |
| 26E | Wire Fraud | 177 |
| 11D | Fondling | 135 |
| 39B | Operating/Promoting/Assisting Gambling | 84 |
| 11C | Sexual Assault With An Object | 81 |
| 11B | Sodomy | 78 |
| 200 | Arson | 78 |
| 250 | Counterfeiting/Forgery | 71 |
| 35B | Drug Equipment Violations | 39 |
| 720 | Animal Cruelty | 34 |
| 100 | Kidnapping/Abduction | 21 |
| 23B | Purse-snatching | 19 |
| 210 | Extortion/Blackmail | 17 |
| 13C | Intimidation | 16 |
| 36B | Statutory Rape | 14 |
| 23A | Pocket-picking | 9 |
| 370 | Pornography/Obscene Material | 6 |
| 23E | Theft From Coin-Operated Machine or Device | 6 |
| 270 | Embezzlement | 5 |
| 23H | All Other Larceny | 5 |
| 26D | Welfare Fraud | 2 |
| 26C | Impersonation | 2 |
| 39C | Gambling Equipment Violation | 2 |
| 64B | Human Trafficking, Involuntary Servitude | 2 |
| 26G | Hacking/Computer Invasion | 1 |
| 09C | Justifiable Homicide | 1 |
| 64A | Human Trafficking, Commercial Sex Acts | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 1,263 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1188 2022-02:1160 2022-03:1212 2022-04:1202 2022-05:1324 2022-06:1304 2022-07:1427 2022-08:1446 2022-09:1225 2022-10:1274 2022-11:1154 2022-12:988 2023-01:1333 2023-02:1197 2023-03:1336 2023-04:1380 2023-05:1758 2023-06:1584 2023-07:1629 2023-08:1603 2023-09:1352 2023-10:1379 2023-11:1292 2023-12:1428 2024-01:1295 2024-02:1146 2024-03:1201 2024-04:1231 2024-05:1473 2024-06:1426 2024-07:1474 2024-08:1365 2024-09:1393 2024-10:1327 2024-11:1234 2024-12:1251 2025-01:1201 2025-02:1059 2025-03:1186 2025-04:1242 2025-05:1226 2025-06:1222 2025-07:1289 2025-08:1252 2025-09:1220 2025-10:1165 2025-11:1166 2025-12:1122

Use only full calendar years where you can; weight any partial year by its share of the year.