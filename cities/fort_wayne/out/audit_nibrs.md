# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/fort_wayne.csv

58,254 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 50,713 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 10.1% | 24 |
| offense_id | 0.0% | 0.0% | 54,692 |
| offense_code | 0.0% | 0.0% | 46 |
| offense_name | 0.0% | 0.0% | 47 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 55,244 |
| victim_seq_num | 0.0% | 0.0% | 15 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 101 |
| age_num | 0.0% | 0.0% | 101 |
| sex | 0.0% | 29.4% | 4 |
| race | 0.0% | 4.3% | 7 |
| ethnicity | 0.0% | 58.1% | 4 |
| resident_status | 72.7% | 0.4% | 3 |
| relationship | 66.5% | 0.0% | 118 |
| weapon | 72.3% | 0.3% | 36 |
| injury | 82.9% | 0.0% | 29 |

## Duplicates

3,010 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 11,437 |
| 23C | Shoplifting | 6,010 |
| 23H | All Other Larceny | 5,887 |
| 35A | Drug/Narcotic Violations | 3,924 |
| 13C | Intimidation | 3,831 |
| 23F | Theft From Motor Vehicle | 3,760 |
| 240 | Motor Vehicle Theft | 2,714 |
| 220 | Burglary/Breaking & Entering | 2,647 |
| 23D | Theft From Building | 2,421 |
| 26A | False Pretenses/Swindle/Confidence Game | 2,075 |
| 35B | Drug Equipment Violations | 1,824 |
| 13A | Aggravated Assault | 1,814 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,656 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,591 |
| 26F | Identity Theft | 1,373 |
| 520 | Weapon Law Violations | 1,002 |
| 120 | Robbery | 897 |
| 720 | Animal Cruelty | 768 |
| 11A | Rape | 431 |
| 11D | Criminal Sexual Contact | 358 |
| 100 | Kidnapping/Abduction | 284 |
| 270 | Embezzlement | 250 |
| 290 | Destruction/Damage/Vandalism of Property | 223 |
| 200 | Arson | 204 |
| 370 | Pornography/Obscene Material | 191 |
| 250 | Counterfeiting/Forgery | 144 |
| 09A | Murder and Nonnegligent Manslaughter | 108 |
| 11D | Fondling | 97 |
| 210 | Extortion/Blackmail | 92 |
| 11B | Sodomy | 49 |
| 36B | Statutory Rape | 46 |
| 40A | Prostitution | 37 |
| 23A | Pocket-picking | 26 |
| 23E | Theft From Coin-Operated Machine or Device | 15 |
| 26E | Wire Fraud | 11 |
| 11C | Sexual Assault With An Object | 10 |
| 26C | Impersonation | 8 |
| 23B | Purse-snatching | 7 |
| 36A | Incest | 6 |
| 26G | Hacking/Computer Invasion | 6 |
| 26D | Welfare Fraud | 5 |
| 64A | Human Trafficking, Commercial Sex Acts | 5 |
| 40B | Assisting or Promoting Prostitution | 3 |
| 39C | Gambling Equipment Violation | 2 |
| 09B | Negligent Manslaughter | 2 |
| 64B | Human Trafficking, Involuntary Servitude | 2 |
| 40C | Purchasing Prostitution | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 1,194 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1103 2022-02:999 2022-03:1164 2022-04:1149 2022-05:1275 2022-06:1358 2022-07:1401 2022-08:1355 2022-09:1368 2022-10:1368 2022-11:1294 2022-12:1130 2023-01:1120 2023-02:1128 2023-03:1118 2023-04:1151 2023-05:1368 2023-06:1196 2023-07:1520 2023-08:1456 2023-09:1279 2023-10:1333 2023-11:1123 2023-12:1202 2024-01:1032 2024-02:1134 2024-03:1076 2024-04:1336 2024-05:1347 2024-06:1327 2024-07:1456 2024-08:1308 2024-09:1293 2024-10:1214 2024-11:1087 2024-12:1119 2025-01:1163 2025-02:869 2025-03:1193 2025-04:1156 2025-05:1338 2025-06:1126 2025-07:1267 2025-08:1351 2025-09:1182 2025-10:1142 2025-11:908 2025-12:872

Use only full calendar years where you can; weight any partial year by its share of the year.