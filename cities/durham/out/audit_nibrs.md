# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/durham.csv

101,208 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 80,293 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 9.1% | 24 |
| offense_id | 0.0% | 0.0% | 90,146 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 44 |
| victim_id | 0.0% | 0.0% | 93,736 |
| victim_seq_num | 0.0% | 0.0% | 36 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 29.0% | 4 |
| race | 0.0% | 1.6% | 7 |
| ethnicity | 0.0% | 36.9% | 4 |
| resident_status | 34.6% | 0.1% | 3 |
| relationship | 81.3% | 0.0% | 158 |
| weapon | 79.2% | 0.2% | 74 |
| injury | 90.9% | 0.0% | 41 |

## Duplicates

7,472 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 23F | Theft From Motor Vehicle | 15,912 |
| 13B | Simple Assault | 10,410 |
| 23C | Shoplifting | 10,362 |
| 290 | Destruction/Damage/Vandalism of Property | 10,301 |
| 240 | Motor Vehicle Theft | 6,809 |
| 220 | Burglary/Breaking & Entering | 6,216 |
| 23H | All Other Larceny | 5,504 |
| 13A | Aggravated Assault | 4,564 |
| 13C | Intimidation | 3,968 |
| 35A | Drug/Narcotic Violations | 3,713 |
| 26A | False Pretenses/Swindle/Confidence Game | 3,043 |
| 23D | Theft From Building | 2,951 |
| 120 | Robbery | 2,942 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,698 |
| 520 | Weapon Law Violations | 2,396 |
| 35B | Drug Equipment Violations | 1,815 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,427 |
| 26F | Identity Theft | 1,091 |
| 26E | Wire Fraud | 769 |
| 280 | Stolen Property Offenses | 564 |
| 270 | Embezzlement | 482 |
| 11A | Rape | 474 |
| 26C | Impersonation | 348 |
| 11D | Criminal Sexual Contact | 344 |
| 210 | Extortion/Blackmail | 315 |
| 100 | Kidnapping/Abduction | 269 |
| 250 | Counterfeiting/Forgery | 251 |
| 200 | Arson | 223 |
| 370 | Pornography/Obscene Material | 211 |
| 09A | Murder and Nonnegligent Manslaughter | 158 |
| 11B | Sodomy | 155 |
| 11D | Fondling | 108 |
| 26D | Welfare Fraud | 69 |
| 26G | Hacking/Computer Invasion | 62 |
| 23A | Pocket-picking | 51 |
| 11C | Sexual Assault With An Object | 46 |
| 36B | Statutory Rape | 42 |
| 23B | Purse-snatching | 37 |
| 720 | Animal Cruelty | 30 |
| 23E | Theft From Coin-Operated Machine or Device | 25 |
| 09B | Negligent Manslaughter | 14 |
| 09C | Justifiable Homicide | 12 |
| 64A | Human Trafficking, Commercial Sex Acts | 10 |
| 64B | Human Trafficking, Involuntary Servitude | 7 |
| 40A | Prostitution | 3 |
| 40C | Purchasing Prostitution | 3 |
| 36A | Incest | 2 |
| 40B | Assisting or Promoting Prostitution | 1 |
| 510 | Bribery | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,093 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1860 2022-02:1762 2022-03:1981 2022-04:1919 2022-05:1921 2022-06:2226 2022-07:2227 2022-08:2379 2022-09:2103 2022-10:1998 2022-11:1955 2022-12:1913 2023-01:2185 2023-02:1960 2023-03:1983 2023-04:1881 2023-05:2380 2023-06:2338 2023-07:2763 2023-08:2483 2023-09:2231 2023-10:2094 2023-11:2066 2023-12:1975 2024-01:2257 2024-02:1863 2024-03:2090 2024-04:2019 2024-05:2284 2024-06:2225 2024-07:2126 2024-08:2138 2024-09:2255 2024-10:2307 2024-11:2092 2024-12:2188 2025-01:2081 2025-02:1656 2025-03:2142 2025-04:1920 2025-05:2229 2025-06:1999 2025-07:2232 2025-08:2253 2025-09:1985 2025-10:2169 2025-11:2074 2025-12:2041

Use only full calendar years where you can; weight any partial year by its share of the year.