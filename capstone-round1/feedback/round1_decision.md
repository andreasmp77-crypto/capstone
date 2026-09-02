# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-02
---

# Round 1 Decision

## Industry/Use Case Review

The Round 1 research and Proof of Concept focused on the maritime ship-management and crew-management sector.

The selected primary use case, the **Crew Change Risk Copilot**, addresses the challenge of monitoring multiple operational factors that may affect planned crew changes and identifying cases that require human attention.

The Round 1 work included:

- Sector and problem research
- Opportunities and risks analysis
- Use case assessment
- User stories
- Data research and Tableau dashboards
- An n8n automation Proof of Concept
- AI-generated crew change risk briefings
- LangSmith monitoring and observability testing
- Indicative implementation cost and timeline

The Proof of Concept demonstrated that a hybrid approach combining deterministic risk assessment with AI interpretation can produce structured risk information and concise operational briefings.

The feedback received during the Round 1 review was positive and supported continuing with the selected industry and use case.

---

## Keep or Change Decision

**Decision: KEEP**

The maritime ship-management industry and the **Crew Change Risk Copilot** remain suitable for further development.

The project has a clear operational problem, a defined target user, relevant data sources and a functioning Proof of Concept.

However, the next development stage should narrow the scope and focus on improving the operational workflow rather than adding unnecessary functionality.

---

## Rationale

The decision to continue is supported by the following points:

- The selected use case addresses a realistic operational challenge within crew management.
- The human-in-the-loop approach remains appropriate for operational decision support.
- The Proof of Concept successfully demonstrated the combination of deterministic risk assessment and AI-generated interpretation.
- The n8n workflow provides a practical implementation environment for continued development.
- The project has a clear path for incremental improvement through future sprints.

The teacher's feedback also highlighted that the existing PoC workflow is already substantial and should not be unnecessarily expanded.

Therefore, the next phase should focus on improving the existing workflow and making it more operationally relevant rather than introducing a separate UI or additional complex features.

The following areas should be incorporated into the future development approach:

- Clear and prioritised User Stories
- Definition of Done
- Acceptance Criteria
- Sprint-based development
- A realistic timeline

---

## Next Steps

The following improvements were agreed for the next development stage.

### 1. Refine the Product Backlog

Further development should be structured around:

- User Stories
- Acceptance Criteria
- Definition of Done
- Sprint planning
- Timeline and prioritisation

This will provide a clearer link between user needs, technical development and project deliverables.

### 2. Extend the n8n Workflow

The existing n8n workflow should remain the main implementation tool.

The next iteration should extend the PoC to simulate a more realistic operational scenario.

Instead of manually analysing a single crew-change case, the workflow should:

1. Generate a batch of approximately 5–10 new crew-change cases using a random data generator.
2. Use the new cases as the trigger for the workflow.
3. Analyse all new crew-change cases.
4. Identify and assess potential operational risks.
5. Update the operational database with the results.
6. Generate a concise summary covering all newly analysed cases.
7. Send the summary for review by the Crew Manager.

Support discussion of priority cases during the morning briefing with the crewing team.

The objective is to move from a **single-case demonstration** toward a more realistic **management-by-exception workflow**. This will be used to support discussion of priority cases during the morning briefing with the crewing team.

### 3. Improve the Reporting Output

The reporting output should evolve from an individual crew-change briefing to a concise management summary.

The summary should help answer:

- How many new crew-change cases were analysed?
- Which cases require attention and why?
- How many cases fall into each risk level?
- What are the key risk drivers?
- Which cases should be prioritised during the morning briefing?

This will better reflect the daily operational workflow of a Crew Manager and crewing team.

### 4. No UI Development at This Stage

Based on the feedback received, a dedicated user interface is not required at this stage.

Development effort should instead focus on:

- workflow logic;
- batch processing;
- risk prioritisation;
- concise management reporting;
- human review.

A UI can remain a potential future enhancement once the operational workflow and underlying logic have been further validated.

### 5. Preserve the n8n Workflow

The n8n workflow should remain the primary implementation tool for the project.

At the end of the course, the final workflow should be downloaded and securely stored together with the project documentation to ensure that the complete implementation can be retained independently of the course environment.

---

## Round 1 Outcome

Round 1 confirms that the **Crew Change Risk Copilot** is a viable use case for continued development.

The project will proceed with the existing industry and primary use case while narrowing the next development stage around a more realistic operational workflow:

> **New crew-change cases → Batch risk analysis → Prioritisation → Database update → Concise management summary → Human review and team discussion**

The next phase will focus on incremental improvement through defined User Stories, Acceptance Criteria, Definition of Done and sprint-based development.
