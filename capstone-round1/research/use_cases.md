# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-01
---

# AI Use Case Proposals

## Company Context

The proposed use cases are designed for a medium-sized ship management or crew management company. Such companies typically manage multiple vessels and coordinate a significant number of crew changes while operating with limited resources and without the large dedicated AI or data teams available to major global organisations.

The use cases therefore focus on practical AI-supported decision-making and operational efficiency rather than large-scale autonomous systems.

---

## Use Case 1 — Crew Change Risk Copilot

### Business Problem

Crew-change plans can be affected by multiple factors, including travel disruptions, tight connections, documentation issues and changes to vessel schedules. Identifying which cases require attention can involve significant manual monitoring.

### Proposed AI Solution

An AI-supported decision tool that analyses available crew-change information and relevant risk indicators to identify and prioritise cases that may require human attention.

### Expected Value

- Earlier identification of potential issues
- Better prioritisation of crewing team workload
- Improved visibility of operational risks
- Reduced reliance on manual monitoring

### Fit for Company Size

This use case is suitable for a medium-sized company because it can support existing teams without requiring a large-scale autonomous system or extensive AI infrastructure.

---

## Use Case 2 — Crew Change Readiness Assistant

### Business Problem

Crew-change information may be spread across different documents, emails and operational systems. Missing or incomplete information can create delays and increase manual checking.

### Proposed AI Solution

An AI assistant that reviews available crew-change information and helps identify missing details, incomplete records or issues requiring follow-up before a planned crew change.

### Expected Value

- Reduced manual checking
- Improved information completeness
- Earlier identification of missing information
- More consistent preparation processes

### Fit for Company Size

A medium-sized company could benefit from reducing repetitive administrative work without needing to replace existing operational systems.

---

## Use Case 3 — Workforce Capacity & Planning Insights

### Business Problem

Crew management companies need visibility of workforce capacity and potential staffing pressures. Identifying longer-term trends can be difficult when information is distributed across operational records and external workforce data.

### Proposed AI Solution

A data-driven tool that combines available workforce and operational information to identify trends and provide insights that support workforce and capacity planning.

### Expected Value

- Improved visibility of workforce trends
- Earlier identification of potential capacity pressures
- Better support for planning and resource allocation
- More informed management decisions

### Fit for Company Size

This use case could provide strategic value to a medium-sized company but may require broader and more reliable historical data than the first two use cases.

---

## Initial Recommendation

The **Crew Change Risk Copilot** is recommended as the strongest candidate for further development.

It addresses a clear operational problem identified in the sector research and can be demonstrated using the available synthetic crew-change data and external operational data sources. It also provides a focused scope for a simple automation POC and future MVP.

The other two use cases remain relevant potential opportunities but would require additional data and broader integration to demonstrate their full value.

---

# User Stories — Recommended Use Case

The following user stories focus on the recommended use case: **Crew Change Risk Copilot**.

### Research Basis

These user stories are grounded in a combination of:

- Research using publicly available maritime industry, regulatory and professional sources.
- Industry evidence relating to crew changes, seafarer welfare, operational disruption, digitalisation and AI-supported decision-making.
- Personal professional experience and domain knowledge in the maritime and shipping industry.

Public sources were used to validate and complement practical industry knowledge. The objective was to derive user needs from realistic operational challenges rather than define requirements based solely on technical assumptions.

The research approach follows the principle:

> **Industry evidence → Operational pain point → User need → User story**

IMO highlights that effective crew changes are important for preventing fatigue and protecting seafarers' health, safety and wellbeing. Crew changes also involve a complex ecosystem of shipping companies, agents, ports, airports, airlines and national authorities. :contentReference[oaicite:0]{index=0}

Maritime industry discussions also highlight the potential of **Management by Exception**, where routine processes are monitored while anomalies and deviations are brought to human attention. This approach is particularly relevant to complex ship-management environments with significant manual monitoring requirements. :contentReference[oaicite:1]{index=1}

## Core User Stories

### US-01 — Identify Priority Cases

> **As a Crew Manager, I want to identify upcoming crew changes with potential risk indicators, so that I can prioritise cases requiring earlier attention.**

