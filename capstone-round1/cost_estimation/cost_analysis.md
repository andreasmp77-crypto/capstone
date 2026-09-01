# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-01
---

# Cost Analysis — Crew Change Risk Copilot

## 1. Purpose

This document provides an indicative cost estimate for developing and piloting the **Crew Change Risk Copilot**.

The estimate is based on a lean delivery model using an independent Lead AI & Maritime Consultant supported by specialist freelance subcontractors sourced across the EU.

The figures are intended for an initial consulting and pilot discussion and should not be considered a final supplier quotation.

---

# 2. Key Assumptions

| Assumption | Description |
|---|---|
| Target organisation | Medium-sized ship management company |
| Project scope | Focused Crew Change Risk Copilot MVP / pilot |
| Pilot duration | Approximately 12 weeks |
| Delivery model | Independent Lead Consultant supported by EU-based freelance specialists |
| Lead Consultant location | Germany |
| Subcontractor sourcing | Remote freelancers from Germany and other EU countries |
| Users | Small group of Crew Managers and Operations users |
| Data | Existing or prepared pilot data and selected external operational data |
| AI approach | LLM-supported risk analysis, explanation and summarisation |
| Human oversight | Required; AI supports but does not autonomously make operational decisions |
| UI approach | Lightweight interface using Streamlit or similar framework |
| Deployment | Controlled pilot environment rather than full enterprise production deployment |

---

# 3. Delivery Team and Rate Assumptions

| Role | Engagement | Day Rate |
|---|---|---:|
| Lead AI & Maritime Consultant | Core project role | €750 |
| Freelance AI Developer | Core technical resource | €500 |
| Freelance UI Developer | Limited project-based support | €450 |
| Specialist Advisor | Limited / ad hoc engagement | €800 |

The Lead Consultant is responsible for client engagement, requirements definition, solution design and overall delivery coordination.

Specialist freelancers may be sourced from across the EU to access a wider talent pool and maintain a flexible delivery model.

---

# 4. Lead AI & Maritime Consultant Cost

| Activity | Days | Cost |
|---|---:|---:|
| Discovery & Requirements | 7 | €5,250 |
| Solution Design | 5 | €3,750 |
| Project Management & Client Coordination | 3 | €2,250 |
| Maritime Domain Input & Risk Logic | 2 | €1,500 |
| Testing & Evaluation | 2 | €1,500 |
| Documentation & Handover | 2 | €1,500 |
| **Total** | **21** | **€15,750** |

### Revised Lean Pilot Allocation

Following scope review, the Lead Consultant effort was reduced to approximately **16 days** through consolidation of activities and a focused MVP scope.

| Role | Days | Day Rate | Cost |
|---|---:|---:|---:|
| Lead AI & Maritime Consultant | **16** | €750 | **€12,000** |

---

# 5. Freelance AI Developer Cost

The AI Developer is responsible for the core technical implementation.

| Activity | Days |
|---|---:|
| Technical Setup & Architecture | 2 |
| Data Processing & Input Preparation | 1 |
| AI / LLM Development | 5 |
| Workflow & Integration | 2 |
| Backend Development | 3 |
| Testing & Debugging | 2 |
| Deployment Support | 1 |
| **Total** | **16** |

| Role | Days | Day Rate | Cost |
|---|---:|---:|---:|
| Freelance AI Developer | **16** | €500 | **€8,000** |

---

# 6. Freelance UI Developer Cost

The pilot uses a lightweight UI approach rather than a fully custom enterprise frontend.

The UI Developer focuses on establishing a clear and intuitive user experience and supporting key operational screens.

| Activity | Days |
|---|---:|
| UI/UX Design and Wireframing | 1 |
| Frontend Development | 2 |
| Dashboard and Risk Visualisation | 1 |
| Testing and UI Refinements | 1 |
| **Total** | **5** |

| Role | Days | Day Rate | Cost |
|---|---:|---:|---:|
| Freelance UI Developer | **5** | €450 | **€2,250** |

Backend and API integration are covered by the Freelance AI Developer.

---

# 7. Specialist Advisor Cost

The Specialist Advisor is engaged only at key stages of the project to provide targeted expert review and recommendations.

