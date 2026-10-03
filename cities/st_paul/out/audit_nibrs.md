# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/st_paul.csv

93,527 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 82,545 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 5.0% | 24 |
| offense_id | 0.0% | 0.0% | 88,689 |
| offense_code | 0.0% | 0.0% | 45 |
| offense_name | 0.0% | 0.0% | 46 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 90,239 |
| victim_seq_num | 0.0% | 0.0% | 29 |
| victim_type | 0.0% | 0.6% | 9 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 25.0% | 4 |
| race | 0.0% | 20.9% | 7 |
| ethnicity | 0.0% | 46.9% | 4 |
| resident_status | 100.0% | nan% | 0 |
| relationship | 77.6% | 0.0% | 117 |
| weapon | 77.5% | 0.5% | 86 |
| injury | 88.7% | 0.0% | 46 |

## Duplicates

3,288 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 11,386 |
| 13B | Simple Assault | 9,257 |
| 240 | Motor Vehicle Theft | 8,373 |
| 23H | All Other Larceny | 8,270 |
| 23F | Theft From Motor Vehicle | 7,049 |
| 220 | Burglary/Breaking & Entering | 6,328 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 5,777 |
| 13A | Aggravated Assault | 5,052 |
| 520 | Weapon Law Violations | 4,479 |
| 280 | Stolen Property Offenses | 3,982 |
| 35A | Drug/Narcotic Violations | 3,643 |
| 13C | Intimidation | 2,630 |
| 23D | Theft From Building | 2,628 |
| 23C | Shoplifting | 2,528 |
| 120 | Robbery | 1,673 |
| 26A | False Pretenses/Swindle/Confidence Game | 1,630 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,601 |
| 26F | Identity Theft | 1,426 |
| 250 | Counterfeiting/Forgery | 932 |
| 200 | Arson | 734 |
| 11A | Rape | 713 |
| 35B | Drug Equipment Violations | 487 |
| 370 | Pornography/Obscene Material | 473 |
| 11D | Criminal Sexual Contact | 450 |
| 26E | Wire Fraud | 379 |
| 26G | Hacking/Computer Invasion | 287 |
| 100 | Kidnapping/Abduction | 224 |
| 23A | Pocket-picking | 180 |
| 23B | Purse-snatching | 160 |
| 26C | Impersonation | 150 |
| 11D | Fondling | 123 |
| 09A | Murder and Nonnegligent Manslaughter | 102 |
| 11C | Sexual Assault With An Object | 79 |
| 11B | Sodomy | 73 |
| 64A | Human Trafficking, Commercial Sex Acts | 67 |
| 210 | Extortion/Blackmail | 66 |
| 720 | Animal Cruelty | 51 |
| 26D | Welfare Fraud | 22 |
| 23E | Theft From Coin-Operated Machine or Device | 21 |
| 270 | Embezzlement | 14 |
| 09B | Negligent Manslaughter | 11 |
| 40C | Purchasing Prostitution | 5 |
| 09C | Justifiable Homicide | 5 |
| 39A | Betting/Wagering | 4 |
| 39B | Operating/Promoting/Assisting Gambling | 2 |
| 40A | Prostitution | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 1,898 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:2234 2022-02:2186 2022-03:2647 2022-04:2440 2022-05:2548 2022-06:2599 2022-07:2743 2022-08:2602 2022-09:2292 2022-10:2280 2022-11:1894 2022-12:1843 2023-01:1933 2023-02:1749 2023-03:1815 2023-04:1913 2023-05:2187 2023-06:2086 2023-07:2156 2023-08:2087 2023-09:1864 2023-10:1880 2023-11:1697 2023-12:1752 2024-01:1819 2024-02:1624 2024-03:1733 2024-04:1783 2024-05:1880 2024-06:1985 2024-07:1941 2024-08:1903 2024-09:1940 2024-10:1836 2024-11:1642 2024-12:1645 2025-01:1470 2025-02:1261 2025-03:1542 2025-04:1512 2025-05:1910 2025-06:1868 2025-07:1927 2025-08:1881 2025-09:1905 2025-10:2004 2025-11:1657 2025-12:1432

Use only full calendar years where you can; weight any partial year by its share of the year.