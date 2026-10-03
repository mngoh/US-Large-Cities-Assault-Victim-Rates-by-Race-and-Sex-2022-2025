# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/stockton.csv

101,219 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 78,559 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 7.9% | 5.1% | 24 |
| offense_id | 0.0% | 0.0% | 87,725 |
| offense_code | 0.0% | 0.0% | 48 |
| offense_name | 0.0% | 0.0% | 49 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 42 |
| victim_id | 0.0% | 0.0% | 95,685 |
| victim_seq_num | 0.0% | 0.0% | 106 |
| victim_type | 0.0% | 0.0% | 8 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 25.9% | 4 |
| race | 0.0% | 0.9% | 7 |
| ethnicity | 0.0% | 31.0% | 4 |
| resident_status | 25.5% | 11.4% | 2 |
| relationship | 53.6% | 0.0% | 281 |
| weapon | 65.6% | 0.2% | 72 |
| injury | 86.7% | 0.0% | 41 |

## Duplicates

5,534 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 14,720 |
| 290 | Destruction/Damage/Vandalism of Property | 12,172 |
| 13A | Aggravated Assault | 9,925 |
| 220 | Burglary/Breaking & Entering | 8,474 |
| 240 | Motor Vehicle Theft | 7,385 |
| 23F | Theft From Motor Vehicle | 7,271 |
| 120 | Robbery | 6,162 |
| 23C | Shoplifting | 5,846 |
| 13C | Intimidation | 3,669 |
| 23D | Theft From Building | 3,398 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 3,352 |
| 26A | False Pretenses/Swindle/Confidence Game | 2,645 |
| 23H | All Other Larceny | 2,319 |
| 520 | Weapon Law Violations | 2,273 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,230 |
| 35A | Drug/Narcotic Violations | 1,363 |
| 26F | Identity Theft | 1,131 |
| 280 | Stolen Property Offenses | 860 |
| 200 | Arson | 856 |
| 35B | Drug Equipment Violations | 837 |
| 250 | Counterfeiting/Forgery | 790 |
| 100 | Kidnapping/Abduction | 583 |
| 11D | Criminal Sexual Contact | 495 |
| 11A | Rape | 432 |
| 26C | Impersonation | 423 |
| 270 | Embezzlement | 285 |
| 09A | Murder and Nonnegligent Manslaughter | 182 |
| 11D | Fondling | 172 |
| 23A | Pocket-picking | 154 |
| 23B | Purse-snatching | 153 |
| 11B | Sodomy | 112 |
| 370 | Pornography/Obscene Material | 101 |
| 11C | Sexual Assault With An Object | 93 |
| 720 | Animal Cruelty | 90 |
| 36B | Statutory Rape | 67 |
| 210 | Extortion/Blackmail | 56 |
| 40B | Assisting or Promoting Prostitution | 40 |
| 64A | Human Trafficking, Commercial Sex Acts | 38 |
| 26G | Hacking/Computer Invasion | 35 |
| 40A | Prostitution | 7 |
| 64B | Human Trafficking, Involuntary Servitude | 7 |
| 09C | Justifiable Homicide | 6 |
| 26E | Wire Fraud | 2 |
| 39B | Operating/Promoting/Assisting Gambling | 2 |
| 510 | Bribery | 2 |
| 36A | Incest | 1 |
| 39C | Gambling Equipment Violation | 1 |
| 40C | Purchasing Prostitution | 1 |
| 09B | Negligent Manslaughter | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 2,106 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:2318 2022-02:2040 2022-03:2170 2022-04:2171 2022-05:2323 2022-06:2404 2022-07:2297 2022-08:2456 2022-09:2166 2022-10:2158 2022-11:2117 2022-12:2036 2023-01:2170 2023-02:2068 2023-03:2259 2023-04:2388 2023-05:2353 2023-06:2444 2023-07:2414 2023-08:2353 2023-09:2292 2023-10:2110 2023-11:1902 2023-12:2036 2024-01:2234 2024-02:1916 2024-03:1969 2024-04:1989 2024-05:2158 2024-06:1884 2024-07:2288 2024-08:2080 2024-09:2038 2024-10:2035 2024-11:1881 2024-12:2146 2025-01:1843 2025-02:1638 2025-03:1919 2025-04:1973 2025-05:2101 2025-06:1945 2025-07:1994 2025-08:2124 2025-09:1996 2025-10:1965 2025-11:1760 2025-12:1898

Use only full calendar years where you can; weight any partial year by its share of the year.