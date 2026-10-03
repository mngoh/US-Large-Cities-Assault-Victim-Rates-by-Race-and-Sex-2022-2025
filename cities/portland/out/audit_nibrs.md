# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/portland.csv

253,997 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 228,810 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 5.7% | 24 |
| offense_id | 0.0% | 0.0% | 238,693 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 247,214 |
| victim_seq_num | 0.0% | 0.0% | 22 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 29.2% | 4 |
| race | 0.0% | 5.7% | 7 |
| ethnicity | 0.0% | 93.0% | 4 |
| resident_status | 28.9% | 5.0% | 3 |
| relationship | 84.4% | 0.0% | 178 |
| weapon | 82.1% | 0.3% | 91 |
| injury | 92.8% | 0.0% | 64 |

## Duplicates

6,783 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 35,713 |
| 23F | Theft From Motor Vehicle | 31,216 |
| 23C | Shoplifting | 29,991 |
| 240 | Motor Vehicle Theft | 29,906 |
| 23H | All Other Larceny | 22,019 |
| 13B | Simple Assault | 21,446 |
| 220 | Burglary/Breaking & Entering | 19,848 |
| 13A | Aggravated Assault | 12,058 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 8,714 |
| 120 | Robbery | 7,227 |
| 23D | Theft From Building | 6,547 |
| 26A | False Pretenses/Swindle/Confidence Game | 4,816 |
| 26F | Identity Theft | 3,595 |
| 520 | Weapon Law Violations | 3,514 |
| 26B | Credit Card/Automated Teller Machine Fraud | 3,291 |
| 13C | Intimidation | 3,225 |
| 35A | Drug/Narcotic Violations | 2,792 |
| 200 | Arson | 1,332 |
| 11A | Rape | 1,182 |
| 250 | Counterfeiting/Forgery | 992 |
| 23B | Purse-snatching | 481 |
| 11D | Criminal Sexual Contact | 445 |
| 40C | Purchasing Prostitution | 409 |
| 40B | Assisting or Promoting Prostitution | 321 |
| 100 | Kidnapping/Abduction | 309 |
| 09A | Murder and Nonnegligent Manslaughter | 286 |
| 370 | Pornography/Obscene Material | 245 |
| 23A | Pocket-picking | 240 |
| 26E | Wire Fraud | 206 |
| 270 | Embezzlement | 197 |
| 280 | Stolen Property Offenses | 178 |
| 720 | Animal Cruelty | 162 |
| 11D | Fondling | 141 |
| 210 | Extortion/Blackmail | 136 |
| 23E | Theft From Coin-Operated Machine or Device | 134 |
| 40A | Prostitution | 128 |
| 64A | Human Trafficking, Commercial Sex Acts | 92 |
| 11B | Sodomy | 88 |
| 36B | Statutory Rape | 71 |
| 26G | Hacking/Computer Invasion | 68 |
| 35B | Drug Equipment Violations | 61 |
| 11C | Sexual Assault With An Object | 52 |
| 26C | Impersonation | 51 |
| 09B | Negligent Manslaughter | 16 |
| 26D | Welfare Fraud | 15 |
| 64B | Human Trafficking, Involuntary Servitude | 14 |
| 09C | Justifiable Homicide | 11 |
| 36A | Incest | 10 |
| 510 | Bribery | 6 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 5,304 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:6221 2022-02:5337 2022-03:6181 2022-04:5784 2022-05:6015 2022-06:5549 2022-07:5917 2022-08:5835 2022-09:4938 2022-10:6007 2022-11:5828 2022-12:5411 2023-01:6332 2023-02:5194 2023-03:6320 2023-04:5698 2023-05:5417 2023-06:5111 2023-07:5548 2023-08:5651 2023-09:5523 2023-10:5609 2023-11:5224 2023-12:5111 2024-01:4675 2024-02:4754 2024-03:4934 2024-04:4669 2024-05:4901 2024-06:4788 2024-07:5335 2024-08:5569 2024-09:5413 2024-10:5373 2024-11:4796 2024-12:4934 2025-01:4905 2025-02:4270 2025-03:4695 2025-04:4725 2025-05:5116 2025-06:4960 2025-07:5166 2025-08:5183 2025-09:5273 2025-10:5350 2025-11:4846 2025-12:3606

Use only full calendar years where you can; weight any partial year by its share of the year.