# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-02
---

# AI Capstone Project — Crew Change Risk Copilot

## Overview

This project explores how AI and workflow automation could support **crew-change risk management** in a medium-sized maritime ship-management or crew-management company.

The proposed solution is the **Crew Change Risk Copilot**: a human-in-the-loop decision-support system designed to help crewing teams identify upcoming crew-change cases that may require earlier attention.

The project does **not** aim to replace the professional judgement of a Crew Manager or automate operational decisions.

The central project hypothesis is:

> **Earlier and clearer identification of combined warning signs may help a crewing officer intervene sooner.**

The Round 1 work progresses from:

**Sector Research → Use Cases → Data & Dashboard → Automation PoC → AI Monitoring → Cost & Timeline**

and provides the foundation for future MVP development.

---

## 1. What the System Does

At PoC level, the system takes information about an upcoming crew change and combines it with relevant operational context.

The workflow can:

1. Retrieve a crew-change record.
2. Retrieve relevant airport information.
3. Retrieve live weather information.
4. Evaluate defined operational risk factors.
5. Calculate a deterministic operational risk score.
6. Classify the case as Low / Medium / High risk.
7. Identify the main risk drivers.
8. Pass the structured information to an LLM.
9. Generate an executive risk briefing.
10. Recommend actions for human review.
11. Store the result in Airtable.
12. Create a human-readable report in Notion.

The viability of monitoring AI executions through LangSmith is demonstrated separately using a Python script.

The PoC therefore combines:

```text
Operational Data
       +
External Context
       ↓
Deterministic Risk Assessment
       ↓
AI Interpretation
       ↓
Structured Risk Briefing
       ↓
Human Review
       ↓
Reporting & Monitoring
```

## 2. Important Design Principle

The system is designed as a decision-support tool, not an autonomous decision-maker.

The AI should support the operational user by:

- highlighting potentially risky cases;
- explaining the main risk drivers;
- summarising relevant information;
- suggesting actions for consideration.

The final operational decision remains with the human user.

The system is not intended to:

- determine whether a person is legally permitted to travel;
- replace immigration or medical advice;
- make employment decisions;
- autonomously purchase or cancel travel;
- guarantee that a journey will succeed;
- make autonomous crew-management decisions.

## 3. Project Structure

```
README.md
capstone-round1/
│
│
├── data/
│   ├── raw/
│   ├── clean/
│   ├── processing/
│   └── ...
│
├── research/
│   ├── sector_research.md
│   ├── opportunities_risks.md
│   ├── use_cases.md
│   ├── Data Research.md
│   ├── Brainstorming Session.md
│   └── sources/
│
├── dashboard/
│   ├── capstone.twbx
│   ├── Dashboard1 Seafarers.png
│   ├── Dashboard2 Airports.png
│   └── dashboard_documentation.md
│
├── n8n/
│   ├── workflow.json
│   ├── workflow_documentation.md
│   ├── Crew Change Risk Briefing - CC-0005.md
│   └── workflow screenshot
│
├── langsmith/
│   ├── monitoring_sample.py
│   ├── monitoring_sample_output.md
│   ├── LangSmith_monitoring.md
│   ├── requirements.txt
│   └── screenshots/
│
├── cost_estimation/
│   ├── cost_analysis.md
│   └── timeline_estimate.md
│
└── feedback/
    └── round1_decision.md
```

# 4. Where to Start

To understand the project, review the folders in the following order:

### 1. Research

`research/`

Understand the industry problem, opportunities, risks, proposed use cases and user stories.

### 2. Data & Dashboard

`data/` and `dashboard/`

Review the available datasets and the Tableau dashboards providing workforce and operational context.

### 3. Automation PoC

`n8n/`

Review the Crew Change Risk Copilot workflow and example risk briefing.

### 4. AI Monitoring

`langsmith/`

Review how AI executions, inputs, outputs and performance are monitored.

### 5. Implementation Planning

`cost_estimation/`

Review the indicative implementation cost and proposed project timeline.

### 6. Feedback & Decision

`feedback/`

Contains the Round 1 review and project decision documentation.

## Attribution and Use

This project was created by Andreas Papachristophorou as part of an AI Consulting & Integration Capstone Project.

If you reuse, adapt, or build upon this work, please retain appropriate attribution to the original author and reference this repository where reasonably possible.

Third-party data, software, APIs and external resources remain subject to their respective licenses and terms of use.