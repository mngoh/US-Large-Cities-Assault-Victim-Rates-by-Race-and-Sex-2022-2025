# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/detroit.csv

342,071 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 295,092 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 5.8% | 24 |
| offense_id | 0.0% | 0.0% | 318,399 |
| offense_code | 0.0% | 0.0% | 49 |
| offense_name | 0.0% | 0.0% | 50 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 323,703 |
| victim_seq_num | 0.0% | 0.0% | 26 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 17.3% | 4 |
| race | 0.0% | 3.9% | 6 |
| ethnicity | 0.0% | 100.0% | 3 |
| resident_status | 15.1% | 3.0% | 3 |
| relationship | 61.5% | 0.0% | 197 |
| weapon | 64.0% | 0.5% | 20 |
| injury | 84.7% | 0.0% | 7 |

## Duplicates

18,368 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 65,111 |
| 290 | Destruction/Damage/Vandalism of Property | 49,416 |
| 13A | Aggravated Assault | 39,593 |
| 240 | Motor Vehicle Theft | 34,213 |
| 220 | Burglary/Breaking & Entering | 20,558 |
| 23F | Theft From Motor Vehicle | 17,022 |
| 23H | All Other Larceny | 16,094 |
| 520 | Weapon Law Violations | 13,202 |
| 280 | Stolen Property Offenses | 11,069 |
| 23C | Shoplifting | 10,782 |
| 23D | Theft From Building | 10,517 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 7,606 |
| 26A | False Pretenses/Swindle/Confidence Game | 6,185 |
| 120 | Robbery | 5,749 |
| 13C | Intimidation | 5,398 |
| 26F | Identity Theft | 5,097 |
| 26B | Credit Card/Automated Teller Machine Fraud | 4,940 |
| 35A | Drug/Narcotic Violations | 3,453 |
| 200 | Arson | 2,154 |
| 11A | Rape | 1,668 |
| 26D | Welfare Fraud | 1,444 |
| 26C | Impersonation | 1,179 |
| 11D | Criminal Sexual Contact | 1,100 |
| 40A | Prostitution | 1,027 |
| 26E | Wire Fraud | 929 |
| 09A | Murder and Nonnegligent Manslaughter | 926 |
| 100 | Kidnapping/Abduction | 809 |
| 11B | Sodomy | 757 |
| 250 | Counterfeiting/Forgery | 697 |
| 370 | Pornography/Obscene Material | 511 |
| 11D | Fondling | 427 |
| 270 | Embezzlement | 396 |
| 23B | Purse-snatching | 309 |
| 35B | Drug Equipment Violations | 303 |
| 210 | Extortion/Blackmail | 302 |
| 23A | Pocket-picking | 283 |
| 720 | Animal Cruelty | 210 |
| 26G | Hacking/Computer Invasion | 156 |
| 40C | Purchasing Prostitution | 123 |
| 11C | Sexual Assault With An Object | 120 |
| 09C | Justifiable Homicide | 95 |
| 23E | Theft From Coin-Operated Machine or Device | 37 |
| 40B | Assisting or Promoting Prostitution | 29 |
| 64A | Human Trafficking, Commercial Sex Acts | 26 |
| 09B | Negligent Manslaughter | 16 |
| 64B | Human Trafficking, Involuntary Servitude | 14 |
| 510 | Bribery | 6 |
| 39A | Betting/Wagering | 5 |
| 36A | Incest | 4 |
| 36B | Statutory Rape | 4 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 7,370 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:5968 2022-02:5436 2022-03:6535 2022-04:6560 2022-05:7311 2022-06:7328 2022-07:8000 2022-08:8009 2022-09:7852 2022-10:7901 2022-11:7422 2022-12:7262 2023-01:6905 2023-02:6232 2023-03:6923 2023-04:7511 2023-05:8160 2023-06:8006 2023-07:8415 2023-08:8307 2023-09:7498 2023-10:7853 2023-11:7430 2023-12:7532 2024-01:6712 2024-02:6341 2024-03:6582 2024-04:6759 2024-05:7814 2024-06:7431 2024-07:7933 2024-08:8020 2024-09:7450 2024-10:7552 2024-11:6897 2024-12:6494 2025-01:5907 2025-02:5147 2025-03:6395 2025-04:6574 2025-05:7411 2025-06:7519 2025-07:7804 2025-08:7522 2025-09:6722 2025-10:6906 2025-11:6228 2025-12:5595

Use only full calendar years where you can; weight any partial year by its share of the year.