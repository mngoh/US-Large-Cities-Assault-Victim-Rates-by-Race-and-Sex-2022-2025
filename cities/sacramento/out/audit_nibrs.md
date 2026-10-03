# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/sacramento.csv

64,799 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 56,937 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 6.9% | 24 |
| offense_id | 0.0% | 0.0% | 59,984 |
| offense_code | 0.0% | 0.0% | 45 |
| offense_name | 0.0% | 0.0% | 45 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 62,738 |
| victim_seq_num | 0.0% | 0.0% | 106 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 102 |
| age_num | 0.0% | 0.0% | 102 |
| sex | 0.0% | 26.4% | 4 |
| race | 0.0% | 1.8% | 7 |
| ethnicity | 0.0% | 30.0% | 4 |
| resident_status | 25.9% | 3.3% | 3 |
| relationship | 59.3% | 0.0% | 120 |
| weapon | 68.2% | 0.4% | 49 |
| injury | 84.3% | 0.0% | 51 |

## Duplicates

2,061 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 11,045 |
| 23H | All Other Larceny | 8,872 |
| 290 | Destruction/Damage/Vandalism of Property | 6,387 |
| 13A | Aggravated Assault | 5,537 |
| 240 | Motor Vehicle Theft | 5,035 |
| 220 | Burglary/Breaking & Entering | 4,851 |
| 23F | Theft From Motor Vehicle | 4,673 |
| 120 | Robbery | 2,449 |
| 35A | Drug/Narcotic Violations | 2,250 |
| 35B | Drug Equipment Violations | 2,109 |
| 23C | Shoplifting | 2,047 |
| 520 | Weapon Law Violations | 1,757 |
| 13C | Intimidation | 1,634 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,081 |
| 26F | Identity Theft | 799 |
| 26B | Credit Card/Automated Teller Machine Fraud | 635 |
| 280 | Stolen Property Offenses | 482 |
| 200 | Arson | 381 |
| 26A | False Pretenses/Swindle/Confidence Game | 354 |
| 11D | Criminal Sexual Contact | 347 |
| 26C | Impersonation | 322 |
| 100 | Kidnapping/Abduction | 278 |
| 23D | Theft From Building | 275 |
| 11A | Rape | 238 |
| 250 | Counterfeiting/Forgery | 233 |
| 09A | Murder and Nonnegligent Manslaughter | 85 |
| 23B | Purse-snatching | 83 |
| 23A | Pocket-picking | 77 |
| 64A | Human Trafficking, Commercial Sex Acts | 70 |
| 11B | Sodomy | 69 |
| 370 | Pornography/Obscene Material | 58 |
| 270 | Embezzlement | 55 |
| 40A | Prostitution | 42 |
| 11C | Sexual Assault With An Object | 41 |
| 40B | Assisting or Promoting Prostitution | 28 |
| 720 | Animal Cruelty | 28 |
| 210 | Extortion/Blackmail | 27 |
| 36B | Statutory Rape | 25 |
| 23E | Theft From Coin-Operated Machine or Device | 11 |
| 26D | Welfare Fraud | 10 |
| 64B | Human Trafficking, Involuntary Servitude | 9 |
| 26E | Wire Fraud | 4 |
| 26G | Hacking/Computer Invasion | 2 |
| 09C | Justifiable Homicide | 2 |
| 09B | Negligent Manslaughter | 2 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 2,734 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:3030 2024-02:2611 2024-03:2856 2024-04:2739 2024-05:2879 2024-06:2782 2024-07:2729 2024-08:2854 2024-09:2843 2024-10:2815 2024-11:2428 2024-12:2651 2025-01:2725 2025-02:2538 2025-03:2800 2025-04:2615 2025-05:2914 2025-06:2795 2025-07:2701 2025-08:2766 2025-09:2517 2025-10:2476 2025-11:2336 2025-12:2399

Use only full calendar years where you can; weight any partial year by its share of the year.