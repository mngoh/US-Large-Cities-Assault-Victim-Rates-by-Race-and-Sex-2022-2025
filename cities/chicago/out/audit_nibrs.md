# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/chicago.csv

1,050,801 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 853,453 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 6.5% | 24 |
| offense_id | 0.0% | 0.0% | 958,016 |
| offense_code | 0.0% | 0.0% | 40 |
| offense_name | 0.0% | 0.0% | 41 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 30 |
| victim_id | 0.0% | 0.0% | 962,199 |
| victim_seq_num | 0.0% | 0.0% | 23 |
| victim_type | 0.0% | 0.1% | 9 |
| age_code | 0.0% | 0.0% | 101 |
| age_num | 0.0% | 0.0% | 101 |
| sex | 0.0% | 16.0% | 4 |
| race | 0.0% | 11.0% | 6 |
| ethnicity | 0.0% | 25.2% | 4 |
| resident_status | 14.2% | 3.0% | 3 |
| relationship | 52.2% | 0.0% | 689 |
| weapon | 89.4% | 0.5% | 53 |
| injury | 89.2% | 0.0% | 7 |

## Duplicates

88,602 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 224,305 |
| 290 | Destruction/Damage/Vandalism of Property | 194,297 |
| 23H | All Other Larceny | 164,344 |
| 240 | Motor Vehicle Theft | 92,086 |
| 13C | Intimidation | 86,887 |
| 23C | Shoplifting | 49,825 |
| 120 | Robbery | 42,935 |
| 220 | Burglary/Breaking & Entering | 35,076 |
| 26A | False Pretenses/Swindle/Confidence Game | 32,749 |
| 520 | Weapon Law Violations | 20,839 |
| 23D | Theft From Building | 20,376 |
| 26F | Identity Theft | 17,948 |
| 35A | Drug/Narcotic Violations | 14,486 |
| 13A | Aggravated Assault | 14,196 |
| 23F | Theft From Motor Vehicle | 7,103 |
| 23A | Pocket-picking | 5,920 |
| 11A | Rape | 5,820 |
| 250 | Counterfeiting/Forgery | 4,593 |
| 26C | Impersonation | 3,114 |
| 11D | Criminal Sexual Contact | 2,949 |
| 09A | Murder and Nonnegligent Manslaughter | 1,910 |
| 200 | Arson | 1,766 |
| 100 | Kidnapping/Abduction | 1,506 |
| 23B | Purse-snatching | 1,263 |
| 370 | Pornography/Obscene Material | 1,084 |
| 35B | Drug Equipment Violations | 857 |
| 11D | Fondling | 688 |
| 40A | Prostitution | 516 |
| 720 | Animal Cruelty | 441 |
| 280 | Stolen Property Offenses | 294 |
| 210 | Extortion/Blackmail | 244 |
| 26G | Hacking/Computer Invasion | 147 |
| 40B | Assisting or Promoting Prostitution | 62 |
| 23E | Theft From Coin-Operated Machine or Device | 58 |
| 36B | Statutory Rape | 39 |
| 64A | Human Trafficking, Commercial Sex Acts | 38 |
| 39A | Betting/Wagering | 26 |
| 36A | Incest | 7 |
| 510 | Bribery | 3 |
| 64B | Human Trafficking, Involuntary Servitude | 2 |
| 09C | Justifiable Homicide | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 21,820 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:15375 2022-02:15257 2022-03:18509 2022-04:18117 2022-05:20758 2022-06:21699 2022-07:23539 2022-08:23508 2022-09:23191 2022-10:24541 2022-11:21714 2022-12:20697 2023-01:21047 2023-02:18101 2023-03:20602 2023-04:20758 2023-05:22692 2023-06:23487 2023-07:24602 2023-08:25016 2023-09:23237 2023-10:23381 2023-11:21594 2023-12:21612 2024-01:21559 2024-02:21976 2024-03:23320 2024-04:22687 2024-05:25867 2024-06:25743 2024-07:26859 2024-08:25114 2024-09:25143 2024-10:24754 2024-11:21519 2024-12:21279 2025-01:19771 2025-02:17400 2025-03:20940 2025-04:21018 2025-05:22163 2025-06:22724 2025-07:24459 2025-08:22718 2025-09:21364 2025-10:21925 2025-11:19362 2025-12:18103

Use only full calendar years where you can; weight any partial year by its share of the year.