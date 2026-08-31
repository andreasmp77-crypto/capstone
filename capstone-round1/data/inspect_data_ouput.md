# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-08-31

---
```python capstone-round1/data/inspect_data.py```
---

######################################################################
CAPSTONE ROUND 1 - DATA INSPECTION
######################################################################

Data directory: C:\Users\andre\Documents\IronHack\ACFT_2026_Course\W8D5_Project_5_Capstone\capstone\capstone-round1\data
Raw data directory: C:\Users\andre\Documents\IronHack\ACFT_2026_Course\W8D5_Project_5_Capstone\capstone\capstone-round1\data\raw

FILE AVAILABILITY CHECK
Found: All_Pre-Departure_Delay.xlsx
Found: 2015 US.Seafarers_20260831_120803.csv
Found: 2021 US.Seafarers_20260831_111621.csv
Found: synthetic_crew_change_plans.csv

======================================================================
EXCEL WORKBOOK SHEETS
======================================================================
['Copyright notice and disclaimer', 'META', 'DATA', 'STATE_MM (by APT)', 'APT_MM', 'APT_DD', 'Change log']

======================================================================
DATASET: EUROCONTROL - All Pre-Departure Delay
======================================================================

1. SHAPE
Rows: 735,045
Columns: 11

2. COLUMN NAMES
['YEAR', 'MONTH_NUM', 'MONTH_MON', 'FLT_DATE', 'APT_ICAO', 'APT_NAME', 'STATE_NAME', 'FLT_DEP_1', 'FLT_DEP_IFR_2', 'DLY_ALL_PRE_2', 'Pivot Label']

3. DATA TYPES
YEAR                      int64
MONTH_NUM                 int64
MONTH_MON                   str
FLT_DATE         datetime64[us]
APT_ICAO                    str
APT_NAME                    str
STATE_NAME                  str
FLT_DEP_1                 int64
FLT_DEP_IFR_2           float64
DLY_ALL_PRE_2           float64
Pivot Label                 str
dtype: object

4. FIRST 5 ROWS
   YEAR  MONTH_NUM MONTH_MON   FLT_DATE APT_ICAO  ... STATE_NAME FLT_DEP_1  FLT_DEP_IFR_2  DLY_ALL_PRE_2                  Pivot Label
0  2020          1       JAN 2020-01-01     EBAW  ...    Belgium         5            NaN            NaN               Antwerp (EBAW)
1  2020          1       JAN 2020-01-01     EBBR  ...    Belgium       202          201.0         1995.0              Brussels (EBBR)
2  2020          1       JAN 2020-01-01     EBCI  ...    Belgium        63           63.0          600.0  Brussels - Charleroi (EBCI)
3  2020          1       JAN 2020-01-01     EBLG  ...    Belgium         9            NaN            NaN                 Liège (EBLG)
4  2020          1       JAN 2020-01-01     EBOS  ...    Belgium         6            NaN            NaN         Ostend-Bruges (EBOS)

[5 rows x 11 columns]

5. MISSING VALUES
FLT_DEP_IFR_2    525693
DLY_ALL_PRE_2    525693
dtype: int64

6. DUPLICATE ROWS
Duplicate rows: 0

7. UNIQUE VALUES PER COLUMN
YEAR                 7
MONTH_NUM           12
MONTH_MON           12
STATE_NAME          43
APT_ICAO           334
APT_NAME           343
Pivot Label        343
FLT_DEP_1          837
FLT_DEP_IFR_2      841
FLT_DATE          2373
DLY_ALL_PRE_2    69731
dtype: int64

EUROCONTROL SPECIFIC CHECKS

Date range:
2020-01-01 00:00:00 to 2026-06-30 00:00:00

Number of airports:
334

======================================================================
DATASET: UNCTAD Seafarers - 2015
======================================================================

1. SHAPE
Rows: 555
Columns: 8

2. COLUMN NAMES
['Economy_Label', 'SeafarerType_Label', 'Percentage_of_total_world_Value', 'Percentage_of_total_world_Footnote', 'Percentage_of_total_world_MissingValue', 'Absolute_value_Value', 'Absolute_value_Footnote', 'Absolute_value_MissingValue']

3. DATA TYPES
Economy_Label                                 str
SeafarerType_Label                            str
Percentage_of_total_world_Value           float64
Percentage_of_total_world_Footnote        float64
Percentage_of_total_world_MissingValue    float64
Absolute_value_Value                        int64
Absolute_value_Footnote                       str
Absolute_value_MissingValue               float64
dtype: object

