# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/tucson.csv

84,331 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 65,190 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 6.7% | 24 |
| offense_id | 0.0% | 0.0% | 77,859 |
| offense_code | 0.0% | 0.0% | 44 |
| offense_name | 0.0% | 0.0% | 44 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 75,184 |
| victim_seq_num | 0.0% | 0.0% | 16 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 46.6% | 4 |
| race | 0.0% | 9.6% | 7 |
| ethnicity | 0.0% | 65.2% | 4 |
| resident_status | 48.7% | 4.9% | 3 |
| relationship | 70.0% | 0.0% | 235 |
| weapon | 80.6% | 0.3% | 138 |
| injury | 91.2% | 0.0% | 56 |

## Duplicates

9,147 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 23C | Shoplifting | 14,088 |
| 290 | Destruction/Damage/Vandalism of Property | 12,980 |
| 35B | Drug Equipment Violations | 11,212 |
| 13B | Simple Assault | 10,837 |
| 35A | Drug/Narcotic Violations | 5,613 |
| 240 | Motor Vehicle Theft | 4,282 |
| 13A | Aggravated Assault | 4,020 |
| 23F | Theft From Motor Vehicle | 3,989 |
| 23H | All Other Larceny | 3,462 |
| 220 | Burglary/Breaking & Entering | 2,685 |
| 13C | Intimidation | 2,109 |
| 23D | Theft From Building | 1,652 |
| 520 | Weapon Law Violations | 1,608 |
| 120 | Robbery | 1,272 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 948 |
| 26A | False Pretenses/Swindle/Confidence Game | 660 |
| 26F | Identity Theft | 376 |
| 270 | Embezzlement | 372 |
| 26B | Credit Card/Automated Teller Machine Fraud | 337 |
| 11A | Rape | 328 |
| 11D | Criminal Sexual Contact | 294 |
| 100 | Kidnapping/Abduction | 240 |
| 200 | Arson | 222 |
| 250 | Counterfeiting/Forgery | 141 |
| 09A | Murder and Nonnegligent Manslaughter | 75 |
| 720 | Animal Cruelty | 74 |
| 370 | Pornography/Obscene Material | 72 |
| 280 | Stolen Property Offenses | 62 |
| 210 | Extortion/Blackmail | 55 |
| 26E | Wire Fraud | 44 |
| 26G | Hacking/Computer Invasion | 35 |
| 23B | Purse-snatching | 28 |
| 23A | Pocket-picking | 27 |
| 64A | Human Trafficking, Commercial Sex Acts | 24 |
| 36B | Statutory Rape | 24 |
| 23E | Theft From Coin-Operated Machine or Device | 21 |
| 40A | Prostitution | 17 |
| 11B | Sodomy | 17 |
| 09B | Negligent Manslaughter | 11 |
| 11C | Sexual Assault With An Object | 7 |
| 36A | Incest | 4 |
| 26D | Welfare Fraud | 4 |
| 40C | Purchasing Prostitution | 2 |
| 64B | Human Trafficking, Involuntary Servitude | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 3,131 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- 2024-12: 1,736

Full series:

2024-01:4425 2024-02:4425 2024-03:4442 2024-04:4859 2024-05:5390 2024-06:5093 2024-07:4747 2024-08:4447 2024-09:3843 2024-10:3441 2024-11:3106 2024-12:1736 2025-01:2943 2025-02:2688 2025-03:3136 2025-04:2829 2025-05:2821 2025-06:2715 2025-07:3126 2025-08:3148 2025-09:2718 2025-10:2955 2025-11:2639 2025-12:2659

Use only full calendar years where you can; weight any partial year by its share of the year.