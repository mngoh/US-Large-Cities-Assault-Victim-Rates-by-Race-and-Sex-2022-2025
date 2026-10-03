# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/winston_salem.csv

119,142 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 93,028 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 6.3% | 24 |
| offense_id | 0.0% | 0.0% | 104,560 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 43 |
| victim_id | 0.0% | 0.0% | 109,200 |
| victim_seq_num | 0.0% | 0.0% | 45 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 33.7% | 4 |
| race | 0.0% | 0.5% | 6 |
| ethnicity | 0.0% | 38.2% | 4 |
| resident_status | 33.7% | 0.3% | 3 |
| relationship | 72.0% | 0.0% | 262 |
| weapon | 67.7% | 1.0% | 73 |
| injury | 89.8% | 0.0% | 36 |

## Duplicates

9,942 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 21,595 |
| 290 | Destruction/Damage/Vandalism of Property | 13,516 |
| 520 | Weapon Law Violations | 10,567 |
| 23F | Theft From Motor Vehicle | 8,227 |
| 23H | All Other Larceny | 7,865 |
| 13A | Aggravated Assault | 7,722 |
| 35A | Drug/Narcotic Violations | 7,653 |
| 220 | Burglary/Breaking & Entering | 7,418 |
| 23C | Shoplifting | 7,213 |
| 13C | Intimidation | 6,827 |
| 26A | False Pretenses/Swindle/Confidence Game | 5,463 |
| 240 | Motor Vehicle Theft | 3,918 |
| 35B | Drug Equipment Violations | 3,662 |
| 23D | Theft From Building | 1,432 |
| 120 | Robbery | 1,393 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,084 |
| 26F | Identity Theft | 879 |
| 11A | Rape | 349 |
| 280 | Stolen Property Offenses | 308 |
| 200 | Arson | 299 |
| 250 | Counterfeiting/Forgery | 235 |
| 26B | Credit Card/Automated Teller Machine Fraud | 221 |
| 11D | Criminal Sexual Contact | 206 |
| 100 | Kidnapping/Abduction | 187 |
| 270 | Embezzlement | 175 |
| 09A | Murder and Nonnegligent Manslaughter | 128 |
| 370 | Pornography/Obscene Material | 106 |
| 11D | Fondling | 84 |
| 210 | Extortion/Blackmail | 67 |
| 11B | Sodomy | 62 |
| 720 | Animal Cruelty | 49 |
| 36B | Statutory Rape | 47 |
| 23E | Theft From Coin-Operated Machine or Device | 39 |
| 26C | Impersonation | 31 |
| 40A | Prostitution | 26 |
| 23A | Pocket-picking | 19 |
| 09B | Negligent Manslaughter | 14 |
| 26E | Wire Fraud | 10 |
| 26G | Hacking/Computer Invasion | 9 |
| 23B | Purse-snatching | 9 |
| 09C | Justifiable Homicide | 7 |
| 39A | Betting/Wagering | 6 |
| 40B | Assisting or Promoting Prostitution | 4 |
| 11C | Sexual Assault With An Object | 3 |
| 39B | Operating/Promoting/Assisting Gambling | 2 |
| 40C | Purchasing Prostitution | 2 |
| 64A | Human Trafficking, Commercial Sex Acts | 2 |
| 39C | Gambling Equipment Violation | 1 |
| 36A | Incest | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,448 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:2736 2022-02:2639 2022-03:2913 2022-04:3066 2022-05:3295 2022-06:3081 2022-07:3071 2022-08:3162 2022-09:2921 2022-10:3045 2022-11:2615 2022-12:2430 2023-01:2555 2023-02:2079 2023-03:2294 2023-04:2290 2023-05:2541 2023-06:2452 2023-07:2471 2023-08:2629 2023-09:2292 2023-10:2309 2023-11:1924 2023-12:2213 2024-01:1993 2024-02:1833 2024-03:2129 2024-04:2155 2024-05:2359 2024-06:2470 2024-07:2680 2024-08:2400 2024-09:2306 2024-10:2445 2024-11:2304 2024-12:2555 2025-01:2115 2025-02:2112 2025-03:2426 2025-04:2576 2025-05:2434 2025-06:2490 2025-07:2450 2025-08:2543 2025-09:2463 2025-10:2268 2025-11:2317 2025-12:2296

Use only full calendar years where you can; weight any partial year by its share of the year.