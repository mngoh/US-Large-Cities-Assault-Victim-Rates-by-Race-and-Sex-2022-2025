# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/san_diego.csv

231,341 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 197,115 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 4.9% | 24 |
| offense_id | 0.0% | 0.0% | 219,275 |
| offense_code | 0.0% | 0.0% | 47 |
| offense_name | 0.0% | 0.0% | 48 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 40 |
| victim_id | 0.0% | 0.0% | 214,143 |
| victim_seq_num | 0.0% | 0.0% | 58 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 30.0% | 4 |
| race | 0.0% | 6.4% | 7 |
| ethnicity | 0.0% | 35.7% | 4 |
| resident_status | 29.4% | 21.5% | 2 |
| relationship | 56.8% | 0.0% | 49 |
| weapon | 75.9% | 1.5% | 21 |
| injury | 87.6% | 0.0% | 86 |

## Duplicates

17,198 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 23H | All Other Larceny | 28,610 |
| 290 | Destruction/Damage/Vandalism of Property | 28,163 |
| 13B | Simple Assault | 27,550 |
| 240 | Motor Vehicle Theft | 23,389 |
| 23F | Theft From Motor Vehicle | 20,087 |
| 13A | Aggravated Assault | 16,889 |
| 35A | Drug/Narcotic Violations | 15,588 |
| 220 | Burglary/Breaking & Entering | 13,235 |
| 35B | Drug Equipment Violations | 9,539 |
| 23C | Shoplifting | 9,537 |
| 26C | Impersonation | 8,588 |
| 120 | Robbery | 5,404 |
| 520 | Weapon Law Violations | 3,788 |
| 13C | Intimidation | 3,452 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,864 |
| 280 | Stolen Property Offenses | 2,653 |
| 23D | Theft From Building | 1,603 |
| 26A | False Pretenses/Swindle/Confidence Game | 1,357 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,217 |
| 11D | Criminal Sexual Contact | 1,061 |
| 26F | Identity Theft | 1,052 |
| 11A | Rape | 1,010 |
| 100 | Kidnapping/Abduction | 878 |
| 250 | Counterfeiting/Forgery | 835 |
| 200 | Arson | 720 |
| 11D | Fondling | 355 |
| 23A | Pocket-picking | 282 |
| 40A | Prostitution | 268 |
| 23B | Purse-snatching | 265 |
| 270 | Embezzlement | 261 |
| 11B | Sodomy | 209 |
| 11C | Sexual Assault With An Object | 153 |
| 09A | Murder and Nonnegligent Manslaughter | 152 |
| 210 | Extortion/Blackmail | 68 |
| 36B | Statutory Rape | 63 |
| 370 | Pornography/Obscene Material | 49 |
| 40B | Assisting or Promoting Prostitution | 46 |
| 23E | Theft From Coin-Operated Machine or Device | 24 |
| 26G | Hacking/Computer Invasion | 21 |
| 39A | Betting/Wagering | 19 |
| 720 | Animal Cruelty | 12 |
| 26D | Welfare Fraud | 6 |
| 09B | Negligent Manslaughter | 6 |
| 64B | Human Trafficking, Involuntary Servitude | 5 |
| 36A | Incest | 2 |
| 39B | Operating/Promoting/Assisting Gambling | 2 |
| 39C | Gambling Equipment Violation | 2 |
| 510 | Bribery | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 4,802 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:5286 2022-02:5114 2022-03:5624 2022-04:5026 2022-05:4846 2022-06:4987 2022-07:5155 2022-08:5101 2022-09:4932 2022-10:5287 2022-11:4762 2022-12:5030 2023-01:5000 2023-02:4446 2023-03:4992 2023-04:4882 2023-05:5078 2023-06:4758 2023-07:5267 2023-08:5156 2023-09:4820 2023-10:4748 2023-11:4696 2023-12:4591 2024-01:4884 2024-02:4539 2024-03:4852 2024-04:4835 2024-05:5118 2024-06:4697 2024-07:5038 2024-08:4608 2024-09:4178 2024-10:4566 2024-11:4680 2024-12:4994 2025-01:4727 2025-02:4126 2025-03:4561 2025-04:4366 2025-05:4740 2025-06:4447 2025-07:4783 2025-08:4715 2025-09:4578 2025-10:4766 2025-11:4389 2025-12:4570

Use only full calendar years where you can; weight any partial year by its share of the year.