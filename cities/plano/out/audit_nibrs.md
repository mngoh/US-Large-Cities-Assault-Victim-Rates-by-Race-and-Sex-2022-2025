# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/plano.csv

49,748 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 38,486 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 2 |
| incident_hour | 10.0% | 3.9% | 24 |
| offense_id | 0.0% | 0.0% | 45,177 |
| offense_code | 0.0% | 0.0% | 45 |
| offense_name | 0.0% | 0.0% | 46 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 42 |
| victim_id | 0.0% | 0.0% | 44,843 |
| victim_seq_num | 0.0% | 0.0% | 34 |
| victim_type | 0.0% | 0.0% | 7 |
| age_code | 0.0% | 0.0% | 101 |
| age_num | 0.0% | 0.0% | 101 |
| sex | 0.0% | 43.4% | 4 |
| race | 0.0% | 2.0% | 7 |
| ethnicity | 0.0% | 46.6% | 4 |
| resident_status | 44.5% | 1.2% | 3 |
| relationship | 63.3% | 0.0% | 154 |
| weapon | 81.5% | 0.1% | 40 |
| injury | 89.7% | 0.0% | 37 |

## Duplicates

4,905 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 13B | Simple Assault | 6,161 |
| 23C | Shoplifting | 4,748 |
| 35B | Drug Equipment Violations | 4,519 |
| 23F | Theft From Motor Vehicle | 4,191 |
| 35A | Drug/Narcotic Violations | 3,860 |
| 23H | All Other Larceny | 2,994 |
| 26F | Identity Theft | 2,364 |
| 220 | Burglary/Breaking & Entering | 2,274 |
| 26A | False Pretenses/Swindle/Confidence Game | 2,176 |
| 26B | Credit Card/Automated Teller Machine Fraud | 2,043 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 2,037 |
| 23D | Theft From Building | 1,899 |
| 240 | Motor Vehicle Theft | 1,797 |
| 26E | Wire Fraud | 1,255 |
| 13A | Aggravated Assault | 1,118 |
| 13C | Intimidation | 1,078 |
| 250 | Counterfeiting/Forgery | 868 |
| 520 | Weapon Law Violations | 717 |
| 120 | Robbery | 459 |
| 290 | Destruction/Damage/Vandalism of Property | 379 |
| 280 | Stolen Property Offenses | 345 |
| 210 | Extortion/Blackmail | 329 |
| 40C | Purchasing Prostitution | 302 |
| 270 | Embezzlement | 261 |
| 26C | Impersonation | 228 |
| 11A | Rape | 213 |
| 370 | Pornography/Obscene Material | 201 |
| 100 | Kidnapping/Abduction | 168 |
| 11B | Sodomy | 120 |
| 11D | Criminal Sexual Contact | 106 |
| 26G | Hacking/Computer Invasion | 86 |
| 11C | Sexual Assault With An Object | 71 |
| 26D | Welfare Fraud | 63 |
| 11D | Fondling | 56 |
| 23A | Pocket-picking | 52 |
| 200 | Arson | 47 |
| 23B | Purse-snatching | 42 |
| 40A | Prostitution | 36 |
| 720 | Animal Cruelty | 30 |
| 23E | Theft From Coin-Operated Machine or Device | 18 |
| 09B | Negligent Manslaughter | 12 |
| 40B | Assisting or Promoting Prostitution | 9 |
| 09A | Murder and Nonnegligent Manslaughter | 9 |
| 39C | Gambling Equipment Violation | 3 |
| 510 | Bribery | 2 |
| 09C | Justifiable Homicide | 2 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 1,021 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:1170 2022-02:969 2022-03:1255 2022-04:1140 2022-05:1246 2022-06:1193 2022-07:1129 2022-08:1140 2022-09:1037 2022-10:1139 2022-11:982 2022-12:1103 2023-01:1210 2023-02:1152 2023-03:1231 2023-04:1154 2023-05:1181 2023-06:1085 2023-07:1194 2023-08:1137 2023-09:1110 2023-10:1042 2023-11:1037 2023-12:942 2024-01:970 2024-02:1004 2024-03:1171 2024-04:1087 2024-05:1121 2024-06:956 2024-07:971 2024-08:994 2024-09:1002 2024-10:1005 2024-11:935 2024-12:947 2025-01:895 2025-02:933 2025-03:969 2025-04:875 2025-05:919 2025-06:849 2025-07:911 2025-08:944 2025-09:917 2025-10:870 2025-11:745 2025-12:780

Use only full calendar years where you can; weight any partial year by its share of the year.