# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-08-31

---
``` $ python capstone-round1/data/clean_data.py ```
---

######################################################################
CAPSTONE ROUND 1 - DATA CLEANING PIPELINE
######################################################################

Raw data directory:
C:\Users\andre\Documents\IronHack\ACFT_2026_Course\W8D5_Project_5_Capstone\capstone\capstone-round1\data\raw

Clean data directory:
C:\Users\andre\Documents\IronHack\ACFT_2026_Course\W8D5_Project_5_Capstone\capstone\capstone-round1\data\clean

######################################################################
CLEANING DATASET 1: EUROCONTROL AIRPORT DELAYS
######################################################################

Original rows: 735,045
Exact duplicate rows found: 0
Invalid or missing dates: 0

======================================================================
CLEANING SUMMARY: EUROCONTROL AIRPORT DELAYS
======================================================================
Original rows: 735,045
Cleaned rows:  209,352
Rows removed:  525,693

Saved cleaned file to:
C:\Users\andre\Documents\IronHack\ACFT_2026_Course\W8D5_Project_5_Capstone\capstone\capstone-round1\data\clean\eurocontrol_delays_clean.csv

######################################################################
CLEANING DATASET 2: UNCTAD SEAFARERS
######################################################################

2015 original rows: 555
2021 original rows: 537
Exact duplicate rows found: 0

======================================================================
CLEANING SUMMARY: UNCTAD SEAFARERS
======================================================================
Original rows: 1,092
Cleaned rows:  1,092
Rows removed:  0

Years included:
[np.int64(2015), np.int64(2021)]

Seafarer types:
<ArrowStringArray>
['Officers', 'Ratings', 'Total']
Length: 3, dtype: string

Saved cleaned file to:
C:\Users\andre\Documents\IronHack\ACFT_2026_Course\W8D5_Project_5_Capstone\capstone\capstone-round1\data\clean\unctad_seafarers_clean.csv

######################################################################
CLEANING DATASET 3: SYNTHETIC CREW CHANGE PLANS
######################################################################

Original rows: 150

Completely empty columns removed:
['ai_risk_briefing']

Exact duplicate rows found: 0
Duplicate crew_change_id values: 0

======================================================================
CLEANING SUMMARY: SYNTHETIC CREW CHANGE PLANS
======================================================================
Original rows: 150
Cleaned rows:  150
Rows removed:  0

Risk level distribution:
risk_level
Low       90
Medium    38
High      22
Name: count, dtype: int64[pyarrow]

Saved cleaned file to:
C:\Users\andre\Documents\IronHack\ACFT_2026_Course\W8D5_Project_5_Capstone\capstone\capstone-round1\data\clean\synthetic_crew_change_plans_clean.csv

######################################################################
DATA CLEANING COMPLETED SUCCESSFULLY
######################################################################

Clean files created:
- eurocontrol_delays_clean.csv
- synthetic_crew_change_plans_clean.csv
- unctad_seafarers_clean.csv
