# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/charlotte.csv

359,167 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 273,068 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 5.2% | 24 |
| offense_id | 0.0% | 0.0% | 312,478 |
| offense_code | 0.0% | 0.0% | 51 |
| offense_name | 0.0% | 0.0% | 52 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 329,354 |
| victim_seq_num | 0.0% | 0.0% | 92 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 102 |
| age_num | 0.0% | 0.0% | 102 |
| sex | 0.0% | 29.6% | 4 |
| race | 0.0% | 8.4% | 7 |
| ethnicity | 0.0% | 73.5% | 4 |
| resident_status | 29.2% | 70.0% | 2 |
| relationship | 75.8% | 0.0% | 387 |
| weapon | 77.5% | 0.8% | 108 |
| injury | 91.6% | 0.0% | 7 |

## Duplicates

29,813 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 23F | Theft From Motor Vehicle | 55,684 |
| 13B | Simple Assault | 41,293 |
| 23H | All Other Larceny | 33,534 |
| 290 | Destruction/Damage/Vandalism of Property | 32,578 |
| 240 | Motor Vehicle Theft | 26,698 |
| 23C | Shoplifting | 22,962 |
| 13A | Aggravated Assault | 21,556 |
| 220 | Burglary/Breaking & Entering | 19,139 |
| 35A | Drug/Narcotic Violations | 16,945 |
| 13C | Intimidation | 14,687 |
| 520 | Weapon Law Violations | 9,214 |
| 35B | Drug Equipment Violations | 8,133 |
| 26A | False Pretenses/Swindle/Confidence Game | 7,879 |
| 120 | Robbery | 7,046 |
| 26B | Credit Card/Automated Teller Machine Fraud | 6,807 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 5,853 |
| 280 | Stolen Property Offenses | 4,186 |
| 26F | Identity Theft | 3,936 |
| 23D | Theft From Building | 3,842 |
| 250 | Counterfeiting/Forgery | 3,237 |
| 26C | Impersonation | 2,104 |
| 100 | Kidnapping/Abduction | 1,758 |
| 370 | Pornography/Obscene Material | 1,351 |
| 11D | Criminal Sexual Contact | 1,192 |
| 270 | Embezzlement | 1,166 |
| 210 | Extortion/Blackmail | 1,090 |
| 200 | Arson | 853 |
| 11A | Rape | 738 |
| 23A | Pocket-picking | 716 |
| 26G | Hacking/Computer Invasion | 574 |
| 23B | Purse-snatching | 526 |
| 11D | Fondling | 440 |
| 09A | Murder and Nonnegligent Manslaughter | 402 |
| 11B | Sodomy | 243 |
| 26E | Wire Fraud | 216 |
| 720 | Animal Cruelty | 120 |
| 23E | Theft From Coin-Operated Machine or Device | 117 |
| 36B | Statutory Rape | 96 |
| 09C | Justifiable Homicide | 51 |
| 39C | Gambling Equipment Violation | 37 |
| 11C | Sexual Assault With An Object | 32 |
| 39B | Operating/Promoting/Assisting Gambling | 28 |
| 09B | Negligent Manslaughter | 20 |
| 64B | Human Trafficking, Involuntary Servitude | 18 |
| 64A | Human Trafficking, Commercial Sex Acts | 15 |
| 40A | Prostitution | 11 |
| 40B | Assisting or Promoting Prostitution | 10 |
| 36A | Incest | 9 |
| 39A | Betting/Wagering | 9 |
| 40C | Purchasing Prostitution | 8 |
| 26D | Welfare Fraud | 4 |
| 510 | Bribery | 4 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 7,484 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:6798 2022-02:6506 2022-03:6800 2022-04:7046 2022-05:7825 2022-06:7470 2022-07:7498 2022-08:7750 2022-09:7186 2022-10:7447 2022-11:6623 2022-12:6807 2023-01:7357 2023-02:6465 2023-03:7110 2023-04:7335 2023-05:8217 2023-06:7960 2023-07:8208 2023-08:7917 2023-09:7889 2023-10:8316 2023-11:7829 2023-12:8560 2024-01:7953 2024-02:7063 2024-03:7131 2024-04:7495 2024-05:8019 2024-06:7815 2024-07:7777 2024-08:7434 2024-09:7710 2024-10:7881 2024-11:7220 2024-12:7331 2025-01:7450 2025-02:6509 2025-03:7472 2025-04:7189 2025-05:7647 2025-06:7603 2025-07:8123 2025-08:7775 2025-09:7895 2025-10:7843 2025-11:7045 2025-12:6868

Use only full calendar years where you can; weight any partial year by its share of the year.