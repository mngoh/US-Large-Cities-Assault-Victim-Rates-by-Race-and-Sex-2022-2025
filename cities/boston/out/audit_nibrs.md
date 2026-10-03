# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/boston.csv

86,803 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 71,936 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 9.7% | 24 |
| offense_id | 0.0% | 0.0% | 78,744 |
| offense_code | 0.0% | 0.0% | 45 |
| offense_name | 0.0% | 0.0% | 45 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 81,702 |
| victim_seq_num | 0.0% | 0.0% | 33 |
| victim_type | 0.0% | 0.3% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 23.3% | 4 |
| race | 0.0% | 17.3% | 7 |
| ethnicity | 0.0% | 56.3% | 4 |
| resident_status | 30.0% | 10.8% | 3 |
| relationship | 55.1% | 0.0% | 199 |
| weapon | 76.4% | 0.9% | 75 |
| injury | 87.8% | 0.0% | 30 |

## Duplicates

5,101 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 14,650 |
| 13C | Intimidation | 9,740 |
| 290 | Destruction/Damage/Vandalism of Property | 9,403 |
| 23C | Shoplifting | 8,732 |
| 13A | Aggravated Assault | 6,135 |
| 35A | Drug/Narcotic Violations | 5,426 |
| 23H | All Other Larceny | 5,188 |
| 23D | Theft From Building | 4,491 |
| 23F | Theft From Motor Vehicle | 4,438 |
| 220 | Burglary/Breaking & Entering | 2,796 |
| 26A | False Pretenses/Swindle/Confidence Game | 2,606 |
| 120 | Robbery | 2,039 |
| 240 | Motor Vehicle Theft | 1,791 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,709 |
| 26F | Identity Theft | 1,315 |
| 520 | Weapon Law Violations | 970 |
| 250 | Counterfeiting/Forgery | 822 |
| 280 | Stolen Property Offenses | 779 |
| 26E | Wire Fraud | 627 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 554 |
| 11D | Criminal Sexual Contact | 366 |
| 210 | Extortion/Blackmail | 351 |
| 370 | Pornography/Obscene Material | 263 |
| 11A | Rape | 242 |
| 26C | Impersonation | 207 |
| 23A | Pocket-picking | 162 |
| 26G | Hacking/Computer Invasion | 114 |
| 100 | Kidnapping/Abduction | 113 |
| 270 | Embezzlement | 113 |
| 35B | Drug Equipment Violations | 106 |
| 26D | Welfare Fraud | 86 |
| 720 | Animal Cruelty | 83 |
| 200 | Arson | 72 |
| 40A | Prostitution | 71 |
| 11B | Sodomy | 68 |
| 09A | Murder and Nonnegligent Manslaughter | 48 |
| 23B | Purse-snatching | 44 |
| 64A | Human Trafficking, Commercial Sex Acts | 32 |
| 11C | Sexual Assault With An Object | 29 |
| 36B | Statutory Rape | 13 |
| 40B | Assisting or Promoting Prostitution | 3 |
| 09B | Negligent Manslaughter | 2 |
| 23E | Theft From Coin-Operated Machine or Device | 2 |
| 510 | Bribery | 1 |
| 64B | Human Trafficking, Involuntary Servitude | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 3,634 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:3338 2024-02:3418 2024-03:3631 2024-04:3446 2024-05:3929 2024-06:3921 2024-07:3980 2024-08:4165 2024-09:3945 2024-10:3801 2024-11:3566 2024-12:3230 2025-01:3355 2025-02:2978 2025-03:3315 2025-04:3289 2025-05:3849 2025-06:3636 2025-07:3952 2025-08:4057 2025-09:4006 2025-10:3659 2025-11:3245 2025-12:3092

Use only full calendar years where you can; weight any partial year by its share of the year.