# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/jersey_city.csv

32,896 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 27,412 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 3.4% | 24 |
| offense_id | 0.0% | 0.0% | 31,339 |
| offense_code | 0.0% | 0.0% | 39 |
| offense_name | 0.0% | 0.0% | 39 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 41 |
| victim_id | 0.0% | 0.0% | 30,333 |
| victim_seq_num | 0.0% | 0.0% | 21 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 99 |
| age_num | 0.0% | 0.0% | 99 |
| sex | 0.0% | 19.4% | 4 |
| race | 0.0% | 0.1% | 7 |
| ethnicity | 0.0% | 19.8% | 4 |
| resident_status | 19.7% | 0.0% | 3 |
| relationship | 56.0% | 0.0% | 60 |
| weapon | 71.4% | 0.1% | 45 |
| injury | 83.1% | 0.0% | 26 |

## Duplicates

2,563 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 4,552 |
| 13B | Simple Assault | 4,322 |
| 13C | Intimidation | 3,100 |
| 23H | All Other Larceny | 2,796 |
| 23C | Shoplifting | 2,588 |
| 13A | Aggravated Assault | 2,063 |
| 240 | Motor Vehicle Theft | 1,801 |
| 23F | Theft From Motor Vehicle | 1,547 |
| 520 | Weapon Law Violations | 1,442 |
| 220 | Burglary/Breaking & Entering | 1,230 |
| 23D | Theft From Building | 1,181 |
| 120 | Robbery | 1,145 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 883 |
| 26B | Credit Card/Automated Teller Machine Fraud | 706 |
| 35A | Drug/Narcotic Violations | 691 |
| 26A | False Pretenses/Swindle/Confidence Game | 649 |
| 26F | Identity Theft | 438 |
| 280 | Stolen Property Offenses | 293 |
| 250 | Counterfeiting/Forgery | 239 |
| 11D | Criminal Sexual Contact | 211 |
| 26E | Wire Fraud | 174 |
| 210 | Extortion/Blackmail | 152 |
| 35B | Drug Equipment Violations | 149 |
| 11A | Rape | 147 |
| 26C | Impersonation | 112 |
| 100 | Kidnapping/Abduction | 46 |
| 370 | Pornography/Obscene Material | 45 |
| 26G | Hacking/Computer Invasion | 41 |
| 270 | Embezzlement | 39 |
| 23A | Pocket-picking | 28 |
| 11B | Sodomy | 20 |
| 09A | Murder and Nonnegligent Manslaughter | 19 |
| 200 | Arson | 17 |
| 23B | Purse-snatching | 11 |
| 11C | Sexual Assault With An Object | 10 |
| 36B | Statutory Rape | 4 |
| 720 | Animal Cruelty | 3 |
| 26D | Welfare Fraud | 1 |
| 36A | Incest | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 1,388 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:1325 2024-02:1232 2024-03:1392 2024-04:1477 2024-05:1531 2024-06:1504 2024-07:1434 2024-08:1371 2024-09:1432 2024-10:1442 2024-11:1361 2024-12:1343 2025-01:1389 2025-02:1166 2025-03:1458 2025-04:1408 2025-05:1421 2025-06:1445 2025-07:1350 2025-08:1388 2025-09:1378 2025-10:1336 2025-11:1167 2025-12:1146

Use only full calendar years where you can; weight any partial year by its share of the year.