**Value:** Supports management by exception by helping users focus their attention on potentially problematic cases rather than manually reviewing every crew change.

---

### US-02 — Understand Why a Case Was Flagged

> **As a Crew Manager, I want to understand the factors that contributed to a risk flag, so that I can assess the situation and make an informed decision.**

**Value:** Supports transparency and reduces the risk of treating an AI-generated result as an unexplained recommendation.

---

### US-03 — Review Relevant Information

> **As a Crew Manager, I want to access the relevant operational information for a flagged crew change in one place, so that I can assess the situation without manually searching across multiple sources.**

**Value:** Reduces information fragmentation and manual effort during operational decision-making.

---

### US-04 — Receive an Operational Risk Briefing

> **As a Crew Manager, I want a concise summary of upcoming crew-change risks and exceptions, so that I can quickly understand the overall operational situation.**

**Value:** Helps users gain situational awareness and focus on the most relevant operational issues.

---

### US-05 — Maintain Human Control

> **As a Crew Manager, I want AI insights to support rather than replace my professional judgement, so that I retain responsibility for operational decisions.**

**Value:** Maintains a human-in-the-loop approach. The system provides decision support but does not autonomously make operational decisions.

---

### US-06 — Monitor Operational Trends

> **As an Operations Manager, I want to view crew-change risk patterns and trends, so that I can identify recurring issues and support better operational planning.**

**Value:** Provides management visibility beyond individual crew-change cases and supports identification of recurring operational patterns.

---

### US-07 — Monitor System Behaviour

> **As a System Administrator or Operations Manager, I want system inputs and outputs to be logged and monitored, so that unexpected results can be investigated and system performance can be reviewed.**

**Value:** Supports transparency, traceability and ongoing monitoring of the AI-supported system.

---

### US-08 — Support Crew Welfare Awareness

> **As a Crew Manager, I want potential crew-change disruptions that could affect planned crew relief to be highlighted, so that I can review situations that may require action to support crew welfare and operational continuity.**

**Value:** Recognises that crew changes are not only a logistical process but can also affect fatigue, wellbeing and safe vessel operations.

## Initial Prioritisation

| Priority | User Stories |
|---|---|
| **Core POC / MVP** | US-01, US-02, US-03, US-04 |
| **Governance & Trust** | US-05, US-07 |
| **Management / Future Enhancement** | US-06 |
| **Future Enhancement** | US-08 |

This prioritisation keeps the initial solution focused while providing a clear path for future development.

## Research Sources

The user stories were informed by a combination of publicly available industry research, regulatory guidance, professional maritime resources and personal professional experience in the maritime and shipping industry.

The following sources were reviewed to identify recurring challenges relating to crew changes, seafarer welfare, operational disruption, ship management, digitalisation, risk monitoring and human-in-the-loop decision support.

### International Regulatory and Industry Organisations

- International Maritime Organization (IMO) — https://www.imo.org/
- International Chamber of Shipping (ICS) — https://www.ics.org.uk/
- BIMCO — https://www.bimco.org/
- InterManager — https://intermanager.org/

### Maritime and Shipping Industry Press

- Lloyd's List — https://www.lloydslist.com/
- Ship Management International — https://www.shipmanagementinternational.com/
- Cruise Industry News — https://www.cruiseindustrynews.com/
- Cyprus Shipping News — https://cyprusshippingnews.com/

### Classification Societies and Technical Organisations

- DNV — https://www.dnv.com/
- RINA — https://www.rina.org/
- Lloyd's Register — https://www.lr.org/
- American Bureau of Shipping (ABS) — https://www.eagle.org/

### Marine Insurance and Risk

Selected P&I Club resources were also considered, particularly regarding crew welfare, fatigue, repatriation, travel disruption, geopolitical risks, sanctions and operational risk management.

Examples include:

- NorthStandard — https://north-standard.com/
- Gard — https://gard.no/
- The Standard Club — https://www.standard-club.com/

### Research Approach

The sources were not used as a formal academic literature review. Instead, they were used to identify and validate recurring industry challenges and operational needs.

The research process followed the framework:

> **Industry evidence → Operational pain point → User need → User story**

The resulting user stories were also informed by personal professional experience and domain knowledge within the maritime and shipping industry.
