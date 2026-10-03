# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/denver.csv

301,650 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 269,008 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 0.0% | 5.9% | 24 |
| offense_id | 0.0% | 0.0% | 281,375 |
| offense_code | 0.0% | 0.0% | 47 |
| offense_name | 0.0% | 0.0% | 48 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 34 |
| victim_id | 0.0% | 0.0% | 293,143 |
| victim_seq_num | 0.0% | 0.0% | 46 |
| victim_type | 0.0% | 0.0% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 24.7% | 4 |
| race | 0.0% | 7.8% | 6 |
| ethnicity | 0.0% | 36.7% | 4 |
| resident_status | 24.9% | 0.6% | 3 |
| relationship | 68.5% | 0.0% | 199 |
| weapon | 77.5% | 0.5% | 79 |
| injury | 88.3% | 0.0% | 69 |

## Duplicates

8,507 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 240 | Motor Vehicle Theft | 42,542 |
| 290 | Destruction/Damage/Vandalism of Property | 38,589 |
| 23F | Theft From Motor Vehicle | 29,590 |
| 23H | All Other Larceny | 26,765 |
| 13B | Simple Assault | 24,874 |
| 220 | Burglary/Breaking & Entering | 22,962 |
| 13A | Aggravated Assault | 20,722 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 17,389 |
| 23C | Shoplifting | 11,252 |
| 520 | Weapon Law Violations | 9,680 |
| 35A | Drug/Narcotic Violations | 9,565 |
| 35B | Drug Equipment Violations | 6,992 |
| 23D | Theft From Building | 6,808 |
| 13C | Intimidation | 6,641 |
| 120 | Robbery | 6,347 |
| 26A | False Pretenses/Swindle/Confidence Game | 3,757 |
| 280 | Stolen Property Offenses | 2,865 |
| 26F | Identity Theft | 2,691 |
| 11A | Rape | 2,053 |
| 100 | Kidnapping/Abduction | 1,252 |
| 11D | Criminal Sexual Contact | 1,220 |
| 26G | Hacking/Computer Invasion | 1,206 |
| 250 | Counterfeiting/Forgery | 767 |
| 200 | Arson | 752 |
| 11B | Sodomy | 699 |
| 26B | Credit Card/Automated Teller Machine Fraud | 648 |
| 40A | Prostitution | 535 |
| 11D | Fondling | 495 |
| 26C | Impersonation | 418 |
| 210 | Extortion/Blackmail | 378 |
| 09A | Murder and Nonnegligent Manslaughter | 288 |
| 23B | Purse-snatching | 135 |
| 370 | Pornography/Obscene Material | 134 |
| 23A | Pocket-picking | 122 |
| 720 | Animal Cruelty | 109 |
| 23E | Theft From Coin-Operated Machine or Device | 99 |
| 270 | Embezzlement | 77 |
| 36B | Statutory Rape | 63 |
| 64A | Human Trafficking, Commercial Sex Acts | 51 |
| 510 | Bribery | 44 |
| 11C | Sexual Assault With An Object | 36 |
| 64B | Human Trafficking, Involuntary Servitude | 11 |
| 40B | Assisting or Promoting Prostitution | 10 |
| 36A | Incest | 6 |
| 09C | Justifiable Homicide | 4 |
| 09B | Negligent Manslaughter | 3 |
| 39B | Operating/Promoting/Assisting Gambling | 3 |
| 39A | Betting/Wagering | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 6,320 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:6895 2022-02:6254 2022-03:7130 2022-04:7046 2022-05:7355 2022-06:6938 2022-07:7364 2022-08:7315 2022-09:7090 2022-10:7238 2022-11:6531 2022-12:6362 2023-01:7017 2023-02:6047 2023-03:6501 2023-04:6387 2023-05:7090 2023-06:7218 2023-07:7601 2023-08:7018 2023-09:6571 2023-10:6553 2023-11:6127 2023-12:6277 2024-01:6068 2024-02:5390 2024-03:5611 2024-04:5585 2024-05:6164 2024-06:5965 2024-07:6492 2024-08:6700 2024-09:6528 2024-10:6630 2024-11:5436 2024-12:5993 2025-01:5536 2025-02:4805 2025-03:5329 2025-04:5410 2025-05:5543 2025-06:5278 2025-07:5985 2025-08:5782 2025-09:5501 2025-10:5607 2025-11:5256 2025-12:5131

Use only full calendar years where you can; weight any partial year by its share of the year.