# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/new_york.csv

1,151,266 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 1,021,327 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.4% | 3.6% | 24 |
| offense_id | 0.0% | 0.0% | 1,130,901 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 48 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 37 |
| victim_id | 0.0% | 0.0% | 1,069,144 |
| victim_seq_num | 0.0% | 0.0% | 23 |
| victim_type | 0.0% | 0.0% | 7 |
| age_code | 0.0% | 0.0% | 101 |
| age_num | 0.0% | 0.0% | 101 |
| sex | 0.0% | 27.6% | 4 |
| race | 0.0% | 8.3% | 6 |
| ethnicity | 0.0% | 32.7% | 4 |
| resident_status | 27.6% | 72.4% | 1 |
| relationship | 31.9% | 0.0% | 165 |
| weapon | 74.7% | 0.2% | 108 |
| injury | 84.0% | 0.0% | 7 |

## Duplicates

82,122 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13C | Intimidation | 227,768 |
| 13B | Simple Assault | 143,390 |
| 23H | All Other Larceny | 126,641 |
| 23C | Shoplifting | 112,250 |
| 290 | Destruction/Damage/Vandalism of Property | 101,413 |
| 13A | Aggravated Assault | 75,201 |
| 35A | Drug/Narcotic Violations | 47,979 |
| 23D | Theft From Building | 46,934 |
| 120 | Robbery | 37,189 |
| 520 | Weapon Law Violations | 33,708 |
| 240 | Motor Vehicle Theft | 32,489 |
| 220 | Burglary/Breaking & Entering | 28,035 |
| 280 | Stolen Property Offenses | 27,137 |
| 23F | Theft From Motor Vehicle | 24,026 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 23,838 |
| 250 | Counterfeiting/Forgery | 20,601 |
| 26F | Identity Theft | 7,277 |
| 11D | Criminal Sexual Contact | 6,567 |
| 11A | Rape | 4,812 |
| 23A | Pocket-picking | 4,666 |
| 210 | Extortion/Blackmail | 2,857 |
| 270 | Embezzlement | 2,632 |
| 100 | Kidnapping/Abduction | 1,698 |
| 370 | Pornography/Obscene Material | 1,631 |
| 200 | Arson | 1,548 |
| 35B | Drug Equipment Violations | 1,490 |
| 23B | Purse-snatching | 1,488 |
| 23E | Theft From Coin-Operated Machine or Device | 1,086 |
| 39B | Operating/Promoting/Assisting Gambling | 644 |
| 26A | False Pretenses/Swindle/Confidence Game | 643 |
| 09A | Murder and Nonnegligent Manslaughter | 605 |
| 11B | Sodomy | 552 |
| 39C | Gambling Equipment Violation | 533 |
| 26C | Impersonation | 518 |
| 40A | Prostitution | 401 |
| 36B | Statutory Rape | 224 |
| 26B | Credit Card/Automated Teller Machine Fraud | 198 |
| 510 | Bribery | 134 |
| 40B | Assisting or Promoting Prostitution | 104 |
| 11C | Sexual Assault With An Object | 101 |
| 64A | Human Trafficking, Commercial Sex Acts | 63 |
| 720 | Animal Cruelty | 55 |
| 09B | Negligent Manslaughter | 51 |
| 26G | Hacking/Computer Invasion | 41 |
| 26D | Welfare Fraud | 40 |
| 09C | Justifiable Homicide | 4 |
| 36A | Incest | 3 |
| 64B | Human Trafficking, Involuntary Servitude | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 48,550 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:47370 2024-02:44554 2024-03:47561 2024-04:46856 2024-05:51274 2024-06:50246 2024-07:51483 2024-08:50360 2024-09:48803 2024-10:50397 2024-11:46912 2024-12:43830 2025-01:46407 2025-02:42421 2025-03:48928 2025-04:48571 2025-05:51357 2025-06:49274 2025-07:50813 2025-08:49352 2025-09:48528 2025-10:48469 2025-11:45374 2025-12:42126

Use only full calendar years where you can; weight any partial year by its share of the year.