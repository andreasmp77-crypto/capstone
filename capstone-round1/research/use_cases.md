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

## Sprint and Deliverable Alignment

The user stories are grouped into delivery stages to keep the initial scope narrow while providing a clear backlog for future sprints.

| Sprint / Stage | User Stories | Deliverable Supported |
|---|---|---|
| **Sprint 1 — Risk Detection** | US-01 | Core n8n risk assessment POC |
| **Sprint 2 — Explainability & Briefing** | US-02, US-03 | AI risk briefing and structured output |
| **Sprint 3 — MVP User Experience** | US-04, US-05 | Future MVP UI and human-in-the-loop workflow |
| **Sprint 4 — Monitoring & Governance** | US-06 | LangSmith monitoring and logging |
| **Future Sprint** | US-07, US-08 | Management insights and welfare enhancement |

This sequence supports a focused development path: **identify → explain → brief → review → monitor → extend**.

## User Stories

### US-01 — Assign a Risk Level

> **As a Crew Manager, I want upcoming crew changes to be assigned a risk level based on defined operational indicators, so that I can identify which cases need attention first.**

**Sprint:** Sprint 1 — Risk Detection  
**Supports:** n8n risk assessment POC

---

### US-02 — See the Main Risk Drivers

> **As a Crew Manager, I want to see the main factors that caused a crew change to be flagged, so that I can quickly understand what requires attention.**

**Sprint:** Sprint 2 — Explainability & Briefing  
**Supports:** AI risk explanation and structured output

---

### US-03 — Receive a Concise Risk Briefing

> **As a Crew Manager, I want a concise briefing for a flagged crew change, so that I can understand the situation and recommended next actions without reviewing all raw data manually.**

**Sprint:** Sprint 2 — Explainability & Briefing  
**Supports:** n8n AI-generated risk briefing

---

### US-04 — Review a Flagged Case in One Place

> **As a Crew Manager, I want to review the crew-change details, risk level and AI briefing together, so that I can assess a flagged case without switching between multiple sources.**

**Sprint:** Sprint 3 — MVP User Experience  
**Supports:** Future MVP UI / risk review screen

---

### US-05 — Maintain Human Decision Ownership

> **As a Crew Manager, I want the system to clearly indicate when human review is required, so that I remain responsible for the final operational decision.**

**Sprint:** Sprint 3 — MVP User Experience  
**Supports:** Human-in-the-loop workflow

---

### US-06 — Monitor System Behaviour

> **As an Operations Manager or System Administrator, I want system inputs and outputs to be logged and monitored, so that unexpected results can be investigated and system performance can be reviewed.**

**Sprint:** Sprint 4 — Monitoring & Governance  
**Supports:** LangSmith monitoring, logging and traceability

---

### US-07 — View Recurring Risk Patterns

> **As an Operations Manager, I want to view recurring crew-change risk patterns over time, so that I can identify operational bottlenecks and support planning decisions.**

**Sprint:** Future Sprint  
**Supports:** Future management dashboard and analytics

---

### US-08 — Highlight Potential Welfare Impact

> **As a Crew Manager, I want potential crew-change disruptions that may affect planned crew relief to be highlighted, so that I can review whether additional action may be needed to support crew welfare and operational continuity.**

**Sprint:** Future Sprint  
**Supports:** Future crew welfare enhancement

## Prioritisation

| Priority | User Stories | Purpose |
|---|---|---|
| **Core POC** | US-01, US-02, US-03 | Demonstrate risk detection, explanation and briefing |
| **Future MVP** | US-04, US-05 | Add a focused human-in-the-loop user experience |
| **Monitoring & Governance** | US-06 | Provide observability and traceability |
| **Future Enhancements** | US-07, US-08 | Extend into management insights and welfare support |

This prioritisation deliberately keeps the first implementation narrow while ensuring that the user stories form a usable backlog for future sprints.

## Research Sources

The user stories were informed by a combination of publicly available industry research, regulatory guidance, professional maritime resources and personal professional experience in the maritime and shipping industry.

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

> **Industry evidence → Operational pain point → User need → User story**

The resulting user stories were also informed by personal professional experience and domain knowledge within the maritime and shipping industry.
