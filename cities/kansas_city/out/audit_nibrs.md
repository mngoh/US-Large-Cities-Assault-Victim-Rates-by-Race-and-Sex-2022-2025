# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/kansas_city.csv

214,085 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 178,070 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 5.4% | 24 |
| offense_id | 0.0% | 0.0% | 186,969 |
| offense_code | 0.0% | 0.0% | 47 |
| offense_name | 0.0% | 0.0% | 48 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 205,675 |
| victim_seq_num | 0.0% | 0.0% | 124 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 18.1% | 4 |
| race | 0.0% | 3.2% | 7 |
| ethnicity | 0.0% | 36.7% | 4 |
| resident_status | 51.2% | 2.1% | 3 |
| relationship | 59.6% | 0.0% | 351 |
| weapon | 69.8% | 0.4% | 127 |
| injury | 86.9% | 0.0% | 67 |

## Duplicates

8,410 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 240 | Motor Vehicle Theft | 30,799 |
| 13B | Simple Assault | 29,999 |
| 290 | Destruction/Damage/Vandalism of Property | 28,105 |
| 13A | Aggravated Assault | 23,622 |
| 23F | Theft From Motor Vehicle | 19,576 |
| 220 | Burglary/Breaking & Entering | 12,953 |
| 23C | Shoplifting | 11,525 |
| 23H | All Other Larceny | 10,363 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 8,602 |
| 120 | Robbery | 6,850 |
| 23D | Theft From Building | 6,473 |
| 13C | Intimidation | 5,455 |
| 26A | False Pretenses/Swindle/Confidence Game | 2,625 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,613 |
| 35A | Drug/Narcotic Violations | 2,165 |
| 26F | Identity Theft | 1,933 |
| 520 | Weapon Law Violations | 1,889 |
| 250 | Counterfeiting/Forgery | 1,289 |
| 11A | Rape | 1,148 |
| 35B | Drug Equipment Violations | 1,006 |
| 280 | Stolen Property Offenses | 950 |
| 09A | Murder and Nonnegligent Manslaughter | 623 |
| 26E | Wire Fraud | 574 |
| 200 | Arson | 543 |
| 270 | Embezzlement | 502 |
| 11B | Sodomy | 355 |
| 11D | Criminal Sexual Contact | 311 |
| 23A | Pocket-picking | 145 |
| 26D | Welfare Fraud | 142 |
| 210 | Extortion/Blackmail | 131 |
| 36B | Statutory Rape | 120 |
| 40A | Prostitution | 118 |
| 23B | Purse-snatching | 93 |
| 26G | Hacking/Computer Invasion | 87 |
| 11D | Fondling | 86 |
| 100 | Kidnapping/Abduction | 58 |
| 11C | Sexual Assault With An Object | 38 |
| 720 | Animal Cruelty | 36 |
| 26C | Impersonation | 34 |
| 370 | Pornography/Obscene Material | 30 |
| 64A | Human Trafficking, Commercial Sex Acts | 30 |
| 23E | Theft From Coin-Operated Machine or Device | 29 |
| 40C | Purchasing Prostitution | 17 |
| 36A | Incest | 15 |
| 64B | Human Trafficking, Involuntary Servitude | 9 |
| 40B | Assisting or Promoting Prostitution | 7 |
| 09C | Justifiable Homicide | 7 |
| 09B | Negligent Manslaughter | 5 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 4,449 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:4114 2022-02:3496 2022-03:4318 2022-04:4465 2022-05:4779 2022-06:4433 2022-07:5036 2022-08:4765 2022-09:4681 2022-10:4868 2022-11:4050 2022-12:4156 2023-01:4264 2023-02:3741 2023-03:4408 2023-04:4621 2023-05:4846 2023-06:4949 2023-07:5672 2023-08:5285 2023-09:4391 2023-10:4686 2023-11:4337 2023-12:4652 2024-01:4279 2024-02:4157 2024-03:4218 2024-04:3584 2024-05:4888 2024-06:5089 2024-07:5670 2024-08:5283 2024-09:4795 2024-10:4865 2024-11:4059 2024-12:4116 2025-01:3648 2025-02:3543 2025-03:4620 2025-04:4602 2025-05:4625 2025-06:4238 2025-07:4626 2025-08:4479 2025-09:4138 2025-10:4102 2025-11:3812 2025-12:3636

Use only full calendar years where you can; weight any partial year by its share of the year.