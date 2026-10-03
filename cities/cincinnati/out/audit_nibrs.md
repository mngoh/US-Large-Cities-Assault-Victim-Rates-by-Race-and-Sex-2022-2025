# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/cincinnati.csv

106,530 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 90,932 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 10.1% | 24 |
| offense_id | 0.0% | 0.0% | 95,639 |
| offense_code | 0.0% | 0.0% | 34 |
| offense_name | 0.0% | 0.0% | 35 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 103,224 |
| victim_seq_num | 0.0% | 0.0% | 39 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 14.7% | 4 |
| race | 0.0% | 4.1% | 7 |
| ethnicity | 0.0% | 65.3% | 4 |
| resident_status | 100.0% | nan% | 0 |
| relationship | 52.4% | 0.0% | 199 |
| weapon | 75.5% | 0.5% | 70 |
| injury | 84.1% | 0.0% | 7 |

## Duplicates

3,306 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 17,586 |
| 13B | Simple Assault | 15,629 |
| 23F | Theft From Motor Vehicle | 14,231 |
| 240 | Motor Vehicle Theft | 11,104 |
| 23H | All Other Larceny | 8,897 |
| 220 | Burglary/Breaking & Entering | 8,041 |
| 13A | Aggravated Assault | 6,334 |
| 23C | Shoplifting | 5,651 |
| 13C | Intimidation | 4,485 |
| 120 | Robbery | 3,220 |
| 23D | Theft From Building | 3,153 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,137 |
| 26F | Identity Theft | 1,516 |
| 250 | Counterfeiting/Forgery | 805 |
| 11A | Rape | 752 |
| 520 | Weapon Law Violations | 718 |
| 26E | Wire Fraud | 322 |
| 26B | Credit Card/Automated Teller Machine Fraud | 316 |
| 11D | Criminal Sexual Contact | 282 |
| 100 | Kidnapping/Abduction | 282 |
| 09A | Murder and Nonnegligent Manslaughter | 275 |
| 23A | Pocket-picking | 194 |
| 23B | Purse-snatching | 133 |
| 210 | Extortion/Blackmail | 116 |
| 11D | Fondling | 93 |
| 11B | Sodomy | 58 |
| 23E | Theft From Coin-Operated Machine or Device | 51 |
| 26A | False Pretenses/Swindle/Confidence Game | 48 |
| 270 | Embezzlement | 32 |
| 36B | Statutory Rape | 29 |
| 09B | Negligent Manslaughter | 18 |
| 370 | Pornography/Obscene Material | 16 |
| 26C | Impersonation | 3 |
| 36A | Incest | 2 |
| 200 | Arson | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,225 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1745 2022-02:1736 2022-03:1962 2022-04:2049 2022-05:2266 2022-06:2505 2022-07:2673 2022-08:2518 2022-09:2314 2022-10:2302 2022-11:2051 2022-12:1929 2023-01:2084 2023-02:2147 2023-03:2173 2023-04:2219 2023-05:2620 2023-06:2296 2023-07:2760 2023-08:2342 2023-09:2104 2023-10:2715 2023-11:2271 2023-12:2100 2024-01:2198 2024-02:1996 2024-03:1979 2024-04:2116 2024-05:2269 2024-06:2371 2024-07:2594 2024-08:2373 2024-09:2283 2024-10:2534 2024-11:2367 2024-12:2079 2025-01:1776 2025-02:1640 2025-03:1906 2025-04:1777 2025-05:2200 2025-06:2483 2025-07:2422 2025-08:2231 2025-09:2504 2025-10:2585 2025-11:1964 2025-12:2002

Use only full calendar years where you can; weight any partial year by its share of the year.