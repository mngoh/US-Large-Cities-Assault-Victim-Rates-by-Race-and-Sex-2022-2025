# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/north_las_vegas.csv

31,004 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 23,384 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 7.3% | 24 |
| offense_id | 0.0% | 0.0% | 28,849 |
| offense_code | 0.0% | 0.0% | 44 |
| offense_name | 0.0% | 0.0% | 44 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 42 |
| victim_id | 0.0% | 0.0% | 27,182 |
| victim_seq_num | 0.0% | 0.0% | 14 |
| victim_type | 0.0% | 0.1% | 9 |
| age_code | 0.0% | 0.0% | 102 |
| age_num | 0.0% | 0.0% | 102 |
| sex | 0.0% | 33.6% | 4 |
| race | 0.0% | 0.9% | 7 |
| ethnicity | 0.0% | 35.6% | 4 |
| resident_status | 33.2% | 3.4% | 3 |
| relationship | 53.9% | 0.0% | 117 |
| weapon | 73.9% | 0.4% | 48 |
| injury | 85.5% | 0.0% | 33 |

## Duplicates

3,822 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 5,300 |
| 290 | Destruction/Damage/Vandalism of Property | 4,570 |
| 240 | Motor Vehicle Theft | 3,701 |
| 23C | Shoplifting | 2,367 |
| 35B | Drug Equipment Violations | 2,328 |
| 220 | Burglary/Breaking & Entering | 1,594 |
| 23H | All Other Larceny | 1,553 |
| 35A | Drug/Narcotic Violations | 1,472 |
| 13A | Aggravated Assault | 1,398 |
| 23F | Theft From Motor Vehicle | 1,349 |
| 520 | Weapon Law Violations | 907 |
| 120 | Robbery | 876 |
| 280 | Stolen Property Offenses | 551 |
| 13C | Intimidation | 490 |
| 26A | False Pretenses/Swindle/Confidence Game | 463 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 411 |
| 23D | Theft From Building | 405 |
| 26B | Credit Card/Automated Teller Machine Fraud | 231 |
| 11D | Criminal Sexual Contact | 159 |
| 11A | Rape | 149 |
| 270 | Embezzlement | 127 |
| 250 | Counterfeiting/Forgery | 108 |
| 100 | Kidnapping/Abduction | 76 |
| 200 | Arson | 70 |
| 26F | Identity Theft | 58 |
| 09A | Murder and Nonnegligent Manslaughter | 57 |
| 210 | Extortion/Blackmail | 44 |
| 26C | Impersonation | 33 |
| 720 | Animal Cruelty | 20 |
| 11B | Sodomy | 20 |
| 23B | Purse-snatching | 20 |
| 64A | Human Trafficking, Commercial Sex Acts | 19 |
| 23A | Pocket-picking | 18 |
| 370 | Pornography/Obscene Material | 18 |
| 26E | Wire Fraud | 10 |
| 26G | Hacking/Computer Invasion | 8 |
| 36B | Statutory Rape | 7 |
| 11C | Sexual Assault With An Object | 6 |
| 36A | Incest | 3 |
| 23E | Theft From Coin-Operated Machine or Device | 3 |
| 40C | Purchasing Prostitution | 2 |
| 40B | Assisting or Promoting Prostitution | 1 |
| 510 | Bribery | 1 |
| 64B | Human Trafficking, Involuntary Servitude | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 1,293 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:1328 2024-02:1390 2024-03:1542 2024-04:1553 2024-05:1539 2024-06:1449 2024-07:1421 2024-08:1328 2024-09:1267 2024-10:1150 2024-11:1177 2024-12:1170 2025-01:1071 2025-02:983 2025-03:1166 2025-04:1301 2025-05:1312 2025-06:1112 2025-07:1319 2025-08:1279 2025-09:1352 2025-10:1285 2025-11:1270 2025-12:1240

Use only full calendar years where you can; weight any partial year by its share of the year.