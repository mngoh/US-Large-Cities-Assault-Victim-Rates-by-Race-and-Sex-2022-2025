# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/virginia_beach.csv

41,545 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 35,086 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 12.6% | 24 |
| offense_id | 0.0% | 0.0% | 38,769 |
| offense_code | 0.0% | 0.0% | 46 |
| offense_name | 0.0% | 0.0% | 46 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 38,645 |
| victim_seq_num | 0.0% | 0.0% | 11 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 102 |
| age_num | 0.0% | 0.0% | 102 |
| sex | 0.0% | 33.9% | 4 |
| race | 0.0% | 3.7% | 7 |
| ethnicity | 0.0% | 55.9% | 4 |
| resident_status | 82.6% | 0.3% | 3 |
| relationship | 64.0% | 0.0% | 188 |
| weapon | 74.8% | 0.3% | 63 |
| injury | 90.8% | 0.0% | 37 |

## Duplicates

2,900 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 8,974 |
| 290 | Destruction/Damage/Vandalism of Property | 5,506 |
| 23C | Shoplifting | 4,801 |
| 23H | All Other Larceny | 3,803 |
| 23F | Theft From Motor Vehicle | 2,955 |
| 35A | Drug/Narcotic Violations | 2,396 |
| 520 | Weapon Law Violations | 1,886 |
| 26A | False Pretenses/Swindle/Confidence Game | 1,440 |
| 13C | Intimidation | 1,175 |
| 240 | Motor Vehicle Theft | 981 |
| 26F | Identity Theft | 937 |
| 23D | Theft From Building | 883 |
| 35B | Drug Equipment Violations | 820 |
| 220 | Burglary/Breaking & Entering | 809 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 568 |
| 720 | Animal Cruelty | 495 |
| 26B | Credit Card/Automated Teller Machine Fraud | 454 |
| 270 | Embezzlement | 440 |
| 13A | Aggravated Assault | 395 |
| 120 | Robbery | 366 |
| 250 | Counterfeiting/Forgery | 361 |
| 370 | Pornography/Obscene Material | 173 |
| 210 | Extortion/Blackmail | 139 |
| 280 | Stolen Property Offenses | 128 |
| 100 | Kidnapping/Abduction | 115 |
| 40A | Prostitution | 84 |
| 11A | Rape | 83 |
| 200 | Arson | 81 |
| 11D | Criminal Sexual Contact | 46 |
| 11B | Sodomy | 39 |
| 23B | Purse-snatching | 39 |
| 11C | Sexual Assault With An Object | 39 |
| 26G | Hacking/Computer Invasion | 29 |
| 09A | Murder and Nonnegligent Manslaughter | 28 |
| 23A | Pocket-picking | 24 |
| 36B | Statutory Rape | 8 |
| 09B | Negligent Manslaughter | 7 |
| 26E | Wire Fraud | 6 |
| 26C | Impersonation | 6 |
| 510 | Bribery | 6 |
| 23E | Theft From Coin-Operated Machine or Device | 5 |
| 40C | Purchasing Prostitution | 4 |
| 09C | Justifiable Homicide | 4 |
| 40B | Assisting or Promoting Prostitution | 3 |
| 64A | Human Trafficking, Commercial Sex Acts | 3 |
| 64B | Human Trafficking, Involuntary Servitude | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 1,749 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:1752 2024-02:1630 2024-03:1758 2024-04:1714 2024-05:1933 2024-06:1888 2024-07:1897 2024-08:1746 2024-09:1803 2024-10:1945 2024-11:1648 2024-12:1726 2025-01:1677 2025-02:1458 2025-03:1805 2025-04:1804 2025-05:1880 2025-06:1673 2025-07:1774 2025-08:1768 2025-09:1696 2025-10:1584 2025-11:1576 2025-12:1410

Use only full calendar years where you can; weight any partial year by its share of the year.