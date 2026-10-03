# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/louisville.csv

109,821 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 89,994 |
| incident_date | 0.0% | 0.0% | 730 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 8.5% | 24 |
| offense_id | 0.0% | 0.0% | 102,583 |
| offense_code | 0.0% | 0.0% | 43 |
| offense_name | 0.0% | 0.0% | 43 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 99,696 |
| victim_seq_num | 0.0% | 0.0% | 28 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 23.3% | 4 |
| race | 0.0% | 1.4% | 7 |
| ethnicity | 0.0% | 27.9% | 4 |
| resident_status | 34.7% | 2.2% | 3 |
| relationship | 59.3% | 0.0% | 140 |
| weapon | 77.4% | 0.6% | 76 |
| injury | 87.7% | 0.0% | 41 |

## Duplicates

10,125 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 12,988 |
| 23H | All Other Larceny | 12,590 |
| 13B | Simple Assault | 12,232 |
| 240 | Motor Vehicle Theft | 10,422 |
| 23F | Theft From Motor Vehicle | 9,088 |
| 13C | Intimidation | 7,707 |
| 13A | Aggravated Assault | 7,267 |
| 23C | Shoplifting | 6,860 |
| 220 | Burglary/Breaking & Entering | 6,788 |
| 35A | Drug/Narcotic Violations | 4,051 |
| 23D | Theft From Building | 2,551 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,457 |
| 120 | Robbery | 2,159 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,117 |
| 35B | Drug Equipment Violations | 1,929 |
| 520 | Weapon Law Violations | 1,486 |
| 26C | Impersonation | 1,317 |
| 280 | Stolen Property Offenses | 1,174 |
| 250 | Counterfeiting/Forgery | 1,049 |
| 26A | False Pretenses/Swindle/Confidence Game | 777 |
| 100 | Kidnapping/Abduction | 527 |
| 270 | Embezzlement | 397 |
| 11A | Rape | 369 |
| 11D | Criminal Sexual Contact | 327 |
| 200 | Arson | 280 |
| 370 | Pornography/Obscene Material | 173 |
| 09A | Murder and Nonnegligent Manslaughter | 168 |
| 23A | Pocket-picking | 135 |
| 11B | Sodomy | 105 |
| 210 | Extortion/Blackmail | 92 |
| 720 | Animal Cruelty | 56 |
| 23E | Theft From Coin-Operated Machine or Device | 49 |
| 36B | Statutory Rape | 33 |
| 26G | Hacking/Computer Invasion | 26 |
| 64B | Human Trafficking, Involuntary Servitude | 26 |
| 23B | Purse-snatching | 19 |
| 09B | Negligent Manslaughter | 9 |
| 510 | Bribery | 6 |
| 09C | Justifiable Homicide | 6 |
| 36A | Incest | 4 |
| 40A | Prostitution | 3 |
| 26F | Identity Theft | 1 |
| 64A | Human Trafficking, Commercial Sex Acts | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 4,586 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:4355 2024-02:4088 2024-03:4408 2024-04:4432 2024-05:5071 2024-06:4951 2024-07:5213 2024-08:4856 2024-09:4219 2024-10:4260 2024-11:4173 2024-12:3083 2025-01:4007 2025-02:3813 2025-03:4611 2025-04:4678 2025-05:5191 2025-06:5100 2025-07:5465 2025-08:5379 2025-09:4804 2025-10:4560 2025-11:4814 2025-12:4290

Use only full calendar years where you can; weight any partial year by its share of the year.