4. FIRST 5 ROWS
  Economy_Label SeafarerType_Label  ...                            Absolute_value_Footnote  Absolute_value_MissingValue
0         World           Officers  ...                                                NaN                          NaN
1         World            Ratings  ...                                                NaN                          NaN
2         World              Total  ...                                                NaN                          NaN
3       Albania           Officers  ...  Estimated by BIMCO/ICS based on estimates of s...                          NaN
4       Albania            Ratings  ...  Estimated by BIMCO/ICS based on estimates of s...                          NaN

[5 rows x 8 columns]

5. MISSING VALUES
Percentage_of_total_world_Footnote        555
Percentage_of_total_world_MissingValue    555
Absolute_value_MissingValue               555
Absolute_value_Footnote                   110
dtype: int64

6. DUPLICATE ROWS
Duplicate rows: 0

7. UNIQUE VALUES PER COLUMN
Percentage_of_total_world_Footnote          0
Percentage_of_total_world_MissingValue      0
Absolute_value_MissingValue                 0
SeafarerType_Label                          3
Absolute_value_Footnote                     5
Economy_Label                             185
Percentage_of_total_world_Value           269
Absolute_value_Value                      415
dtype: int64

======================================================================
DATASET: UNCTAD Seafarers - 2021
======================================================================

1. SHAPE
Rows: 537
Columns: 8

2. COLUMN NAMES
['Economy_Label', 'SeafarerType_Label', 'Percentage_of_total_world_Value', 'Percentage_of_total_world_Footnote', 'Percentage_of_total_world_MissingValue', 'Absolute_value_Value', 'Absolute_value_Footnote', 'Absolute_value_MissingValue']

3. DATA TYPES
Economy_Label                                 str
SeafarerType_Label                            str
Percentage_of_total_world_Value           float64
Percentage_of_total_world_Footnote        float64
Percentage_of_total_world_MissingValue    float64
Absolute_value_Value                        int64
Absolute_value_Footnote                       str
Absolute_value_MissingValue               float64
dtype: object

4. FIRST 5 ROWS
  Economy_Label SeafarerType_Label  ...                            Absolute_value_Footnote  Absolute_value_MissingValue
0         World           Officers  ...                                                NaN                          NaN
1         World            Ratings  ...                                                NaN                          NaN
2         World              Total  ...                                                NaN                          NaN
3       Albania           Officers  ...  Estimated by BIMCO/ICS based on estimates of s...                          NaN
4       Albania            Ratings  ...  Estimated by BIMCO/ICS based on estimates of s...                          NaN

[5 rows x 8 columns]

5. MISSING VALUES
Percentage_of_total_world_Footnote        537
Percentage_of_total_world_MissingValue    537
Absolute_value_MissingValue               537
Absolute_value_Footnote                    90
dtype: int64

6. DUPLICATE ROWS
Duplicate rows: 0

7. UNIQUE VALUES PER COLUMN
Percentage_of_total_world_Footnote          0
Percentage_of_total_world_MissingValue      0
Absolute_value_MissingValue                 0
SeafarerType_Label                          3
Absolute_value_Footnote                     5
Economy_Label                             179
Percentage_of_total_world_Value           282
Absolute_value_Value                      414
dtype: int64

======================================================================
UNCTAD 2015 vs 2021 COMPARISON
======================================================================

Columns only in 2015:
set()

Columns only in 2021:
set()

Common columns:
{'Absolute_value_Footnote', 'Percentage_of_total_world_Footnote', 'Percentage_of_total_world_Value', 'SeafarerType_Label', 'Economy_Label', 'Percentage_of_total_world_MissingValue', 'Absolute_value_Value', 'Absolute_value_MissingValue'}

Economies only in 2015:
['Anguilla', 'Bermuda', 'British Virgin Islands', 'Cayman Islands', 'Channel Islands', 'Curacao', 'Faroe Islands', 'French Polynesia', 'Gibraltar', 'Guadeloupe', 'Isle of Man', "Lao People's Dem. Rep.", 'Martinique', 'New Caledonia', 'Saint Helena', 'Timor-Leste', 'Turks and Caicos Islands']

Economies only in 2021:
['Austria', 'Belarus', 'Czechia', 'El Salvador', 'Malawi', 'Nauru', 'Saint Lucia', 'San Marino', 'Serbia', 'Zambia', 'Zimbabwe']

