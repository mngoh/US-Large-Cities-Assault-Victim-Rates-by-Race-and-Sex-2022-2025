# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/san_jose.csv

122,481 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 2 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 102,008 |
| incident_date | 0.0% | 0.0% | 731 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 9.5% | 24 |
| offense_id | 0.0% | 0.0% | 112,095 |
| offense_code | 0.0% | 0.0% | 51 |
| offense_name | 0.0% | 0.0% | 51 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 115,243 |
| victim_seq_num | 0.0% | 0.0% | 46 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 103 |
| age_num | 0.0% | 0.0% | 103 |
| sex | 0.0% | 29.2% | 4 |
| race | 0.0% | 8.6% | 7 |
| ethnicity | 0.0% | 40.4% | 4 |
| resident_status | 27.6% | 2.7% | 3 |
| relationship | 61.9% | 0.0% | 151 |
| weapon | 75.0% | 1.6% | 69 |
| injury | 87.8% | 0.0% | 49 |

## Duplicates

7,238 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 16,741 |
| 290 | Destruction/Damage/Vandalism of Property | 12,379 |
| 23H | All Other Larceny | 11,948 |
| 240 | Motor Vehicle Theft | 11,939 |
| 220 | Burglary/Breaking & Entering | 9,411 |
| 23F | Theft From Motor Vehicle | 8,082 |
| 13A | Aggravated Assault | 7,120 |
| 23C | Shoplifting | 6,625 |
| 35A | Drug/Narcotic Violations | 4,887 |
| 26A | False Pretenses/Swindle/Confidence Game | 4,852 |
| 35B | Drug Equipment Violations | 4,272 |
| 120 | Robbery | 3,252 |
| 13C | Intimidation | 3,232 |
| 23D | Theft From Building | 2,929 |
| 26C | Impersonation | 2,702 |
| 520 | Weapon Law Violations | 1,851 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,595 |
| 11D | Criminal Sexual Contact | 1,543 |
| 280 | Stolen Property Offenses | 1,323 |
| 11A | Rape | 1,049 |
| 250 | Counterfeiting/Forgery | 761 |
| 100 | Kidnapping/Abduction | 633 |
| 26F | Identity Theft | 490 |
| 23A | Pocket-picking | 404 |
| 200 | Arson | 373 |
| 370 | Pornography/Obscene Material | 266 |
| 210 | Extortion/Blackmail | 218 |
| 720 | Animal Cruelty | 216 |
| 270 | Embezzlement | 201 |
| 40A | Prostitution | 200 |
| 36B | Statutory Rape | 174 |
| 23B | Purse-snatching | 167 |
| 11B | Sodomy | 162 |
| 26B | Credit Card/Automated Teller Machine Fraud | 118 |
| 11C | Sexual Assault With An Object | 118 |
| 09A | Murder and Nonnegligent Manslaughter | 50 |
| 64B | Human Trafficking, Involuntary Servitude | 49 |
| 64A | Human Trafficking, Commercial Sex Acts | 27 |
| 39A | Betting/Wagering | 24 |
| 26G | Hacking/Computer Invasion | 18 |
| 26D | Welfare Fraud | 17 |
| 40C | Purchasing Prostitution | 14 |
| 40B | Assisting or Promoting Prostitution | 12 |
| 23E | Theft From Coin-Operated Machine or Device | 11 |
| 39C | Gambling Equipment Violation | 6 |
| 26E | Wire Fraud | 5 |
| 36A | Incest | 4 |
| 09B | Negligent Manslaughter | 4 |
| 39B | Operating/Promoting/Assisting Gambling | 3 |
| 09C | Justifiable Homicide | 3 |
| 510 | Bribery | 1 |

## Coverage by month

0 unparseable dates. Range 2024-01-01 to 2025-12-31.

Median 5,113 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2024-01:5454 2024-02:4942 2024-03:5226 2024-04:4966 2024-05:5183 2024-06:5194 2024-07:5378 2024-08:5287 2024-09:5114 2024-10:5567 2024-11:5052 2024-12:5331 2025-01:5211 2025-02:4824 2025-03:5452 2025-04:5179 2025-05:5066 2025-06:4679 2025-07:4906 2025-08:5086 2025-09:4790 2025-10:5112 2025-11:4746 2025-12:4736

Use only full calendar years where you can; weight any partial year by its share of the year.