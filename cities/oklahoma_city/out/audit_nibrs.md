# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/oklahoma_city.csv

215,180 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 178,878 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 2.7% | 24 |
| offense_id | 0.0% | 0.0% | 199,254 |
| offense_code | 0.0% | 0.0% | 51 |
| offense_name | 0.0% | 0.0% | 52 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 198,872 |
| victim_seq_num | 0.0% | 0.0% | 51 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 30.0% | 4 |
| race | 0.0% | 3.1% | 7 |
| ethnicity | 0.0% | 100.0% | 1 |
| resident_status | 90.6% | 0.2% | 3 |
| relationship | 73.8% | 0.0% | 281 |
| weapon | 76.2% | 0.7% | 153 |
| injury | 89.6% | 0.0% | 66 |

## Duplicates

16,308 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 25,847 |
| 13B | Simple Assault | 24,584 |
| 23F | Theft From Motor Vehicle | 17,780 |
| 220 | Burglary/Breaking & Entering | 16,998 |
| 23C | Shoplifting | 15,905 |
| 23H | All Other Larceny | 14,377 |
| 13A | Aggravated Assault | 13,856 |
| 240 | Motor Vehicle Theft | 11,026 |
| 13C | Intimidation | 9,732 |
| 26A | False Pretenses/Swindle/Confidence Game | 8,564 |
| 35A | Drug/Narcotic Violations | 8,480 |
| 23D | Theft From Building | 5,975 |
| 26B | Credit Card/Automated Teller Machine Fraud | 4,829 |
| 520 | Weapon Law Violations | 4,731 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 4,030 |
| 120 | Robbery | 3,470 |
| 35B | Drug Equipment Violations | 3,372 |
| 26F | Identity Theft | 3,104 |
| 270 | Embezzlement | 2,983 |
| 250 | Counterfeiting/Forgery | 2,520 |
| 280 | Stolen Property Offenses | 2,050 |
| 11A | Rape | 1,488 |
| 370 | Pornography/Obscene Material | 1,256 |
| 11D | Criminal Sexual Contact | 1,170 |
| 26E | Wire Fraud | 830 |
| 100 | Kidnapping/Abduction | 795 |
| 210 | Extortion/Blackmail | 782 |
| 200 | Arson | 624 |
| 26G | Hacking/Computer Invasion | 597 |
| 40A | Prostitution | 525 |
| 720 | Animal Cruelty | 456 |
| 11B | Sodomy | 400 |
| 11D | Fondling | 368 |
| 26C | Impersonation | 367 |
| 09A | Murder and Nonnegligent Manslaughter | 269 |
| 40C | Purchasing Prostitution | 253 |
| 11C | Sexual Assault With An Object | 201 |
| 23A | Pocket-picking | 107 |
| 26D | Welfare Fraud | 83 |
| 36B | Statutory Rape | 82 |
| 23E | Theft From Coin-Operated Machine or Device | 79 |
| 40B | Assisting or Promoting Prostitution | 66 |
| 23B | Purse-snatching | 42 |
| 64A | Human Trafficking, Commercial Sex Acts | 39 |
| 09B | Negligent Manslaughter | 38 |
| 36A | Incest | 19 |
| 64B | Human Trafficking, Involuntary Servitude | 16 |
| 39B | Operating/Promoting/Assisting Gambling | 5 |
| 39C | Gambling Equipment Violation | 4 |
| 510 | Bribery | 4 |
| 09C | Justifiable Homicide | 1 |
| 39A | Betting/Wagering | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 4,570 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:4140 2022-02:3741 2022-03:3843 2022-04:3985 2022-05:4722 2022-06:4614 2022-07:4773 2022-08:4631 2022-09:4812 2022-10:4814 2022-11:4074 2022-12:4173 2023-01:4412 2023-02:3883 2023-03:4590 2023-04:4458 2023-05:4725 2023-06:4549 2023-07:4530 2023-08:4218 2023-09:3812 2023-10:4322 2023-11:4024 2023-12:4457 2024-01:4285 2024-02:4310 2024-03:4655 2024-04:4744 2024-05:5133 2024-06:4758 2024-07:4733 2024-08:4628 2024-09:4912 2024-10:4889 2024-11:4435 2024-12:4467 2025-01:4113 2025-02:3771 2025-03:4788 2025-04:4658 2025-05:5018 2025-06:4861 2025-07:4618 2025-08:4889 2025-09:4709 2025-10:4824 2025-11:4211 2025-12:4469

Use only full calendar years where you can; weight any partial year by its share of the year.