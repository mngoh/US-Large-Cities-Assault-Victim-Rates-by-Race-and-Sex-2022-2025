# Audit: /Users/Martin1/Desktop/GIT/US-Large-Cities-Assault-Victim-Rates-by-Race-and-Sex-2022-2025/data/interim/cities/cleveland.csv

220,797 rows, 24 columns. Guessed: date `incident_date`, code `offense_code`, description `offense_name`, id `victim_id`. Override with flags if wrong.

## Missing and coded-missing values

| column | blank | coded missing (0, X, UNKNOWN...) | distinct |
|---|---|---|---|
| file_year | 0.0% | 0.0% | 4 |
| agency | 0.0% | 0.0% | 1 |
| ori | 0.0% | 0.0% | 1 |
| incident_id | 0.0% | 0.0% | 169,721 |
| incident_date | 0.0% | 0.0% | 1,461 |
| report_date_flag | 0.0% | 0.0% | 1 |
| incident_hour | 0.0% | 7.5% | 24 |
| offense_id | 0.0% | 0.0% | 198,768 |
| offense_code | 0.0% | 0.0% | 42 |
| offense_name | 0.0% | 0.0% | 43 |
| attempt_complete | 0.0% | 0.0% | 2 |
| location | 0.0% | 0.0% | 38 |
| victim_id | 0.0% | 0.0% | 194,945 |
| victim_seq_num | 0.0% | 0.0% | 44 |
| victim_type | 0.0% | 0.2% | 9 |
| age_code | 0.0% | 0.0% | 104 |
| age_num | 0.0% | 0.0% | 104 |
| sex | 0.0% | 13.0% | 4 |
| race | 0.0% | 6.7% | 7 |
| ethnicity | 0.0% | 99.8% | 2 |
| resident_status | 100.0% | nan% | 0 |
| relationship | 56.8% | 0.0% | 251 |
| weapon | 73.0% | 2.7% | 116 |
| injury | 88.2% | 0.0% | 7 |

## Duplicates

25,852 rows share an id in `victim_id`. One row per victim or offense? Decide before counting.

## Every offense value

Read the whole list. Related offenses are often coded separately (intimate partner, on police, on children, attempts).

| offense_code | offense_name | rows |
|---|---|---|
| 290 | Destruction/Damage/Vandalism of Property | 38,316 |
| 13B | Simple Assault | 35,839 |
| 13C | Intimidation | 30,763 |
| 23H | All Other Larceny | 28,754 |
| 240 | Motor Vehicle Theft | 16,945 |
| 13A | Aggravated Assault | 14,851 |
| 220 | Burglary/Breaking & Entering | 14,053 |
| 23F | Theft From Motor Vehicle | 8,314 |
| 120 | Robbery | 6,992 |
| 520 | Weapon Law Violations | 5,577 |
| 23C | Shoplifting | 2,880 |
| 26F | Identity Theft | 2,279 |
| 100 | Kidnapping/Abduction | 2,085 |
| 35A | Drug/Narcotic Violations | 1,999 |
| 11A | Rape | 1,675 |
| 23D | Theft From Building | 1,462 |
| 26B | Credit Card/Automated Teller Machine Fraud | 1,311 |
| 23G | Theft of Motor Vehicle Parts or Accessories | 1,120 |
| 280 | Stolen Property Offenses | 936 |
| 200 | Arson | 884 |
| 11D | Criminal Sexual Contact | 751 |
| 09A | Murder and Nonnegligent Manslaughter | 496 |
| 250 | Counterfeiting/Forgery | 368 |
| 26A | False Pretenses/Swindle/Confidence Game | 293 |
| 35B | Drug Equipment Violations | 284 |
| 11D | Fondling | 256 |
| 210 | Extortion/Blackmail | 230 |
| 370 | Pornography/Obscene Material | 214 |
| 23A | Pocket-picking | 165 |
| 26E | Wire Fraud | 153 |
| 11B | Sodomy | 130 |
| 23B | Purse-snatching | 104 |
| 26D | Welfare Fraud | 77 |
| 23E | Theft From Coin-Operated Machine or Device | 73 |
| 36B | Statutory Rape | 49 |
| 40B | Assisting or Promoting Prostitution | 47 |
| 26C | Impersonation | 34 |
| 64A | Human Trafficking, Commercial Sex Acts | 13 |
| 270 | Embezzlement | 10 |
| 510 | Bribery | 6 |
| 64B | Human Trafficking, Involuntary Servitude | 6 |
| 39B | Operating/Promoting/Assisting Gambling | 2 |
| 720 | Animal Cruelty | 1 |

## Coverage by month

0 unparseable dates. Range 2022-01-01 to 2025-12-31.

Median 4,727 rows a month. Months under 60% of that (system changes, partial periods, reporting lag):

- none

Full series:

2022-01:3936 2022-02:3489 2022-03:4268 2022-04:4307 2022-05:4742 2022-06:4995 2022-07:5291 2022-08:4859 2022-09:4849 2022-10:4756 2022-11:4803 2022-12:4660 2023-01:4964 2023-02:4219 2023-03:4738 2023-04:4753 2023-05:5337 2023-06:5927 2023-07:5955 2023-08:5376 2023-09:4910 2023-10:4719 2023-11:4464 2023-12:4160 2024-01:4221 2024-02:3884 2024-03:4838 2024-04:4424 2024-05:5419 2024-06:4919 2024-07:5317 2024-08:5139 2024-09:4886 2024-10:5266 2024-11:4147 2024-12:4087 2025-01:3703 2025-02:3199 2025-03:4256 2025-04:4515 2025-05:4665 2025-06:4735 2025-07:4840 2025-08:4606 2025-09:4399 2025-10:4286 2025-11:3268 2025-12:3301

Use only full calendar years where you can; weight any partial year by its share of the year.