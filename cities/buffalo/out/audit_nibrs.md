# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/buffalo.csv

117,917 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 88,924 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.7% | 7.2% | 24 |
| offense_id | 0.0% | 0.0% | 114,057 |
| offense_code | 0.0% | 0.0% | 44 |
| offense_name | 0.0% | 0.0% | 45 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 95,187 |
| victim_seq_num | 0.0% | 0.0% | 18 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 17.9% | 4 |
| race | 0.0% | 3.8% | 7 |
| ethnicity | 0.0% | 25.6% | 4 |
| resident_status | 17.8% | 0.2% | 3 |
| relationship | 34.3% | 0.0% | 95 |
| weapon | 77.8% | 0.2% | 57 |
| injury | 88.5% | 0.0% | 46 |

## Duplicates

22,730 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 24,181 |
| 13B | Simple Assault | 15,195 |
| 13C | Intimidation | 11,735 |
| 23D | Theft From Building | 9,266 |
| 240 | Motor Vehicle Theft | 9,240 |
| 23H | All Other Larceny | 7,362 |
| 23F | Theft From Motor Vehicle | 6,731 |
| 23C | Shoplifting | 6,642 |
| 13A | Aggravated Assault | 5,568 |
| 220 | Burglary/Breaking & Entering | 5,455 |
| 26F | Identity Theft | 3,013 |
| 120 | Robbery | 2,360 |
| 520 | Weapon Law Violations | 2,127 |
| 35A | Drug/Narcotic Violations | 2,125 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,047 |
| 280 | Stolen Property Offenses | 1,111 |
| 250 | Counterfeiting/Forgery | 620 |
| 35B | Drug Equipment Violations | 441 |
| 26A | False Pretenses/Swindle/Confidence Game | 392 |
| 11A | Rape | 380 |
| 200 | Arson | 365 |
| 100 | Kidnapping/Abduction | 332 |
| 26C | Impersonation | 231 |
| 11D | Criminal Sexual Contact | 190 |
| 09A | Murder and Nonnegligent Manslaughter | 170 |
| 370 | Pornography/Obscene Material | 113 |
| 23A | Pocket-picking | 111 |
| 11B | Sodomy | 107 |
| 11D | Fondling | 66 |
| 23E | Theft From Coin-Operated Machine or Device | 59 |
| 26B | Credit Card/Automated Teller Machine Fraud | 43 |
| 210 | Extortion/Blackmail | 35 |
| 23B | Purse-snatching | 30 |
| 36B | Statutory Rape | 20 |
| 11C | Sexual Assault With An Object | 10 |
| 26D | Welfare Fraud | 10 |
| 720 | Animal Cruelty | 9 |
| 26G | Hacking/Computer Invasion | 7 |
| 09B | Negligent Manslaughter | 7 |
| 40A | Prostitution | 3 |
| 09C | Justifiable Homicide | 3 |
| 510 | Bribery | 2 |
| 270 | Embezzlement | 1 |
| 40B | Assisting or Promoting Prostitution | 1 |
| 64A | Human Trafficking, Commercial Sex Acts | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,478 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1733 2022-02:1642 2022-03:2044 2022-04:2086 2022-05:2191 2022-06:2470 2022-07:2830 2022-08:2538 2022-09:2444 2022-10:2397 2022-11:1826 2022-12:2405 2023-01:2775 2023-02:2097 2023-03:2548 2023-04:2511 2023-05:3147 2023-06:3491 2023-07:3223 2023-08:3171 2023-09:2664 2023-10:2609 2023-11:2509 2023-12:2636 2024-01:2266 2024-02:2275 2024-03:2522 2024-04:2410 2024-05:2921 2024-06:2853 2024-07:2833 2024-08:2720 2024-09:2536 2024-10:2448 2024-11:2041 2024-12:1850 2025-01:2126 2025-02:1799 2025-03:2191 2025-04:2235 2025-05:2511 2025-06:2640 2025-07:2922 2025-08:2481 2025-09:2744 2025-10:2476 2025-11:2220 2025-12:1910

Use only full calendar years where you can; weight any partial year by its share of the year.