======================================================================
DATASET: Synthetic Crew Change Plans
======================================================================

1. SHAPE
Rows: 150
Columns: 40

2. COLUMN NAMES
['crew_change_id', 'plan_created_date', 'vessel_code', 'seafarer_id', 'rank', 'movement_type', 'origin_airport', 'connection_airport', 'destination_airport', 'number_of_connections', 'shortest_connection_minutes', 'scheduled_departure', 'scheduled_arrival', 'estimated_travel_cost_eur', 'joining_port', 'vessel_eta', 'reporting_deadline', 'port_transfer_minutes', 'port_agent_confirmed', 'vessel_eta_confidence', 'passport_country_code', 'passport_valid', 'visa_status', 'medical_valid', 'documents_verified', 'ticket_status', 'airport_delay_risk', 'weather_risk', 'route_complexity', 'arrival_buffer_minutes', 'risk_score', 'risk_level', 'risk_reasons', 'ai_risk_briefing', 'human_review_status', 'actual_outcome', 'actual_delay_minutes', 'crew_change_completed', 'additional_cost_eur', 'outcome_reason']

3. DATA TYPES
crew_change_id                     str
plan_created_date                  str
vessel_code                        str
seafarer_id                        str
rank                               str
movement_type                      str
origin_airport                     str
connection_airport                 str
destination_airport                str
number_of_connections            int64
shortest_connection_minutes    float64
scheduled_departure                str
scheduled_arrival                  str
estimated_travel_cost_eur        int64
joining_port                       str
vessel_eta                         str
reporting_deadline                 str
port_transfer_minutes            int64
port_agent_confirmed              bool
vessel_eta_confidence              str
passport_country_code              str
passport_valid                    bool
visa_status                        str
medical_valid                     bool
documents_verified                bool
ticket_status                      str
airport_delay_risk                 str
weather_risk                       str
route_complexity                   str
arrival_buffer_minutes           int64
risk_score                       int64
risk_level                         str
risk_reasons                       str
ai_risk_briefing               float64
human_review_status                str
actual_outcome                     str
actual_delay_minutes             int64
crew_change_completed             bool
additional_cost_eur              int64
outcome_reason                     str
dtype: object

4. FIRST 5 ROWS
  crew_change_id plan_created_date vessel_code seafarer_id  ... actual_delay_minutes crew_change_completed additional_cost_eur outcome_reason
0        CC-0001        2026-03-19     VSL-014    SEA-0029  ...                    0                  True                   0  No disruption
1        CC-0002        2026-03-18     VSL-013    SEA-0011  ...                    0                  True                   0  No disruption
2        CC-0003        2026-06-06     VSL-003    SEA-0078  ...                    0                  True                   0  No disruption
3        CC-0004        2026-06-09     VSL-015    SEA-0019  ...                  138                  True                 350   Flight delay
4        CC-0005        2026-08-10     VSL-013    SEA-0077  ...                    0                  True                   0  No disruption

[5 rows x 40 columns]

5. MISSING VALUES
ai_risk_briefing               150
connection_airport              37
shortest_connection_minutes     37
dtype: int64

6. DUPLICATE ROWS
Duplicate rows: 0

7. UNIQUE VALUES PER COLUMN
ai_risk_briefing                 0
movement_type                    1
passport_valid                   1
medical_valid                    1
human_review_status              1
port_agent_confirmed             2
documents_verified               2
number_of_connections            2
crew_change_completed            2
vessel_eta_confidence            3
risk_level                       3
route_complexity                 3
weather_risk                     3
airport_delay_risk               3
visa_status                      4
ticket_status                    4
actual_outcome                   4
passport_country_code            5
connection_airport               5
origin_airport                   6
port_transfer_minutes            6
outcome_reason                   7
joining_port                    10
rank                            10
destination_airport             10
vessel_code                     18
additional_cost_eur             22
risk_score                      28
actual_delay_minutes            33
shortest_connection_minutes     76
seafarer_id                     76
risk_reasons                    95
plan_created_date              103
arrival_buffer_minutes         134
estimated_travel_cost_eur      141
scheduled_arrival              148
scheduled_departure            149
reporting_deadline             150
crew_change_id                 150
vessel_eta                     150
dtype: int64

SYNTHETIC CREW CHANGE SPECIFIC CHECKS

Unique Crew Change IDs:
150

Risk Level Distribution:
risk_level
Low       90
Medium    38
High      22
Name: count, dtype: int64
