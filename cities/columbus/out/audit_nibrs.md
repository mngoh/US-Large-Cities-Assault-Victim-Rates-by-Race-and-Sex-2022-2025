# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/columbus.csv

273,747 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 220,240 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 8.2% | 24 |
| offense_id | 0.0% | 0.0% | 250,501 |
| offense_code | 0.0% | 0.0% | 45 |
| offense_name | 0.0% | 0.0% | 46 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 246,041 |
| victim_seq_num | 0.0% | 0.0% | 37 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 16.6% | 4 |
| race | 0.0% | 12.4% | 6 |
| ethnicity | 0.0% | 95.8% | 2 |
| resident_status | 100.0% | nan% | 0 |
| relationship | 56.5% | 0.0% | 431 |
| weapon | 86.4% | 1.6% | 66 |
| injury | 94.4% | 0.0% | 7 |

## Duplicates

27,706 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 59,192 |
| 13B | Simple Assault | 40,251 |
| 23F | Theft From Motor Vehicle | 30,653 |
| 23H | All Other Larceny | 25,780 |
| 240 | Motor Vehicle Theft | 24,059 |
| 13C | Intimidation | 21,628 |
| 220 | Burglary/Breaking & Entering | 16,823 |
| 26F | Identity Theft | 11,333 |
| 23C | Shoplifting | 8,309 |
| 13A | Aggravated Assault | 6,530 |
| 520 | Weapon Law Violations | 5,084 |
| 120 | Robbery | 5,034 |
| 11A | Rape | 3,782 |
| 270 | Embezzlement | 2,182 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,018 |
| 23D | Theft From Building | 1,974 |
| 11D | Criminal Sexual Contact | 1,615 |
| 35A | Drug/Narcotic Violations | 1,373 |
| 100 | Kidnapping/Abduction | 666 |
| 280 | Stolen Property Offenses | 546 |
| 35B | Drug Equipment Violations | 515 |
| 11D | Fondling | 475 |
| 370 | Pornography/Obscene Material | 459 |
| 210 | Extortion/Blackmail | 431 |
| 26E | Wire Fraud | 420 |
| 09A | Murder and Nonnegligent Manslaughter | 418 |
| 11B | Sodomy | 395 |
| 26A | False Pretenses/Swindle/Confidence Game | 362 |
| 250 | Counterfeiting/Forgery | 353 |
| 26B | Credit Card/Automated Teller Machine Fraud | 293 |
| 40B | Assisting or Promoting Prostitution | 276 |
| 23B | Purse-snatching | 169 |
| 23A | Pocket-picking | 97 |
| 200 | Arson | 86 |
| 36B | Statutory Rape | 69 |
| 23E | Theft From Coin-Operated Machine or Device | 30 |
| 720 | Animal Cruelty | 18 |
| 26C | Impersonation | 13 |
| 26D | Welfare Fraud | 13 |
| 36A | Incest | 8 |
| 26G | Hacking/Computer Invasion | 4 |
| 39B | Operating/Promoting/Assisting Gambling | 4 |
| 09B | Negligent Manslaughter | 3 |
| 40A | Prostitution | 2 |
| 510 | Bribery | 1 |
| 64A | Human Trafficking, Commercial Sex Acts | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 5,740 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:6115 2022-02:6271 2022-03:7198 2022-04:7152 2022-05:6951 2022-06:6927 2022-07:7501 2022-08:6938 2022-09:6182 2022-10:5809 2022-11:5659 2022-12:5191 2023-01:5885 2023-02:5077 2023-03:5750 2023-04:5893 2023-05:6404 2023-06:6046 2023-07:5439 2023-08:5022 2023-09:4517 2023-10:4343 2023-11:4114 2023-12:3863 2024-01:5790 2024-02:4980 2024-03:5209 2024-04:5278 2024-05:5833 2024-06:4830 2024-07:5140 2024-08:5982 2024-09:5606 2024-10:5975 2024-11:5827 2024-12:6253 2025-01:5466 2025-02:5135 2025-03:5621 2025-04:5462 2025-05:5909 2025-06:5387 2025-07:5923 2025-08:5674 2025-09:5902 2025-10:5731 2025-11:5094 2025-12:5493

Use only full calendar years where you can; weight any partial year by its share of the year.