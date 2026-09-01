# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-01


# Crew Change Operational Risk Assessment Workflow

## 1. Overview

This document describes the final **n8n workflow** developed for the AI Capstone Project. The workflow demonstrates an AI-assisted operational decision-support process for maritime crew changes.

The workflow combines operational crew-change data, airport information, live weather data, deterministic risk calculations, and an LLM-generated assessment. The resulting assessment is stored in both **Airtable** and **Notion**.

The objective is to demonstrate how AI and workflow automation can support operations teams by transforming multiple operational signals into a structured risk briefing and a clear recommendation for human review.

---

## 2. Workflow Overview

![Final n8n Workflow](<n8n workflow Screenshot 2026-09-01 105412.png>)

### High-level process

```text
Manual Trigger
      |
      v
Retrieve Crew Change Record
      |
      v
Retrieve Airport Information
      |
      v
Retrieve Live Weather Data
      |
      v
Build Risk Assessment Input
      |
      v
Calculate Live Operational Risk
      |
      +-----------------------------+
      |                             |
      v                             v
Update Airtable Record        AI Assessment Branch
                                    |
                                    v
                              OpenAI Chat Model
                                    |
                                    v
                            Structured Output Parser
                                    |
                                    v
                                   Merge
                                    |
                                    v
                           Format AI Briefing
                              /             \
                             v               v
                    Update Airtable      Create Notion Page
```

---

## 3. Workflow Components

### 3.1 Run Crew Change Analysis

**Node type:** Manual Trigger

This node starts the workflow manually for the Proof of Concept (PoC).

For the MVP, this allows a specific crew-change record to be analysed on demand. In a production implementation, this trigger could be replaced with:

- Webhook trigger
- Scheduled trigger
- Airtable record update trigger
- API request from a user interface

---

### 3.2 Crew Change Node

**Platform:** Airtable  
**Operation:** Search Record

This node retrieves the relevant crew-change plan and operational information.

Typical data includes:

- Crew change ID
- Seafarer ID
- Rank
- Movement type
- Vessel code
- Origin airport
- Connection airport
- Destination airport
- Visa status
- Ticket status
- Arrival buffer
- Route complexity
- Vessel ETA
- Reporting deadline

This operational record forms the core input for the risk assessment.

---

### 3.3 Airport Node

**Platform:** Airtable  
**Operation:** Get Record

The Airport node retrieves airport-related information required to enrich the crew-change analysis.

This allows the workflow to combine crew logistics data with airport context.

---

### 3.4 Weather Node – Open-Meteo

**Platform:** HTTP Request  
**External API:** Open-Meteo

The workflow retrieves current weather information for the relevant operational location.

Examples of retrieved values include:

- Temperature
- Precipitation
- Wind speed
- Wind gusts
- Weather code

The weather data is then incorporated into the risk assessment input.

Using a live external API demonstrates that the workflow can combine stored operational data with dynamic external data.

---

### 3.5 Build Risk Assessment Input

**Node type:** Edit Fields / Set

This node consolidates the operational information into a structured input for the risk calculation.

Its purpose is to create a clean and standardised data object before applying the risk logic.

Typical inputs include:

- Visa/document status
- Ticket status
- Arrival buffer
- Airport disruption indicators
- Weather conditions
- Route complexity
- Vessel schedule information

This separation improves workflow clarity and makes the risk calculation easier to maintain.

---

### 3.6 Calculate Live Operational Risk

**Node type:** Code

This node applies deterministic business rules to calculate the operational risk.

The deterministic risk calculation is important because it ensures that measurable operational factors are assessed consistently.

Examples of risk drivers include:

- Pending visa verification
- Unconfirmed or quoted tickets
- Short arrival buffers
- Airport disruption
- Weather conditions

The node produces outputs such as:

- `live_operational_risk_score`
- `live_operational_risk_level`
- `live_risk_reasons`

An example output from the workflow is:

- Risk Score: **55**
- Risk Level: **High**
- Risk Reasons:
  - Visa status pending verification
  - Ticket status quoted but not confirmed
  - Arrival buffer below four hours

---

## 4. AI Assessment Branch

After the deterministic risk score has been calculated, the workflow creates a second branch for AI-assisted interpretation.

This is a deliberate design decision.

### Deterministic logic answers:

> What operational risk factors have been detected?

### AI analysis answers:

> What do these risk factors mean operationally, and what actions should be considered?

This hybrid architecture avoids relying entirely on an LLM for numerical risk scoring while using AI for contextual interpretation and decision support.

---

### 4.1 Basic LLM Chain

**AI component:** OpenAI Chat Model  
**Orchestration:** n8n Basic LLM Chain

The LLM receives the structured operational context and generates an executive-level assessment.

The prompt instructs the model to interpret the operational situation and provide:

- Executive assessment
- Key risk drivers
- Recommended actions
- AI recommendation
- Recommendation rationale
- Assessment limitation

The AI is positioned as a **decision-support assistant**, not an autonomous decision-maker.

---

### 4.2 Structured Output Parser

The Structured Output Parser ensures that the LLM response follows a predefined schema.

The expected structure includes:

```json
{
  "executive_assessment": "string",
  "key_risk_drivers": ["string"],
  "recommended_actions": ["string"],
  "ai_recommendation": "string",
  "recommendation_rationale": "string",
  "assessment_limitation": "string"
}
```

This structured approach is important because downstream workflow nodes can reliably access specific AI outputs rather than attempting to parse unstructured natural language.

---

### 4.3 Merge

The Merge node combines:

1. The original operational and risk data
2. The structured AI output

This creates a single enriched data object containing both deterministic and AI-generated information.

---

## 5. Format the AI Briefing

**Node type:** Python Code

