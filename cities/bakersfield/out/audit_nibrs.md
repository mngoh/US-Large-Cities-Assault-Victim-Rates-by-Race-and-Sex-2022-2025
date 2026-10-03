# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/bakersfield.csv

46,422 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 40,777 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 8.7% | 24 |
| offense_id | 0.0% | 0.0% | 43,315 |
| offense_code | 0.0% | 0.0% | 46 |
| offense_name | 0.0% | 0.0% | 46 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 44,779 |
| victim_seq_num | 0.0% | 0.0% | 23 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 102 |
| age_num | 0.0% | 0.0% | 102 |
| sex | 0.0% | 29.7% | 4 |
| race | 0.0% | 0.7% | 7 |
| ethnicity | 0.0% | 31.9% | 4 |
| resident_status | 29.6% | 0.5% | 3 |
| relationship | 55.7% | 0.0% | 139 |
| weapon | 76.3% | 0.4% | 34 |
| injury | 88.0% | 0.0% | 46 |

## Duplicates

1,643 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 6,742 |
| 240 | Motor Vehicle Theft | 4,905 |
| 23C | Shoplifting | 4,301 |
| 220 | Burglary/Breaking & Entering | 4,292 |
| 290 | Destruction/Damage/Vandalism of Property | 4,140 |
| 13A | Aggravated Assault | 3,066 |
| 23F | Theft From Motor Vehicle | 3,001 |
| 23H | All Other Larceny | 2,602 |
| 35A | Drug/Narcotic Violations | 2,018 |
| 13C | Intimidation | 1,512 |
| 35B | Drug Equipment Violations | 1,335 |
| 120 | Robbery | 1,240 |
| 520 | Weapon Law Violations | 1,075 |
| 26A | False Pretenses/Swindle/Confidence Game | 1,025 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 774 |
| 23D | Theft From Building | 590 |
| 26F | Identity Theft | 501 |
| 250 | Counterfeiting/Forgery | 475 |
| 26B | Credit Card/Automated Teller Machine Fraud | 470 |
| 11D | Criminal Sexual Contact | 360 |
| 280 | Stolen Property Offenses | 344 |
| 26C | Impersonation | 254 |
| 23A | Pocket-picking | 242 |
| 11A | Rape | 175 |
| 100 | Kidnapping/Abduction | 154 |
| 270 | Embezzlement | 103 |
| 720 | Animal Cruelty | 95 |
| 370 | Pornography/Obscene Material | 86 |
| 11B | Sodomy | 78 |
| 40A | Prostitution | 74 |
| 09A | Murder and Nonnegligent Manslaughter | 61 |
| 23B | Purse-snatching | 59 |
| 36B | Statutory Rape | 59 |
| 40B | Assisting or Promoting Prostitution | 38 |
| 26E | Wire Fraud | 29 |
| 200 | Arson | 25 |
| 11C | Sexual Assault With An Object | 25 |
| 64A | Human Trafficking, Commercial Sex Acts | 22 |
| 210 | Extortion/Blackmail | 20 |
| 09B | Negligent Manslaughter | 18 |
| 64B | Human Trafficking, Involuntary Servitude | 17 |
| 23E | Theft From Coin-Operated Machine or Device | 11 |
| 40C | Purchasing Prostitution | 3 |
| 39B | Operating/Promoting/Assisting Gambling | 2 |
| 39C | Gambling Equipment Violation | 2 |
| 09C | Justifiable Homicide | 2 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 1,924 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:2437 2024-02:2034 2024-03:2040 2024-04:1929 2024-05:2083 2024-06:1897 2024-07:1822 2024-08:1912 2024-09:1813 2024-10:1863 2024-11:1827 2024-12:2021 2025-01:1954 2025-02:1701 2025-03:1937 2025-04:1941 2025-05:2018 2025-06:1828 2025-07:1920 2025-08:2007 2025-09:1941 2025-10:1892 2025-11:1768 2025-12:1837

Use only full calendar years where you can; weight any partial year by its share of the year.