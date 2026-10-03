# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/memphis.csv

470,760 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 367,056 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 5.9% | 24 |
| offense_id | 0.0% | 0.0% | 406,926 |
| offense_code | 0.0% | 0.0% | 51 |
| offense_name | 0.0% | 0.0% | 52 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 447,685 |
| victim_seq_num | 0.0% | 0.0% | 58 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 23.1% | 4 |
| race | 0.0% | 0.2% | 7 |
| ethnicity | 0.0% | 23.1% | 4 |
| resident_status | 22.9% | 0.7% | 3 |
| relationship | 67.2% | 0.0% | 496 |
| weapon | 71.9% | 0.2% | 153 |
| injury | 90.4% | 0.0% | 13 |

## Duplicates

23,075 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 65,436 |
| 13B | Simple Assault | 55,436 |
| 13A | Aggravated Assault | 47,562 |
| 23F | Theft From Motor Vehicle | 47,302 |
| 240 | Motor Vehicle Theft | 43,086 |
| 23C | Shoplifting | 36,935 |
| 13C | Intimidation | 36,611 |
| 220 | Burglary/Breaking & Entering | 24,330 |
| 23H | All Other Larceny | 16,294 |
| 520 | Weapon Law Violations | 15,782 |
| 120 | Robbery | 12,223 |
| 35A | Drug/Narcotic Violations | 11,589 |
| 23D | Theft From Building | 11,023 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 10,354 |
| 26A | False Pretenses/Swindle/Confidence Game | 5,298 |
| 26B | Credit Card/Automated Teller Machine Fraud | 4,631 |
| 35B | Drug Equipment Violations | 4,386 |
| 250 | Counterfeiting/Forgery | 3,361 |
| 100 | Kidnapping/Abduction | 2,508 |
| 280 | Stolen Property Offenses | 2,408 |
| 200 | Arson | 1,819 |
| 270 | Embezzlement | 1,624 |
| 26C | Impersonation | 1,503 |
| 11A | Rape | 1,248 |
| 09A | Murder and Nonnegligent Manslaughter | 1,058 |
| 26E | Wire Fraud | 1,014 |
| 11D | Criminal Sexual Contact | 765 |
| 370 | Pornography/Obscene Material | 734 |
| 26F | Identity Theft | 525 |
| 720 | Animal Cruelty | 458 |
| 40A | Prostitution | 417 |
| 210 | Extortion/Blackmail | 384 |
| 23A | Pocket-picking | 346 |
| 26G | Hacking/Computer Invasion | 318 |
| 11D | Fondling | 317 |
| 11B | Sodomy | 311 |
| 23B | Purse-snatching | 242 |
| 40C | Purchasing Prostitution | 215 |
| 39B | Operating/Promoting/Assisting Gambling | 194 |
| 09C | Justifiable Homicide | 126 |
| 36B | Statutory Rape | 123 |
| 09B | Negligent Manslaughter | 120 |
| 11C | Sexual Assault With An Object | 87 |
| 26D | Welfare Fraud | 77 |
| 23E | Theft From Coin-Operated Machine or Device | 73 |
| 64A | Human Trafficking, Commercial Sex Acts | 51 |
| 39A | Betting/Wagering | 22 |
| 40B | Assisting or Promoting Prostitution | 16 |
| 39C | Gambling Equipment Violation | 11 |
| 36A | Incest | 4 |
| 510 | Bribery | 2 |
| 64B | Human Trafficking, Involuntary Servitude | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 10,032 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- 2025-11: 5,877

Full series:

2022-01:8838 2022-02:7885 2022-03:8990 2022-04:10071 2022-05:11084 2022-06:11025 2022-07:11332 2022-08:11559 2022-09:10988 2022-10:11140 2022-11:10567 2022-12:11302 2023-01:11313 2023-02:9992 2023-03:11361 2023-04:11606 2023-05:12609 2023-06:12323 2023-07:12317 2023-08:11625 2023-09:10753 2023-10:11206 2023-11:10177 2023-12:10331 2024-01:8784 2024-02:9316 2024-03:9395 2024-04:10122 2024-05:11470 2024-06:11334 2024-07:10783 2024-08:9750 2024-09:9732 2024-10:9597 2024-11:8683 2024-12:8884 2025-01:8355 2025-02:7179 2025-03:8367 2025-04:8716 2025-05:9010 2025-06:8253 2025-07:8525 2025-08:8109 2025-09:7593 2025-10:6375 2025-11:5877 2025-12:6157

Use only full calendar years where you can; weight any partial year by its share of the year.