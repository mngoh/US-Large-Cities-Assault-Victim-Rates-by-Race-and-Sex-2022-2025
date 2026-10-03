# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/tulsa.csv

146,741 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 138,767 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 3.7% | 24 |
| offense_id | 0.0% | 0.0% | 145,668 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 141,282 |
| victim_seq_num | 0.0% | 0.0% | 14 |
| victim_type | 0.0% | 0.1% | 9 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 26.2% | 4 |
| race | 0.0% | 3.4% | 7 |
| ethnicity | 0.0% | 100.0% | 1 |
| resident_status | 98.9% | 0.2% | 3 |
| relationship | 65.8% | 0.0% | 121 |
| weapon | 70.8% | 0.1% | 92 |
| injury | 88.7% | 0.0% | 60 |

## Duplicates

5,459 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 22,746 |
| 13C | Intimidation | 13,236 |
| 23H | All Other Larceny | 12,847 |
| 23C | Shoplifting | 12,847 |
| 220 | Burglary/Breaking & Entering | 12,826 |
| 13A | Aggravated Assault | 11,377 |
| 23F | Theft From Motor Vehicle | 9,564 |
| 240 | Motor Vehicle Theft | 9,193 |
| 290 | Destruction/Damage/Vandalism of Property | 6,222 |
| 35A | Drug/Narcotic Violations | 5,012 |
| 26A | False Pretenses/Swindle/Confidence Game | 4,268 |
| 23D | Theft From Building | 3,760 |
| 520 | Weapon Law Violations | 3,620 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,329 |
| 35B | Drug Equipment Violations | 2,195 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,068 |
| 120 | Robbery | 1,878 |
| 26F | Identity Theft | 1,629 |
| 250 | Counterfeiting/Forgery | 1,468 |
| 280 | Stolen Property Offenses | 1,368 |
| 11A | Rape | 1,353 |
| 11D | Criminal Sexual Contact | 573 |
| 270 | Embezzlement | 547 |
| 26E | Wire Fraud | 538 |
| 210 | Extortion/Blackmail | 519 |
| 26C | Impersonation | 414 |
| 100 | Kidnapping/Abduction | 339 |
| 11B | Sodomy | 289 |
| 720 | Animal Cruelty | 236 |
| 11D | Fondling | 226 |
| 200 | Arson | 167 |
| 09A | Murder and Nonnegligent Manslaughter | 159 |
| 26G | Hacking/Computer Invasion | 157 |
| 370 | Pornography/Obscene Material | 125 |
| 23A | Pocket-picking | 104 |
| 11C | Sexual Assault With An Object | 96 |
| 23B | Purse-snatching | 85 |
| 40A | Prostitution | 77 |
| 09B | Negligent Manslaughter | 59 |
| 26D | Welfare Fraud | 50 |
| 09C | Justifiable Homicide | 46 |
| 36B | Statutory Rape | 32 |
| 40B | Assisting or Promoting Prostitution | 27 |
| 40C | Purchasing Prostitution | 24 |
| 64A | Human Trafficking, Commercial Sex Acts | 22 |
| 23E | Theft From Coin-Operated Machine or Device | 15 |
| 36A | Incest | 4 |
| 64B | Human Trafficking, Involuntary Servitude | 3 |
| 510 | Bribery | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 3,041 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:3320 2022-02:2709 2022-03:3221 2022-04:3435 2022-05:3606 2022-06:3315 2022-07:3050 2022-08:3458 2022-09:3210 2022-10:3035 2022-11:2816 2022-12:2920 2023-01:3603 2023-02:2976 2023-03:3031 2023-04:2921 2023-05:3257 2023-06:3458 2023-07:3723 2023-08:3466 2023-09:3142 2023-10:2972 2023-11:2736 2023-12:2990 2024-01:2718 2024-02:2819 2024-03:3226 2024-04:3142 2024-05:3412 2024-06:3167 2024-07:3069 2024-08:3094 2024-09:2974 2024-10:3047 2024-11:2802 2024-12:2798 2025-01:2809 2025-02:2402 2025-03:2887 2025-04:3001 2025-05:3213 2025-06:3101 2025-07:3122 2025-08:2873 2025-09:2839 2025-10:2805 2025-11:2678 2025-12:2373

Use only full calendar years where you can; weight any partial year by its share of the year.