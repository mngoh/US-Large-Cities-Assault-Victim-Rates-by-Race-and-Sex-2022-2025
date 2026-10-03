# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/long_beach.csv

60,699 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 50,127 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 6.2% | 24 |
| offense_id | 0.0% | 0.0% | 55,106 |
| offense_code | 0.0% | 0.0% | 46 |
| offense_name | 0.0% | 0.0% | 46 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 57,425 |
| victim_seq_num | 0.0% | 0.0% | 16 |
| victim_type | 0.0% | 0.1% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 24.9% | 4 |
| race | 0.0% | 7.1% | 7 |
| ethnicity | 0.0% | 40.6% | 4 |
| resident_status | 76.6% | 0.8% | 3 |
| relationship | 57.3% | 0.0% | 123 |
| weapon | 72.9% | 0.6% | 61 |
| injury | 85.6% | 0.0% | 46 |

## Duplicates

3,274 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 8,527 |
| 240 | Motor Vehicle Theft | 7,837 |
| 290 | Destruction/Damage/Vandalism of Property | 7,112 |
| 220 | Burglary/Breaking & Entering | 6,004 |
| 23C | Shoplifting | 4,852 |
| 23F | Theft From Motor Vehicle | 4,423 |
| 13A | Aggravated Assault | 3,660 |
| 23H | All Other Larceny | 3,003 |
| 120 | Robbery | 2,511 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,185 |
| 13C | Intimidation | 1,496 |
| 35B | Drug Equipment Violations | 1,385 |
| 520 | Weapon Law Violations | 1,262 |
| 35A | Drug/Narcotic Violations | 1,134 |
| 23D | Theft From Building | 1,003 |
| 250 | Counterfeiting/Forgery | 570 |
| 26A | False Pretenses/Swindle/Confidence Game | 535 |
| 26F | Identity Theft | 450 |
| 200 | Arson | 414 |
| 11D | Criminal Sexual Contact | 379 |
| 280 | Stolen Property Offenses | 310 |
| 26B | Credit Card/Automated Teller Machine Fraud | 308 |
| 11A | Rape | 278 |
| 100 | Kidnapping/Abduction | 239 |
| 26C | Impersonation | 184 |
| 23A | Pocket-picking | 110 |
| 11B | Sodomy | 99 |
| 09A | Murder and Nonnegligent Manslaughter | 66 |
| 23B | Purse-snatching | 63 |
| 270 | Embezzlement | 56 |
| 720 | Animal Cruelty | 55 |
| 11C | Sexual Assault With An Object | 44 |
| 370 | Pornography/Obscene Material | 42 |
| 210 | Extortion/Blackmail | 31 |
| 23E | Theft From Coin-Operated Machine or Device | 17 |
| 36B | Statutory Rape | 14 |
| 40A | Prostitution | 8 |
| 26G | Hacking/Computer Invasion | 7 |
| 64B | Human Trafficking, Involuntary Servitude | 6 |
| 09B | Negligent Manslaughter | 5 |
| 64A | Human Trafficking, Commercial Sex Acts | 5 |
| 40B | Assisting or Promoting Prostitution | 4 |
| 40C | Purchasing Prostitution | 2 |
| 26D | Welfare Fraud | 2 |
| 510 | Bribery | 1 |
| 09C | Justifiable Homicide | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 2,552 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:2895 2024-02:2751 2024-03:3121 2024-04:2810 2024-05:3049 2024-06:2695 2024-07:2811 2024-08:2849 2024-09:2754 2024-10:2763 2024-11:2500 2024-12:2339 2025-01:2684 2025-02:2310 2025-03:2485 2025-04:2481 2025-05:2603 2025-06:2315 2025-07:2407 2025-08:2276 2025-09:2212 2025-10:1979 2025-11:1827 2025-12:1783

Use only full calendar years where you can; weight any partial year by its share of the year.