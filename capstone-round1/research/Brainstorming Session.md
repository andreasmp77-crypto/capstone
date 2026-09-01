# Brainstorming Session

### **Initial conclusion**

**Idea A is the strongest starting point**, but I would narrow and rename it:

> **Crew Change Risk Copilot**
A human-in-the-loop decision-support tool that gives crewing officers an early risk briefing for each planned crew change—covering travel disruption, connection time, visa/document readiness, cost exposure, and last-mile coordination.
> 

This fits both your **conference role** and the **capstone rubric** unusually well.

You are listed as a panellist in Session 1, **“The Logistics of Talent — Sourcing, Travel, and the AI Revolution,”** specifically for the panel **“Technology in the Driver’s Seat: Rethinking the Last Mile of Crew Change.”** The conference highlights rising travel costs, visa friction, travel risk, predictive scheduling, and automated logistics as central topics.[Conference agenda](https://cyprusshippingevents.com/2nd-csn-northern-european-crewing-conference/)

### **The useful mental model**

Think of your capstone as building a **lighthouse, not an autopilot**:

The system does **not** book travel or decide who joins the vessel.

It shines a light on risks that a crewing officer might otherwise notice too late.

The human remains responsible for the final decision.

That positioning addresses Chleo’s fear about transparency and reflects the conference theme: **digital efficiency combined with human reliability**.

### **Comparison of the four ideas**

| **Idea** | **Conference fit** | **Feasibility** | **Capstone fit** | **Main concern** |
| --- | --- | --- | --- | --- |
| **A. Crew Travel Copilot** | Excellent | Strong if scoped narrowly | Excellent | Live flight, visa, and pricing APIs may be difficult |
| **B. Talent Pipeline Radar** | Strong | Moderate | Strong | Bias, explainability, and employment-related AI regulation |
| **C. Welfare & Claims Assistant** | Strong for Sessions 2–3 | Moderate–low | Strong analytically | Health data, GDPR sensitivity, and difficult datasets |
| **D. Crew Rotation Planning** | Strong | Low if fully implemented | Potentially strong | Too many constraints and sensitive employment decisions |

#### **1. Idea A — Crew Travel Copilot**

**Strengths**

Directly aligned with your panel topic.

Easy to explain to shipowners, managers, travel agencies, and crewing companies.

Produces visible outputs suitable for Power BI.

Naturally supports an n8n alert workflow.

LangSmith can show exactly what information the AI received and how it produced the briefing.

Easier to position as low-risk **decision support**, provided it does not autonomously book or reject arrangements.

**Weakness**

A complete system would require reliable access to:

live flight schedules and prices;

historical delay data;

visa and immigration requirements;

vessel schedules and port-agent information;

company travel policies.

Trying to integrate all of this would be too ambitious.

**Recommended response**

Use public historical flight-delay data plus a **synthetic crew-change planning dataset**. Treat visa status, vessel ETA, port transfer, and traveller-document readiness as structured mock inputs.

The brief explicitly allows public or synthetic data.

#### **2. Idea B — AI Talent Pipeline Radar**

This is a good **dashboard concept**. It could show:

vacancy coverage by rank;

qualified candidates per vacancy;

certificate expiry exposure;

average days to fill;

nationality or sourcing-region concentration;

vacancies at risk of late coverage.

However, the AI component must be handled carefully. If it ranks individual candidates or influences recruitment decisions, it moves toward an employment-related AI system with substantial bias and EU AI Act concerns.

A safer version would analyse **workforce capacity**, not score people:

> “We may have a Second Engineer shortage in six weeks”
> 

rather than:

> “Candidate X is unsuitable.”
> 

This is commercially relevant, but less directly connected to your specific last-mile panel than Idea A.

#### **3. Idea C — Crew Welfare & Claims Insight Assistant**

This fits the conference’s “Cost of Health,” fatigue, mental health, welfare, and P&I themes. These are clearly important industry concerns, with recent industry discussion linking fatigue, rest, operational crewing, and safe vessel operation.[BIMCO survey](https://www.bimco.org/news-insights/bimco-news/2026/07/13-crew-survey)

But it is a difficult first capstone choice because:

health information may be **special-category personal data** under GDPR;

claims data is commercially sensitive;

public maritime claims datasets may be difficult to obtain;

mental-health risk predictions could easily be overstated or misused;

proving whether patterns are meaningful requires more analytical rigour.

It could become a strong future project, but its legal and ethical burden could consume much of your limited build time.

#### **4. Idea D — Crew Rotation Planning**

I would label this **Idea D**, because there are currently two Idea Cs.

This may have the greatest long-term business value, but it is also the most complex. A real rotation engine must reconcile:

rank and vessel requirements;

certificates and endorsements;

medical validity;

availability and leave;

contract duration;

nationality and visa restrictions;

client preferences;

budget;

travel feasibility;

fatigue and rest considerations;

collective agreements and company policies.

It resembles solving a large puzzle where every piece has rules attached. AI can help explain or flag the plan, but the core allocation problem may need **constraint optimisation**, not just a large language model.

There is also a significant compliance concern if the application ranks people or substantially influences employment assignments. For a beginner-friendly capstone, this is likely too wide unless reduced to one small capability, such as:

> **Rotation Readiness Checker:** flag upcoming relief plans with missing documents, insufficient overlap, unavailable relief crew, or travel-window risks.
> 

That smaller version could be feasible.

## **My recommendation: select Idea A, borrowing one narrow element from D**

### **Proposed capstone concept**

#### **Crew Change Risk Copilot**

**One-sentence pitch:**

> An explainable decision-support assistant that reviews a planned crew change, identifies travel and readiness risks early, explains why each risk was flagged, and sends the crewing officer an actionable briefing.
> 

#### **Important scope boundary**

It should **not**:

select the “best” seafarer;

make employment decisions;

autonomously purchase tickets;

claim to provide authoritative immigration advice;

guarantee that a crew change will succeed.

It should help a qualified professional ask better questions earlier.

### **A simple end-to-end scenario**

Imagine this record:

Vessel: *MV Example*

Joining port: Hamburg

Vessel ETA: 18 September, 14:00

Seafarer origin: Manila

Flight arrival: 18 September, 09:45

Connection: 55 minutes in Istanbul

Visa/document status: pending verification

Port transfer estimate: 90 minutes

Historical route delay risk: elevated

The copilot might produce:

> **Overall status: High risk**
Main reasons: short transfer margin, elevated connection-delay exposure, and unverified document status.
Suggested human actions: verify visa/document eligibility, request a safer routing, confirm vessel ETA tolerance, and alert the port agent.
> 

Notice the transparency: the result is not merely a mysterious red badge. It says **why** it is red.

---

## **How it maps to Round 1**

### **1. Research pack**

Research:

crew-change logistics;

flight disruption and missed-connection exposure;

visa and document friction;

last-mile port transfers;

costs of delayed joining and extended contracts;

operational risks of last-minute planning.

Present 2–3 use cases:

**Crew Change Risk Copilot** — recommended POC.

**Talent Capacity Radar** — future workforce-planning opportunity.

**Rotation Readiness Checker** — future operational-planning opportunity.

This satisfies the requirement to propose 2–3 use cases without trying to build all three.

### **2. Dataset**

Use two layers:

**Public historical flight-delay data** for route or airport-level disruption indicators.

**Synthetic crew-change records** for seafarer origin, vessel ETA, connection time, document readiness, port transfer, and estimated cost.

This is realistic enough to demonstrate the logic without pretending you possess live operational data.

### **3. Power BI dashboard**

Possible stakeholder metrics:

Planned crew changes

High-risk crew changes

Average travel cost per change

Changes with tight connection windows

Document or visa readiness rate

Arrival-to-vessel buffer time

Risk exposure by airport, port, route, or month

The dashboard is the **control tower**; it shows the overall operation. The copilot is the **risk briefing officer**; it explains one specific case.

### **4. n8n POC**

A manageable workflow:

New crew-change record
        ↓
Validate required fields
        ↓
Apply transparent risk rules
        ↓
Ask the LLM to generate a plain-language briefing
        ↓
Send alert to the crewing officer
        ↓
Store output for monitoring

The rules should identify the risk; the LLM should primarily **explain and summarise it**. This prevents the language model from inventing the underlying risk score.

Memory aid:

> **Rules calculate; AI communicates; humans decide.**
> 

### **5. LangSmith monitoring**

Monitor:

input data received;

identified risk factors;

generated explanation;

whether required warnings were included;

latency and token usage;

consistency across a small test dataset;

cases where the explanation contradicts the structured score.

This directly supports the transparency story.

### **6. Cost and timeline**

The Round 1 estimate could cover a small pilot:

dashboard and data preparation;

n8n workflow;

LLM usage;

monitoring;

travel-data integration;

testing and staff training.

All figures must be labelled as assumptions—not presented as proven savings.

## **Conference positioning**

There is one strategic caveat: the conference includes travel-sector specialists and a presentation about AI and crew travel. You should avoid presenting yourself as replacing travel agencies or building a full competing booking platform.

A stronger industry message is:

> “The goal is not to replace the travel professional or crewing officer. It is to create a shared, explainable risk picture before the crew change becomes a crisis.”
> 

That invites travel agencies, ship managers, port agents, and technology providers into the solution rather than placing them on the defensive.

### **Possible panel talking point**

> “In crew travel, the first useful AI application may not be autonomous booking. It may be earlier visibility. If the crewing officer, travel partner, and port agent can see the same reasons why a crew change is becoming risky, they can intervene before the cost and welfare consequences escalate.”
> 

### **Possible provocative question for the panel**

> “Should we measure crew-travel technology by how many bookings it automates—or by how many high-risk crew changes it helps humans prevent?”
> 

### **Recommended working choice**

**Sector:** Maritime shipping / ship management

**Starting company size:** Medium ship-management company

**Primary use case:** Crew Change Risk Copilot

**Primary users:** Crewing officers and crew travel coordinators

**Decision-maker:** Crew manager, operations director, or CEO

**Conference hook:** Last-mile crew-change risk and human-centred AI

**MVP principle:** One crew-change record enters; one explainable risk briefing comes out

#### **First check-in**

Before we design the formal use case, decide which business problem should be at its centre:

**Preventing failed or delayed crew changes**

**Reducing crew-travel cost**

**Reducing last-minute workload for crewing officers**

**Protecting seafarer welfare during travel**

My recommendation is **#1 as the primary problem**, with cost, workload, and welfare presented as secondary benefits.