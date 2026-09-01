# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-01

# Dashboard Documentation

## Capstone Project – Crew Change Risk Intelligence Dashboard

## 1. Purpose

This document describes the Tableau Public dashboards created for the capstone project. The visualisations support a hybrid analytical view of crew-change operations by combining:

- **EUROCONTROL operational aviation data** to provide airport disruption context.
- **UNCTADstat seafarer data** to provide global workforce supply context.
- A separate **synthetic crew-change dataset** for operational risk analysis and decision-support use cases.

The dashboards are designed to provide contextual intelligence rather than imply direct causal relationships between independent datasets.

---

## 2. Dashboard 1 – Global Seafarer Supply

### Objective

The Global Seafarer Supply dashboard provides a high-level view of where the global maritime workforce is geographically concentrated.

It addresses the question:

> **Which economies are the leading suppliers of Ratings and Officers, and where are major seafarer supply concentrations located?**

### Visualisations

#### 2.1 Top Seafarer Suppliers — Ratings 2021

A bar chart displays the ten leading economies by the number of **Ratings**.

- **Dimension:** Economy
- **Measure:** Seafarer Count
- **Filter:** Seafarer Type = Ratings
- **Filter:** Year = 2021
- **Ranking:** Top 10 economies by seafarer count

#### 2.2 Top Seafarer Suppliers — Officers 2021

A second bar chart displays the ten leading economies by the number of **Officers**.

Ratings and Officers are deliberately shown separately because they represent different workforce segments and may have different geographical supply patterns.

- **Dimension:** Economy
- **Measure:** Seafarer Count
- **Filter:** Seafarer Type = Officers
- **Filter:** Year = 2021
- **Ranking:** Top 10 economies by seafarer count

#### 2.3 Total Seafarer Supplier Countries 2021

A proportional-symbol world map provides a geographical overview of seafarer supply. The size of each mark represents the reported seafarer count for an economy.

This visualisation complements the Top 10 charts by answering:

> **How geographically concentrated is global seafarer supply?**

### Data preparation and design decisions

The `World` total and other non-country aggregate categories were excluded from economy-level ranking views to avoid comparing aggregate totals with individual economies.

Ratings and Officers were not combined into one chart because aggregation could hide meaningful differences in their geographical supply patterns.

---

## 3. Dashboard 2 – European Airport Delay Intelligence

### Objective

The European Airport Delay Intelligence dashboard provides operational aviation context relevant to crew-change travel.

It addresses two questions:

> **Which European airports experience the highest average pre-departure delays?**

> **How do delay patterns vary seasonally at selected operationally relevant airports?**

### Visualisations

#### 3.1 European Airport Delay Ranking 2025

A horizontal bar chart ranks airports by average pre-departure delay for the 2025 analysis year.

### Calculated metric

The dashboard uses the following weighted calculation:

```text
Average Delay per Departure (min)
=
SUM(Total_Delay_Minutes)
/
SUM(IFR_Departures)
```

This calculation is preferred over simply averaging row-level delay values because it accounts for differences in flight volumes.

#### 3.2 Seasonality of Average Pre-Departure Delays — 2025

A multi-line chart shows monthly delay patterns for selected airports relevant to the crew-change use case.

The final view includes:

- Amsterdam Schiphol
- Athens
- Frankfurt
- Hamburg
- London Heathrow

Each line represents an airport, allowing comparison of seasonal delay patterns and identification of monthly peaks.

- **Columns:** Month Name
- **Rows:** Average Delay per Departure (min)
- **Colour:** Airport Name
- **Analysis year:** 2025

### Design decision

The selected airports are presented as operationally relevant hubs within the case-study context. The analysis does not claim that EUROCONTROL data independently identifies them as the world's largest crew-change hubs.

---

## 4. Data Sources

### EUROCONTROL

**Purpose:** Operational aviation context and airport delay analysis.

**Used for:**
- Airport delay ranking
- Seasonal delay analysis

### UNCTADstat – US.Seafarers

**Purpose:** Global workforce supply context.

The source provides estimated seafarer supply by economy and workforce type, including Officers and Ratings.

**Used for:**
- Top supplier economies for Ratings
- Top supplier economies for Officers
- Global geographical distribution of seafarer supply

### Synthetic Crew Change Plans

**Purpose:** Operational proof-of-concept and decision-support analysis.

This synthetic dataset is separate from the external contextual datasets and is intended to model individual crew-change scenarios, including operational risk and outcomes.

---

## 5. Dashboard Design Logic

The project follows a layered analytical approach:

```text
EXTERNAL CONTEXT
│
├── Airport disruption
│   ├── Where are delays highest?
│   └── When do delays peak?
│
├── Global workforce supply
│   ├── Where do Ratings come from?
│   └── Where do Officers come from?
│
└── Operational crew-change analysis
    └── How can these factors support risk-aware decisions?
```

The dashboards provide context around two important dimensions of crew-change operations:

1. **Travel disruption risk**
2. **Geographical concentration of workforce supply**

---

## 6. Interactivity

The Tableau dashboards support exploratory analysis through interactive filters and chart tooltips.

Users can explore:

- Different reporting periods where filters are available
- Workforce supply by seafarer category
- Airport-level delay patterns
- Individual values through interactive marks and tooltips

---

## 7. Analytical Limitations

### Independent datasets

The EUROCONTROL and UNCTAD datasets operate at different levels of analysis and are not directly joined.

- EUROCONTROL data is airport and time-based.
- UNCTAD data is economy and workforce-based.

They are used as complementary contextual sources rather than as a single relational dataset.

### Reporting periods

The airport dashboard focuses on 2025 to provide a consistent full-year comparison. UNCTAD data reflects the reporting years available in the source dataset.

### Crew-change hub selection

The airports shown in the seasonality analysis were selected based on their relevance to the case-study context. Airport traffic volume alone does not necessarily define an airport as a crew-change hub.

### Synthetic operational data

The synthetic crew-change dataset is used for proof-of-concept purposes and should not be interpreted as real operational performance data.

---

## 8. Key Takeaway

Together, the dashboards demonstrate how external data can be transformed into operational context for a crew-change risk intelligence use case.

The project combines:

- **Aviation disruption intelligence**
- **Global maritime workforce supply intelligence**
- **Synthetic operational crew-change scenarios**

This hybrid approach provides the analytical foundation for a future AI-enabled decision-support system capable of assessing crew-change plans against relevant operational risk factors.