This node transforms the structured AI response into a formatted executive briefing.

The final output includes the following sections:

### Executive Assessment

A concise summary of the overall operational situation.

### Key Risk Drivers

A bullet-point list of the factors contributing to the risk level.

### Recommended Actions

A prioritised list of suggested operational actions.

### AI Recommendation

A clear recommendation regarding the next operational step.

### Rationale

An explanation of why the recommendation was made.

### Assessment Limitation

A transparency statement explaining that the assessment is based on the available operational data.

The formatted briefing is stored as:

- `ai_risk_briefing`
- `ai_executive_assessment`
- `ai_key_risk_drivers`
- `ai_recommended_actions`
- `ai_recommendation`
- `ai_recommendation_rationale`
- `ai_assessment_limitation`

---

## 6. Airtable Output

### Update Airtable AI Assessment

**Platform:** Airtable  
**Operation:** Update Record

The workflow writes the AI-generated assessment back into the original crew-change record.

This ensures that the operational database contains both:

- The deterministic risk assessment
- The AI-generated executive interpretation

Example fields include:

| Field | Purpose |
|---|---|
| `live_operational_risk_score` | Numerical operational risk score |
| `live_operational_risk_level` | Low / Medium / High classification |
| `live_risk_reasons` | Deterministic explanation of risk factors |
| `ai_risk_briefing` | Full formatted AI briefing |
| `ai_recommendation` | AI recommendation |
| `ai_recommendation_rationale` | Explanation supporting the recommendation |

This creates a persistent audit trail within the operational dataset.

---

## 7. Notion Output

### Create a Page

**Platform:** Notion  
**Operation:** Create Page

A second branch sends the formatted assessment to Notion.

Each execution creates a new page within the designated **Crew Change Reports** parent page.

The page title follows the format:

```text
Crew Change Risk Briefing - CC-XXXX
```

The Notion page contains a structured executive report, including:

- AI Operational Risk Assessment
- Executive Assessment
- Key Risk Drivers
- Recommended Actions
- AI Recommendation
- Rationale
- Assessment Limitation

This demonstrates a useful separation between:

- **Airtable:** structured operational data storage
- **Notion:** human-readable management reporting

---

## 8. Example Assessment

An example AI-generated assessment from the workflow was:

> The crew change operation carries a high operational risk level due to pending visa status, unconfirmed ticket status, and limited arrival buffer.

### Key risk drivers

- Visa status pending verification
- Ticket status quoted but not confirmed
- Arrival buffer below four hours

### Recommended actions

1. Request immediate verification of visa status.
2. Confirm ticket status to ensure validity.
3. Evaluate options for increasing the arrival buffer.

### AI recommendation

> Human review is recommended due to the high operational risk level.

---

## 9. Architecture and Design Rationale

The workflow follows a **hybrid intelligence architecture**.

### Layer 1: Operational Data

Structured crew-change and logistics data is retrieved from Airtable.

### Layer 2: External Context

Live weather information is retrieved through the Open-Meteo API.

### Layer 3: Deterministic Rules

A Code node applies transparent business rules to calculate an operational risk score.

### Layer 4: Generative AI

An LLM interprets the operational context and produces an executive assessment and recommended actions.

### Layer 5: Human Review

The AI recommendation supports human decision-making rather than replacing operational judgement.

### Layer 6: Knowledge and Reporting

Results are stored in:

- Airtable for structured operational records
- Notion for readable executive briefings

---

## 10. Key AI Consulting Principles Demonstrated

This PoC demonstrates several important AI integration principles.

### Hybrid AI design

The solution combines deterministic rules with generative AI rather than relying exclusively on an LLM.

### Structured AI output

The Structured Output Parser ensures predictable machine-readable responses.

### Human-in-the-loop

The workflow can explicitly recommend human review for higher-risk situations.

### Explainability

Risk reasons and AI rationale are retained alongside the recommendation.

### Data enrichment

Operational data is enriched using an external weather API.

### System integration

The workflow connects multiple platforms:

- Airtable
- Open-Meteo
- OpenAI
- Notion
- n8n

---

## 11. Current PoC Scope

The current implementation is designed as a Proof of Concept and MVP demonstration.

Current characteristics include:

- Manual workflow execution
- Single crew-change analysis per execution
- Rule-based operational risk calculation
- AI-generated executive assessment
- Airtable persistence
- Notion report generation
- Human-review recommendation

---

## 12. Potential Future Enhancements

Possible next steps include:

1. **User Interface**
   - Build a React/Next.js or Streamlit front end.
   - Allow users to select and analyse crew changes visually.

2. **Automated Triggers**
   - Trigger reassessment when operational data changes.

3. **Real-time Flight Data**
   - Integrate live flight status and disruption APIs.

4. **Advanced Risk Modelling**
   - Replace or supplement fixed scoring rules with predictive models.

5. **Alerting**
   - Automatically notify operations teams when High-risk cases are detected.

6. **Human Feedback Loop**
   - Capture reviewer decisions and use them to improve future risk logic.

7. **Batch Processing**
   - Analyse multiple upcoming crew changes automatically.

8. **Management Dashboard**
   - Integrate workflow outputs into Tableau or a dedicated operational dashboard.

---

## 13. Conclusion

The Crew Change Operational Risk Assessment workflow demonstrates how AI can be integrated into a real-world maritime operations process.

The solution does not simply generate text with an LLM. Instead, it combines:

**Operational Data + External Context + Deterministic Risk Logic + Generative AI + Human Review + Automated Reporting**

The resulting workflow provides a practical example of an AI-enabled decision-support system that can identify operational risks, explain their significance, recommend actions, and create structured reports across multiple business systems.

This architecture provides a strong foundation for future development into a production-grade crew-change risk management platform.

