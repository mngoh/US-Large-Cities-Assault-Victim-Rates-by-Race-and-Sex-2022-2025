# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/lexington.csv

82,390 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 61,562 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 7.8% | 24 |
| offense_id | 0.0% | 0.0% | 76,020 |
| offense_code | 0.0% | 0.0% | 44 |
| offense_name | 0.0% | 0.0% | 45 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 70,806 |
| victim_seq_num | 0.0% | 0.0% | 45 |
| victim_type | 0.0% | 0.1% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 29.0% | 4 |
| race | 0.0% | 3.5% | 7 |
| ethnicity | 0.0% | 33.6% | 4 |
| resident_status | 28.7% | 71.3% | 1 |
| relationship | 62.6% | 0.0% | 205 |
| weapon | 84.7% | 0.4% | 77 |
| injury | 88.5% | 0.0% | 49 |

## Duplicates

11,584 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 12,644 |
| 23H | All Other Larceny | 12,191 |
| 13B | Simple Assault | 7,945 |
| 13C | Intimidation | 7,174 |
| 23F | Theft From Motor Vehicle | 6,666 |
| 23C | Shoplifting | 6,619 |
| 35A | Drug/Narcotic Violations | 5,132 |
| 240 | Motor Vehicle Theft | 4,240 |
| 220 | Burglary/Breaking & Entering | 4,160 |
| 35B | Drug Equipment Violations | 2,732 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,806 |
| 13A | Aggravated Assault | 1,601 |
| 120 | Robbery | 1,215 |
| 280 | Stolen Property Offenses | 1,210 |
| 26F | Identity Theft | 1,022 |
| 520 | Weapon Law Violations | 924 |
| 250 | Counterfeiting/Forgery | 831 |
| 270 | Embezzlement | 628 |
| 11A | Rape | 537 |
| 100 | Kidnapping/Abduction | 520 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 494 |
| 11D | Criminal Sexual Contact | 433 |
| 370 | Pornography/Obscene Material | 320 |
| 26A | False Pretenses/Swindle/Confidence Game | 283 |
| 11B | Sodomy | 254 |
| 11D | Fondling | 147 |
| 210 | Extortion/Blackmail | 117 |
| 200 | Arson | 86 |
| 09A | Murder and Nonnegligent Manslaughter | 77 |
| 26G | Hacking/Computer Invasion | 70 |
| 26C | Impersonation | 57 |
| 40A | Prostitution | 43 |
| 36B | Statutory Rape | 39 |
| 23A | Pocket-picking | 37 |
| 23D | Theft From Building | 33 |
| 23B | Purse-snatching | 31 |
| 720 | Animal Cruelty | 20 |
| 64A | Human Trafficking, Commercial Sex Acts | 15 |
| 510 | Bribery | 13 |
| 64B | Human Trafficking, Involuntary Servitude | 9 |
| 40B | Assisting or Promoting Prostitution | 7 |
| 23E | Theft From Coin-Operated Machine or Device | 5 |
| 36A | Incest | 1 |
| 39B | Operating/Promoting/Assisting Gambling | 1 |
| 39C | Gambling Equipment Violation | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 1,721 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1725 2022-02:1170 2022-03:1837 2022-04:1911 2022-05:2021 2022-06:1867 2022-07:2004 2022-08:2021 2022-09:1995 2022-10:1829 2022-11:1705 2022-12:1796 2023-01:1858 2023-02:1925 2023-03:1905 2023-04:1876 2023-05:1905 2023-06:1871 2023-07:2125 2023-08:1899 2023-09:1695 2023-10:1822 2023-11:1582 2023-12:1783 2024-01:1510 2024-02:1455 2024-03:1779 2024-04:1537 2024-05:1800 2024-06:1691 2024-07:1802 2024-08:1647 2024-09:1717 2024-10:1690 2024-11:1737 2024-12:1512 2025-01:1360 2025-02:1325 2025-03:1436 2025-04:1433 2025-05:1632 2025-06:1664 2025-07:1686 2025-08:1648 2025-09:1663 2025-10:1583 2025-11:1511 2025-12:1445

Use only full calendar years where you can; weight any partial year by its share of the year.