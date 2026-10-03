# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/philadelphia.csv

650,859 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 561,887 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 13.2% | 4.2% | 24 |
| offense_id | 0.0% | 0.0% | 629,689 |
| offense_code | 0.0% | 0.0% | 50 |
| offense_name | 0.0% | 0.0% | 51 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 602,088 |
| victim_seq_num | 0.0% | 0.0% | 35 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 25.4% | 4 |
| race | 0.0% | 0.9% | 7 |
| ethnicity | 0.0% | 40.1% | 4 |
| resident_status | 25.2% | 3.6% | 3 |
| relationship | 69.0% | 0.0% | 204 |
| weapon | 77.7% | 0.3% | 104 |
| injury | 90.3% | 0.0% | 81 |

## Duplicates

48,771 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 104,626 |
| 23C | Shoplifting | 74,817 |
| 240 | Motor Vehicle Theft | 69,110 |
| 13B | Simple Assault | 57,847 |
| 23H | All Other Larceny | 48,771 |
| 23F | Theft From Motor Vehicle | 41,876 |
| 13C | Intimidation | 39,174 |
| 13A | Aggravated Assault | 36,015 |
| 520 | Weapon Law Violations | 26,915 |
| 26A | False Pretenses/Swindle/Confidence Game | 26,500 |
| 120 | Robbery | 22,703 |
| 220 | Burglary/Breaking & Entering | 22,493 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 20,983 |
| 35A | Drug/Narcotic Violations | 12,593 |
| 23D | Theft From Building | 11,386 |
| 26B | Credit Card/Automated Teller Machine Fraud | 5,979 |
| 26F | Identity Theft | 4,666 |
| 26E | Wire Fraud | 4,074 |
| 200 | Arson | 2,754 |
| 11A | Rape | 2,181 |
| 370 | Pornography/Obscene Material | 1,441 |
| 11D | Criminal Sexual Contact | 1,418 |
| 09A | Murder and Nonnegligent Manslaughter | 1,403 |
| 23A | Pocket-picking | 1,302 |
| 280 | Stolen Property Offenses | 1,160 |
| 250 | Counterfeiting/Forgery | 1,054 |
| 210 | Extortion/Blackmail | 856 |
| 26D | Welfare Fraud | 847 |
| 270 | Embezzlement | 818 |
| 40A | Prostitution | 755 |
| 11B | Sodomy | 668 |
| 23B | Purse-snatching | 564 |
| 11D | Fondling | 524 |
| 100 | Kidnapping/Abduction | 471 |
| 35B | Drug Equipment Violations | 356 |
| 11C | Sexual Assault With An Object | 282 |
| 40C | Purchasing Prostitution | 266 |
| 26G | Hacking/Computer Invasion | 232 |
| 26C | Impersonation | 227 |
| 23E | Theft From Coin-Operated Machine or Device | 194 |
| 720 | Animal Cruelty | 110 |
| 09B | Negligent Manslaughter | 108 |
| 09C | Justifiable Homicide | 95 |
| 36B | Statutory Rape | 80 |
| 39C | Gambling Equipment Violation | 61 |
| 64A | Human Trafficking, Commercial Sex Acts | 48 |
| 39B | Operating/Promoting/Assisting Gambling | 23 |
| 510 | Bribery | 18 |
| 64B | Human Trafficking, Involuntary Servitude | 10 |
| 40B | Assisting or Promoting Prostitution | 3 |
| 39A | Betting/Wagering | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 13,656 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:11211 2022-02:10894 2022-03:12324 2022-04:12465 2022-05:13512 2022-06:13820 2022-07:14139 2022-08:14076 2022-09:13428 2022-10:13663 2022-11:13220 2022-12:13172 2023-01:14184 2023-02:12810 2023-03:14290 2023-04:13863 2023-05:15645 2023-06:15644 2023-07:16827 2023-08:16546 2023-09:14463 2023-10:14785 2023-11:13649 2023-12:13505 2024-01:12686 2024-02:11840 2024-03:12369 2024-04:13371 2024-05:14870 2024-06:15008 2024-07:15286 2024-08:14571 2024-09:13972 2024-10:14563 2024-11:13071 2024-12:12039 2025-01:12017 2025-02:10555 2025-03:13126 2025-04:13016 2025-05:13316 2025-06:14012 2025-07:14413 2025-08:13681 2025-09:13948 2025-10:13819 2025-11:12200 2025-12:10975

Use only full calendar years where you can; weight any partial year by its share of the year.