# ROI & Risk Assessment — Crew Change Risk Copilot

- Round: 2
- Status: Draft business-case model for pilot validation

---

## 1. Executive Summary

The Crew Change Risk Copilot is a human-in-the-loop decision-support system intended to help crewing teams identify upcoming crew-change cases that may require earlier attention. It does not replace the professional judgement of Crew Managers and does not autonomously make operational decisions.

The existing Round 1 cost model estimated an indicative client investment of approximately **€31,000** for a 12-week controlled MVP/pilot. This is used as the baseline for the Round 2 assessment.

However, the POC also demonstrated additional technical complexity: the n8n implementation proved more complex than initially expected and was not considered a feasible foundation for the MVP. The original €31,000 should therefore be treated as a baseline estimate rather than a firm production cost.

The clearest quantifiable financial benefit identified at this stage is the avoidance of costs associated with failed or disrupted crew-change itineraries. The base model uses **€1,250 avoided cost per prevented problematic case**, within the identified €1,000–€1,500 range.

Other benefits — including Crew Manager productivity, reduced operational firefighting, reduced stress, improved seafarer experience and potential retention benefits — are strategically relevant but are not monetised in the base ROI calculation. These should be measured during the pilot.

---

## 2. Cost Assessment

### 2.1 Round 1 Baseline Cost

| Cost category | Round 1 estimate |
|---|---:|
| Direct labour | €24,650 |
| Infrastructure, software & APIs | €1,000 |
| Contingency | €2,500 |
| **Estimated delivery cost** | **€28,150** |
| Consulting margin (10%) | €2,815 |
| **Indicative client investment** | **€30,965 (~€31,000)** |

The original estimate assumed a focused 12-week controlled pilot, a small group of operational users, limited enterprise integration, a lightweight UI and human oversight.

### 2.2 Revised Round 2 Cost View

The POC demonstrated that workflow orchestration and integration were more complex than initially anticipated. This creates a risk to both schedule and cost.

For planning purposes, the base-case ROI model therefore uses:

> **Initial implementation investment: €35,000**

This is a planning assumption rather than a supplier quotation. It represents the Round 1 baseline plus a modest allowance for additional implementation complexity. The final number should be validated before pilot approval.

### 2.3 Ongoing Operating Costs

The Round 1 infrastructure estimate was approximately €325 per month:

| Cost | Monthly estimate |
|---|---:|
| LLM API usage | €100 |
| Workflow/orchestration | €50 |
| Cloud hosting/database | €100 |
| Monitoring & observability | €50 |
| Storage & backups | €25 |
| **Total** | **€325** |

For the ROI model, ongoing operating costs are rounded to **€4,000 per year**.

Actual production costs may be higher depending on API usage, user numbers, integrations, security requirements, support and deployment scale.

---

## 3. Business Value

### 3.1 Direct Cost Avoidance

A failed or disrupted crew-change itinerary can create additional costs such as:

- replacement air tickets;
- hotel accommodation;
- additional salary or overtime;
- emergency replacement arrangements;
- additional administrative and coordination effort.

Base assumption:

> **€1,250 average avoidable cost per problematic crew-change case.**

### 3.2 Operational Productivity

The Copilot may help Crew Managers:

- identify higher-risk cases earlier;
- focus attention on exceptions;
- understand why a case was flagged;
- bring relevant operational information together;
- receive concise risk briefings.

No monetary productivity benefit is included in the base ROI calculation because no measured baseline data is currently available. This should be measured during the pilot.

### 3.3 Workforce and Seafarer Value

Potential strategic benefits include:

- less repetitive firefighting and operational pressure for Crew Managers;
- reduced stress associated with avoidable failed crew changes;
- improved experience for seafarers during joining and repatriation;
- potential improvement in crew satisfaction and retention.

These benefits are not monetised in the base ROI model because sufficient evidence is not yet available to assign a reliable euro value.

### 3.4 Benefits Excluded from Base ROI

| Potential benefit | Treatment |
|---|---|
| Crew Manager time savings | Not monetised; measure during pilot |
| Reduced firefighting/stress | Not monetised |
| Improved seafarer experience | Not monetised |
| Crew retention benefit | Not monetised |
| Reduced absence/turnover | Not monetised |
| Better operational planning | Not monetised |

This deliberately conservative approach avoids overstating the business case.

---

## 4. ROI Analysis

### 4.1 Formula

> **ROI = (Net Benefit / Total Cost) × 100**

Where:

> **Net Benefit = Total Benefit − Total Cost**

The calculations below use direct avoided-case savings only. Therefore, the result represents a conservative financial view.

### 4.2 Base-Case Assumptions

| Assumption | Base case |
|---|---:|
| Initial investment | €35,000 |
| Ongoing operating cost | €4,000/year |
| Avoided problematic crew changes | 15/year |
| Avoided cost per case | €1,250 |
| Annual direct benefit | €18,750 |
| Productivity/retention benefit | Excluded from base ROI |

