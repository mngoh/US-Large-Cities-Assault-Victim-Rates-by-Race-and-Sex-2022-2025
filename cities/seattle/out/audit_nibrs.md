# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/seattle.csv

296,967 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 243,191 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 11.0% | 24 |
| offense_id | 0.0% | 0.0% | 264,665 |
| offense_code | 0.0% | 0.0% | 50 |
| offense_name | 0.0% | 0.0% | 51 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 279,609 |
| victim_seq_num | 0.0% | 0.0% | 32 |
| victim_type | 0.0% | 0.2% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 23.9% | 4 |
| race | 0.0% | 23.2% | 7 |
| ethnicity | 0.0% | 55.4% | 4 |
| resident_status | 74.8% | 8.8% | 3 |
| relationship | 68.0% | 0.0% | 194 |
| weapon | 82.8% | 0.3% | 131 |
| injury | 91.1% | 0.0% | 68 |

## Duplicates

17,358 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 220 | Burglary/Breaking & Entering | 39,435 |
| 23F | Theft From Motor Vehicle | 36,010 |
| 240 | Motor Vehicle Theft | 33,235 |
| 290 | Destruction/Damage/Vandalism of Property | 31,460 |
| 23H | All Other Larceny | 25,016 |
| 13B | Simple Assault | 20,936 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 20,708 |
| 23C | Shoplifting | 15,689 |
| 13A | Aggravated Assault | 15,444 |
| 13C | Intimidation | 11,242 |
| 120 | Robbery | 9,818 |
| 23D | Theft From Building | 7,801 |
| 35A | Drug/Narcotic Violations | 3,874 |
| 520 | Weapon Law Violations | 3,496 |
| 26B | Credit Card/Automated Teller Machine Fraud | 3,437 |
| 280 | Stolen Property Offenses | 3,420 |
| 26F | Identity Theft | 2,928 |
| 26A | False Pretenses/Swindle/Confidence Game | 2,695 |
| 26E | Wire Fraud | 1,552 |
| 11A | Rape | 1,038 |
| 250 | Counterfeiting/Forgery | 947 |
| 100 | Kidnapping/Abduction | 855 |
| 200 | Arson | 841 |
| 11D | Criminal Sexual Contact | 655 |
| 210 | Extortion/Blackmail | 648 |
| 26C | Impersonation | 589 |
| 23A | Pocket-picking | 429 |
| 26G | Hacking/Computer Invasion | 425 |
| 35B | Drug Equipment Violations | 378 |
| 11B | Sodomy | 263 |
| 370 | Pornography/Obscene Material | 220 |
| 11D | Fondling | 217 |
| 09A | Murder and Nonnegligent Manslaughter | 209 |
| 270 | Embezzlement | 204 |
| 720 | Animal Cruelty | 193 |
| 40C | Purchasing Prostitution | 133 |
| 11C | Sexual Assault With An Object | 131 |
| 23B | Purse-snatching | 124 |
| 64A | Human Trafficking, Commercial Sex Acts | 66 |
| 26D | Welfare Fraud | 48 |
| 40A | Prostitution | 33 |
| 36B | Statutory Rape | 31 |
| 23E | Theft From Coin-Operated Machine or Device | 29 |
| 40B | Assisting or Promoting Prostitution | 18 |
| 09C | Justifiable Homicide | 14 |
| 09B | Negligent Manslaughter | 12 |
| 64B | Human Trafficking, Involuntary Servitude | 9 |
| 36A | Incest | 4 |
| 510 | Bribery | 4 |
| 39A | Betting/Wagering | 3 |
| 39B | Operating/Promoting/Assisting Gambling | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 6,108 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:6876 2022-02:6482 2022-03:7138 2022-04:6448 2022-05:6844 2022-06:6424 2022-07:6949 2022-08:6861 2022-09:6350 2022-10:6496 2022-11:5974 2022-12:5746 2023-01:6003 2023-02:5161 2023-03:5807 2023-04:5954 2023-05:6540 2023-06:5928 2023-07:6946 2023-08:6877 2023-09:6364 2023-10:6456 2023-11:6115 2023-12:5926 2024-01:5846 2024-02:5184 2024-03:5753 2024-04:5809 2024-05:6337 2024-06:5927 2024-07:6555 2024-08:6688 2024-09:6915 2024-10:7160 2024-11:6289 2024-12:5937 2025-01:5828 2025-02:4749 2025-03:5359 2025-04:5365 2025-05:6060 2025-06:5722 2025-07:6015 2025-08:6482 2025-09:6100 2025-10:6519 2025-11:5693 2025-12:6010

Use only full calendar years where you can; weight any partial year by its share of the year.