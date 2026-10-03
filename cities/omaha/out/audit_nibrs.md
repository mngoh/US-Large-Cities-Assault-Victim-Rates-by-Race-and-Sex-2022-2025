# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/omaha.csv

67,046 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 59,706 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 11.1% | 24 |
| offense_id | 0.0% | 0.0% | 64,858 |
| offense_code | 0.0% | 0.0% | 47 |
| offense_name | 0.0% | 0.0% | 47 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 62,670 |
| victim_seq_num | 0.0% | 0.0% | 13 |
| victim_type | 0.0% | 0.1% | 9 |
| age_code | 0.0% | 0.0% | 101 |
| age_num | 0.0% | 0.0% | 101 |
| sex | 0.0% | 27.5% | 4 |
| race | 0.0% | 4.4% | 7 |
| ethnicity | 0.0% | 46.7% | 4 |
| resident_status | 27.3% | 60.2% | 3 |
| relationship | 53.8% | 0.0% | 132 |
| weapon | 77.4% | 4.0% | 55 |
| injury | 99.1% | 0.0% | 6 |

## Duplicates

4,376 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 11,116 |
| 13B | Simple Assault | 10,343 |
| 23C | Shoplifting | 7,897 |
| 23H | All Other Larceny | 6,608 |
| 240 | Motor Vehicle Theft | 5,426 |
| 23F | Theft From Motor Vehicle | 4,622 |
| 13C | Intimidation | 3,468 |
| 13A | Aggravated Assault | 2,589 |
| 220 | Burglary/Breaking & Entering | 2,105 |
| 26A | False Pretenses/Swindle/Confidence Game | 1,967 |
| 35A | Drug/Narcotic Violations | 1,904 |
| 23D | Theft From Building | 1,887 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,354 |
| 35B | Drug Equipment Violations | 886 |
| 26F | Identity Theft | 800 |
| 520 | Weapon Law Violations | 727 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 645 |
| 120 | Robbery | 439 |
| 11A | Rape | 371 |
| 11D | Criminal Sexual Contact | 312 |
| 250 | Counterfeiting/Forgery | 242 |
| 26C | Impersonation | 192 |
| 200 | Arson | 164 |
| 280 | Stolen Property Offenses | 148 |
| 370 | Pornography/Obscene Material | 144 |
| 100 | Kidnapping/Abduction | 123 |
| 26E | Wire Fraud | 102 |
| 270 | Embezzlement | 99 |
| 210 | Extortion/Blackmail | 95 |
| 09A | Murder and Nonnegligent Manslaughter | 45 |
| 23B | Purse-snatching | 44 |
| 11C | Sexual Assault With An Object | 39 |
| 23A | Pocket-picking | 37 |
| 11B | Sodomy | 24 |
| 09B | Negligent Manslaughter | 23 |
| 36B | Statutory Rape | 11 |
| 23E | Theft From Coin-Operated Machine or Device | 11 |
| 09C | Justifiable Homicide | 8 |
| 720 | Animal Cruelty | 8 |
| 26G | Hacking/Computer Invasion | 5 |
| 64A | Human Trafficking, Commercial Sex Acts | 5 |
| 40B | Assisting or Promoting Prostitution | 3 |
| 36A | Incest | 3 |
| 40A | Prostitution | 2 |
| 40C | Purchasing Prostitution | 1 |
| 510 | Bribery | 1 |
| 26D | Welfare Fraud | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 2,814 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:2615 2024-02:3020 2024-03:3098 2024-04:2975 2024-05:2964 2024-06:3023 2024-07:2993 2024-08:2606 2024-09:2803 2024-10:3026 2024-11:2988 2024-12:2788 2025-01:2565 2025-02:2104 2025-03:2709 2025-04:2675 2025-05:2939 2025-06:2729 2025-07:3069 2025-08:2878 2025-09:2824 2025-10:2772 2025-11:2464 2025-12:2419

Use only full calendar years where you can; weight any partial year by its share of the year.