### 4.3 12-Month ROI

**Total cost**

€35,000 + €4,000 = **€39,000**

**Total benefit**

15 × €1,250 = **€18,750**

**Net benefit**

€18,750 − €39,000 = **−€20,250**

**ROI**

(−€20,250 / €39,000) × 100 = **−51.9%**

#### Interpretation

The solution does not recover its initial investment within 12 months through direct avoided crew-change costs alone under the conservative base assumptions.

This means the business case depends on validating additional value streams, particularly operational productivity.

### 4.4 36-Month ROI

**Total cost over 36 months**

€35,000 + (€4,000 × 3) = **€47,000**

**Total benefit over 36 months**

€18,750 × 3 = **€56,250**

**Net benefit**

€56,250 − €47,000 = **€9,250**

**ROI**

(€9,250 / €47,000) × 100 = **19.7%**

#### Interpretation

Under the conservative base assumptions, the project becomes financially positive over three years through direct cost avoidance alone.

---

## 5. Sensitivity Analysis

Assumptions: €35,000 initial investment, €4,000 annual operating cost and €1,250 avoided cost per case.

| Avoided cases/year | Annual benefit | 12-month ROI | 36-month ROI |
|---:|---:|---:|---:|
| 5 | €6,250 | -84.0% | -63.5% |
| 10 | €12,500 | -68.0% | -20.2% |
| 15 | €18,750 | -51.9% | 19.7% |
| 20 | €25,000 | -35.9% | 59.6% |
| 25 | €31,250 | -19.9% | 99.5% |
| 30 | €37,500 | -3.8% | 139.4% |

### Key Message

Direct cost avoidance alone produces a relatively slow payback. The pilot should therefore measure productivity gains rather than assume them.

---

## 6. Break-Even Note

Using the 12-month cost assumption:

**€39,000 total first-year cost / €1,250 per avoided case = 31.2 cases**

Therefore, approximately **32 avoided problematic crew-change cases** would be required to recover first-year costs through direct case savings alone.

This reinforces the importance of measuring additional productivity and workforce benefits during the pilot.

---

## 7. Risk Assessment

| ID | Risk | Category | Likelihood (1–5) | Impact (1–5) | Mitigation |
|---|---|---|---:|---:|---|
| R1 | AI incorrectly flags a case or misses a relevant risk | Technical/Operational | 3 | 5 | Human review remains mandatory; test representative scenarios; monitor false positives and false negatives |
| R2 | Poor or incomplete input data produces unreliable results | Technical | 4 | 4 | Validate required inputs; show missing-data warnings; improve data quality |
| R3 | Users rely on AI output without sufficient professional judgement | Ethical/Operational | 3 | 5 | Human-in-the-loop approval; clear decision-support boundaries |
| R4 | Personal data is processed or retained inappropriately | Regulatory/GDPR | 3 | 5 | Data minimisation, access controls, retention rules and compliance review |
| R5 | AI regulatory obligations are misunderstood | Regulatory | 2 | 5 | Formal compliance and risk classification review before production |
| R6 | System inputs, outputs or records cannot be traced | Technical/Governance | 3 | 4 | Log and monitor system inputs, outputs and relevant records for traceability |
| R7 | UI/UX is difficult to use and adds workload | Operational | 3 | 4 | Create a clear, intuitive UI; test with operational users and refine |
| R8 | Implementation complexity increases cost and timeline | Technical/Commercial | 4 | 4 | Keep MVP scope small; simplify architecture; phased delivery; contingency and pilot go/no-go gate |

### Priority Risks

The most important risks are AI reliability, data quality and implementation complexity. The controlled pilot should validate these before any larger production investment.

---

## 8. Pilot Validation Priorities

The pilot should replace assumptions with measured evidence.

| Metric | Purpose |
|---|---|
| Problematic crew changes identified early | Tests core solution value |
| Problematic cases successfully avoided | Measures direct financial benefit |
| Average cost avoided per case | Validates €1,250 assumption |
| Time spent reviewing cases | Measures productivity |
| Time saved per Crew Manager | Supports additional ROI calculation |
| False-positive rate | Tests trust and usability |
| False-negative rate | Tests reliability |
| User adoption | Tests operational viability |
| User satisfaction | Tests practical usefulness |
| System exceptions and errors | Supports monitoring and improvement |

---

## 9. Conclusion

The Crew Change Risk Copilot has a plausible business case, but the current evidence does not justify presenting a guaranteed financial return.

The strongest directly measurable value is potential avoidance of failed or disrupted crew-change costs. Under the conservative base case of 15 avoided problematic cases per year at €1,250 per case, the model produces a negative 12-month ROI but a positive 36-month ROI of approximately **19.7%**.

The most important next step is to validate additional operational value during the pilot, particularly time saved for Crew Managers and reductions in repetitive exception-handling work.

> **Recommended approach: Run a controlled pilot, measure the value, and use measured results to support the full-deployment investment decision.**