| Activity | Days |
|---|---:|
| Initial Solution Review | 1 |
| Mid-Project Review | 1 |
| Final Review and Recommendations | 1 |
| **Total** | **3** |

| Role | Days | Day Rate | Cost |
|---|---:|---:|---:|
| Specialist Advisor | **3** | €800 | **€2,400** |

---

# 8. Direct Labour Cost Summary

| Role | Days | Day Rate | Cost |
|---|---:|---:|---:|
| Lead AI & Maritime Consultant | 16 | €750 | €12,000 |
| Freelance AI Developer | 16 | €500 | €8,000 |
| Freelance UI Developer | 5 | €450 | €2,250 |
| Specialist Advisor | 3 | €800 | €2,400 |
| **Total Direct Labour Cost** | **40 days** | | **€24,650** |

---

# 9. Infrastructure, Software and API Costs

The following costs are estimated for the approximately 12-week controlled pilot.

| Category | Monthly Estimate | 3-Month Estimate |
|---|---:|---:|
| LLM API usage | €100 | €300 |
| Workflow automation platform / n8n | €50 | €150 |
| Cloud hosting / database | €100 | €300 |
| Monitoring and observability | €50 | €150 |
| Data storage and backups | €25 | €75 |
| **Total** | **€325** | **€975** |

For planning purposes, this is rounded to:

> **Infrastructure, Software and API Costs: €1,000**

These estimates assume a small number of pilot users and limited usage volumes. Actual costs may increase depending on API usage, infrastructure requirements and deployment scale.

---

# 10. Contingency

A contingency of approximately **10%** is included to account for uncertainty during the pilot.

Potential sources of uncertainty include:

- Changes in requirements
- Unexpected technical issues
- AI prompt and output refinement
- Data quality issues
- Integration challenges

### Contingency Calculation

**€24,650 × 10% = €2,465**

Rounded for planning purposes:

> **Contingency: €2,500**

---

# 11. Estimated Project Delivery Cost

| Cost Category | Cost |
|---|---:|
| Direct Labour | €24,650 |
| Infrastructure, Software & APIs | €1,000 |
| Contingency | €2,500 |
| **Estimated Delivery Cost** | **€28,150** |

Rounded:

> ## **Estimated Pilot Delivery Cost: approximately €28,000**

---

# 12. Client-Facing Investment

The estimated delivery cost represents the expected cost of delivering the pilot.

A separate consulting margin is applied to account for commercial risk, subcontractor coordination, business overhead and profit.

For this initial consulting engagement, a modest **10% margin** is assumed.

### Margin Calculation

**€28,150 × 10% = €2,815**

| Item | Cost |
|---|---:|
| Estimated Delivery Cost | €28,150 |
| Consulting Margin (10%) | €2,815 |
| **Indicative Client Investment** | **€30,965** |

Rounded for planning and presentation purposes:

> # **Indicative Pilot Investment: approximately €31,000**

---

# 13. Scope Exclusions

This estimate covers a focused MVP and controlled pilot only.

The following are not included:

- Full enterprise integration with crew management systems
- Large-scale historical data migration
- Complex data engineering
- 24/7 production support
- Enterprise-wide deployment
- Custom mobile applications
- Advanced enterprise cybersecurity infrastructure
- Major commercial software licence fees
- Global rollout across multiple offices

These requirements would need to be assessed separately before a full production deployment.

---

# 14. Key Cost Drivers

The final cost of a future production implementation could be affected by:

1. **Data availability and quality**
2. **Number and complexity of enterprise integrations**
3. **AI and API usage volumes**
4. **Cybersecurity and compliance requirements**
5. **Number of users and geographical deployment scope**
6. **Required availability and support levels**

---

# 15. Conclusion

The proposed delivery model supports a lean and controlled implementation of the Crew Change Risk Copilot.

The indicative estimates are:

| Metric | Estimate |
|---|---:|
| Pilot duration | 12 weeks |
| Direct labour cost | €24,650 |
| Estimated delivery cost | ~€28,000 |
| Indicative client investment | **~€31,000** |

The recommended approach is to validate the solution through a controlled pilot before committing to a larger enterprise implementation.

> **The pilot investment of approximately €31,000 provides a basis for testing technical feasibility, operational value and user adoption before further investment in full-scale deployment.**