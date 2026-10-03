# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/jacksonville.csv

269,315 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 215,128 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 100.0% | 1 |
| offense_id | 0.0% | 0.0% | 246,454 |
| offense_code | 0.0% | 0.0% | 50 |
| offense_name | 0.0% | 0.0% | 51 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 45 |
| victim_id | 0.0% | 0.0% | 249,672 |
| victim_seq_num | 0.0% | 0.0% | 62 |
| victim_type | 0.0% | 0.1% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 35.0% | 4 |
| race | 0.0% | 2.2% | 7 |
| ethnicity | 0.0% | 39.3% | 4 |
| resident_status | 32.9% | 4.4% | 3 |
| relationship | 63.5% | 0.0% | 356 |
| weapon | 67.8% | 0.7% | 132 |
| injury | 87.1% | 0.0% | 7 |

## Duplicates

19,643 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 53,515 |
| 23H | All Other Larceny | 29,002 |
| 23C | Shoplifting | 25,770 |
| 290 | Destruction/Damage/Vandalism of Property | 25,717 |
| 23F | Theft From Motor Vehicle | 22,016 |
| 13A | Aggravated Assault | 19,191 |
| 35A | Drug/Narcotic Violations | 16,926 |
| 220 | Burglary/Breaking & Entering | 12,769 |
| 240 | Motor Vehicle Theft | 11,353 |
| 520 | Weapon Law Violations | 8,907 |
| 35B | Drug Equipment Violations | 8,585 |
| 13C | Intimidation | 7,205 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 4,270 |
| 26A | False Pretenses/Swindle/Confidence Game | 3,620 |
| 26B | Credit Card/Automated Teller Machine Fraud | 3,482 |
| 120 | Robbery | 2,798 |
| 23D | Theft From Building | 2,214 |
| 250 | Counterfeiting/Forgery | 2,118 |
| 26C | Impersonation | 1,462 |
| 11A | Rape | 1,380 |
| 270 | Embezzlement | 1,056 |
| 280 | Stolen Property Offenses | 1,012 |
| 100 | Kidnapping/Abduction | 703 |
| 11D | Criminal Sexual Contact | 479 |
| 26F | Identity Theft | 467 |
| 200 | Arson | 444 |
| 09A | Murder and Nonnegligent Manslaughter | 390 |
| 210 | Extortion/Blackmail | 369 |
| 720 | Animal Cruelty | 334 |
| 40B | Assisting or Promoting Prostitution | 300 |
| 23A | Pocket-picking | 201 |
| 40A | Prostitution | 185 |
| 36B | Statutory Rape | 179 |
| 370 | Pornography/Obscene Material | 149 |
| 23B | Purse-snatching | 133 |
| 11B | Sodomy | 125 |
| 11D | Fondling | 116 |
| 23E | Theft From Coin-Operated Machine or Device | 80 |
| 26G | Hacking/Computer Invasion | 79 |
| 09C | Justifiable Homicide | 58 |
| 26D | Welfare Fraud | 31 |
| 11C | Sexual Assault With An Object | 30 |
| 39B | Operating/Promoting/Assisting Gambling | 25 |
| 64A | Human Trafficking, Commercial Sex Acts | 22 |
| 09B | Negligent Manslaughter | 19 |
| 36A | Incest | 13 |
| 39C | Gambling Equipment Violation | 6 |
| 510 | Bribery | 4 |
| 26E | Wire Fraud | 3 |
| 39A | Betting/Wagering | 2 |
| 64B | Human Trafficking, Involuntary Servitude | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 5,698 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:5326 2022-02:4928 2022-03:5408 2022-04:5709 2022-05:5941 2022-06:5686 2022-07:5818 2022-08:5815 2022-09:5661 2022-10:5820 2022-11:5297 2022-12:5712 2023-01:5831 2023-02:4044 2023-03:5566 2023-04:5868 2023-05:6201 2023-06:5780 2023-07:6312 2023-08:6264 2023-09:6063 2023-10:6174 2023-11:5668 2023-12:6026 2024-01:6039 2024-02:5505 2024-03:6068 2024-04:5929 2024-05:6883 2024-06:5946 2024-07:6037 2024-08:5840 2024-09:5778 2024-10:5858 2024-11:5604 2024-12:5377 2025-01:5059 2025-02:4999 2025-03:5046 2025-04:5061 2025-05:5502 2025-06:5080 2025-07:5325 2025-08:5048 2025-09:5137 2025-10:5285 2025-11:4924 2025-12:5067

Use only full calendar years where you can; weight any partial year by its share of the year.