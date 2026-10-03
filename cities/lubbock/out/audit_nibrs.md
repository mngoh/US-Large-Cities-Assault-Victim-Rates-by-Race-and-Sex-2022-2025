# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/lubbock.csv

107,129 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 82,476 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 8.7% | 5.7% | 24 |
| offense_id | 0.0% | 0.0% | 94,991 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 98,359 |
| victim_seq_num | 0.0% | 0.0% | 140 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 28.9% | 4 |
| race | 0.0% | 1.7% | 7 |
| ethnicity | 0.0% | 31.0% | 4 |
| resident_status | 28.3% | 3.4% | 3 |
| relationship | 48.6% | 0.0% | 200 |
| weapon | 72.5% | 0.2% | 80 |
| injury | 86.1% | 0.0% | 45 |

## Duplicates

8,770 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 17,035 |
| 290 | Destruction/Damage/Vandalism of Property | 11,020 |
| 23F | Theft From Motor Vehicle | 9,744 |
| 220 | Burglary/Breaking & Entering | 7,871 |
| 13A | Aggravated Assault | 6,949 |
| 35A | Drug/Narcotic Violations | 5,963 |
| 23H | All Other Larceny | 5,858 |
| 23C | Shoplifting | 5,402 |
| 26A | False Pretenses/Swindle/Confidence Game | 4,314 |
| 13C | Intimidation | 4,274 |
| 23D | Theft From Building | 3,935 |
| 240 | Motor Vehicle Theft | 3,780 |
| 35B | Drug Equipment Violations | 3,235 |
| 250 | Counterfeiting/Forgery | 2,075 |
| 520 | Weapon Law Violations | 1,950 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,830 |
| 26F | Identity Theft | 1,828 |
| 120 | Robbery | 1,737 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,526 |
| 280 | Stolen Property Offenses | 1,511 |
| 26E | Wire Fraud | 843 |
| 11A | Rape | 679 |
| 370 | Pornography/Obscene Material | 485 |
| 270 | Embezzlement | 479 |
| 11D | Criminal Sexual Contact | 325 |
| 200 | Arson | 319 |
| 210 | Extortion/Blackmail | 268 |
| 26G | Hacking/Computer Invasion | 258 |
| 11B | Sodomy | 223 |
| 40C | Purchasing Prostitution | 220 |
| 100 | Kidnapping/Abduction | 184 |
| 40A | Prostitution | 168 |
| 26C | Impersonation | 158 |
| 11D | Fondling | 122 |
| 720 | Animal Cruelty | 106 |
| 11C | Sexual Assault With An Object | 102 |
| 23E | Theft From Coin-Operated Machine or Device | 91 |
| 09A | Murder and Nonnegligent Manslaughter | 66 |
| 23A | Pocket-picking | 60 |
| 23B | Purse-snatching | 21 |
| 09B | Negligent Manslaughter | 20 |
| 09C | Justifiable Homicide | 18 |
| 26D | Welfare Fraud | 16 |
| 510 | Bribery | 16 |
| 64A | Human Trafficking, Commercial Sex Acts | 15 |
| 40B | Assisting or Promoting Prostitution | 14 |
| 39B | Operating/Promoting/Assisting Gambling | 12 |
| 39C | Gambling Equipment Violation | 2 |
| 64B | Human Trafficking, Involuntary Servitude | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,180 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:2268 2022-02:2562 2022-03:2783 2022-04:2848 2022-05:2928 2022-06:2704 2022-07:2780 2022-08:2806 2022-09:2850 2022-10:2940 2022-11:2437 2022-12:2434 2023-01:2413 2023-02:2188 2023-03:2436 2023-04:2371 2023-05:2448 2023-06:2465 2023-07:2559 2023-08:2458 2023-09:2293 2023-10:2173 2023-11:2044 2023-12:2130 2024-01:1973 2024-02:2032 2024-03:2162 2024-04:2113 2024-05:2218 2024-06:2273 2024-07:2301 2024-08:2117 2024-09:1955 2024-10:2034 2024-11:1743 2024-12:1701 2025-01:1860 2025-02:1788 2025-03:1955 2025-04:1823 2025-05:2056 2025-06:1659 2025-07:2036 2025-08:1820 2025-09:1844 2025-10:1801 2025-11:1881 2025-12:1666

Use only full calendar years where you can; weight any partial year by its share of the year.