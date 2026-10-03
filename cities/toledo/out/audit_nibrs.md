# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/toledo.csv

114,593 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 86,783 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 6.8% | 24 |
| offense_id | 0.0% | 0.0% | 100,075 |
| offense_code | 0.0% | 0.0% | 41 |
| offense_name | 0.0% | 0.0% | 42 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 41 |
| victim_id | 0.0% | 0.0% | 105,847 |
| victim_seq_num | 0.0% | 0.0% | 20 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 81 |
| age_num | 0.0% | 0.0% | 81 |
| sex | 0.0% | 21.7% | 4 |
| race | 0.0% | 3.1% | 6 |
| ethnicity | 0.0% | 98.5% | 2 |
| resident_status | 100.0% | nan% | 0 |
| relationship | 20.7% | 0.0% | 307 |
| weapon | 57.8% | 5.6% | 70 |
| injury | 88.7% | 0.0% | 7 |

## Duplicates

8,746 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 34,966 |
| 13C | Intimidation | 14,043 |
| 23H | All Other Larceny | 11,119 |
| 13A | Aggravated Assault | 8,637 |
| 290 | Destruction/Damage/Vandalism of Property | 6,563 |
| 220 | Burglary/Breaking & Entering | 6,179 |
| 23C | Shoplifting | 6,045 |
| 35A | Drug/Narcotic Violations | 5,854 |
| 240 | Motor Vehicle Theft | 4,771 |
| 520 | Weapon Law Violations | 2,919 |
| 35B | Drug Equipment Violations | 2,793 |
| 120 | Robbery | 1,890 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,822 |
| 23F | Theft From Motor Vehicle | 1,726 |
| 11A | Rape | 971 |
| 280 | Stolen Property Offenses | 954 |
| 23D | Theft From Building | 586 |
| 200 | Arson | 534 |
| 26A | False Pretenses/Swindle/Confidence Game | 464 |
| 26F | Identity Theft | 428 |
| 100 | Kidnapping/Abduction | 258 |
| 250 | Counterfeiting/Forgery | 240 |
| 09A | Murder and Nonnegligent Manslaughter | 146 |
| 26B | Credit Card/Automated Teller Machine Fraud | 121 |
| 720 | Animal Cruelty | 96 |
| 11D | Criminal Sexual Contact | 77 |
| 11B | Sodomy | 69 |
| 40B | Assisting or Promoting Prostitution | 64 |
| 26D | Welfare Fraud | 58 |
| 23A | Pocket-picking | 34 |
| 370 | Pornography/Obscene Material | 32 |
| 11D | Fondling | 32 |
| 26E | Wire Fraud | 26 |
| 210 | Extortion/Blackmail | 19 |
| 23B | Purse-snatching | 19 |
| 36B | Statutory Rape | 16 |
| 26C | Impersonation | 12 |
| 64A | Human Trafficking, Commercial Sex Acts | 4 |
| 36A | Incest | 3 |
| 23E | Theft From Coin-Operated Machine or Device | 1 |
| 510 | Bribery | 1 |
| 09B | Negligent Manslaughter | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,388 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:2372 2022-02:2043 2022-03:2757 2022-04:2637 2022-05:2921 2022-06:2866 2022-07:3189 2022-08:2875 2022-09:2619 2022-10:2716 2022-11:2336 2022-12:2129 2023-01:2462 2023-02:2184 2023-03:2485 2023-04:2531 2023-05:2838 2023-06:2588 2023-07:2472 2023-08:2553 2023-09:2662 2023-10:2702 2023-11:2477 2023-12:2181 2024-01:2033 2024-02:2051 2024-03:2218 2024-04:2404 2024-05:2638 2024-06:2633 2024-07:2660 2024-08:2526 2024-09:2248 2024-10:2541 2024-11:1955 2024-12:1954 2025-01:1892 2025-02:1696 2025-03:2237 2025-04:2126 2025-05:2270 2025-06:2352 2025-07:2288 2025-08:2327 2025-09:2169 2025-10:2203 2025-11:1811 2025-12:1766

Use only full calendar years where you can; weight any partial year by its share of the year.