# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-01
---

>⚓
This document establishes the Round 1 sector context for the proposed Crew Travel Copilot. It separates externally sourced facts from the project’s illustrative company assumptions.


## 1. Executive summary

Maritime transport is a critical global industry: UN Trade and Development reports that around 80% of international trade in goods by volume is carried by sea. Safe shipping depends not only on vessels and technology, but also on qualified, rested seafarers and effective shore-based management.

A crew change is the coordinated process of replacing seafarers who are completing their service with colleagues joining the vessel. The process connects ship schedules, ports, immigration requirements, crew documentation, flights, ground transport, accommodation where needed, training requirements, payroll reconciliation, agents and shore-based crewing teams. A disruption in one part of this chain can delay or prevent the change.

For Round 1, the project examines whether a medium-sized ship manager could use transparent decision support to identify crew-change plans that deserve earlier human attention. It does not claim to predict individual flight outcomes or make employment, immigration or travel decisions.

## 2. Sector definition

### Maritime transport

Maritime transport moves cargo and passengers by sea and connects exporters, importers, ports and inland logistics networks. Its economic significance is substantial: around 80% of the volume of international trade in goods is carried by sea. [UNCTAD — Review of Maritime Transport](https://unctad.org/topic/transport-and-trade-logistics/review-of-maritime-transport)

UNCTAD reported that seaborne trade grew by 2.2% in 2024, while longer routes caused ton-miles to increase by 5.9%. This illustrates how geopolitical disruption and rerouting can increase operational complexity even when cargo volumes grow more slowly. [UNCTAD — Review of Maritime Transport 2025](https://unctad.org/publication/review-maritime-transport-2025)

### Ship management

A ship manager operates vessels on behalf of an owner or assumes defined operational responsibilities. Depending on the contract, these responsibilities may include:

- safe vessel operation;
- crewing and training;
- maintenance and technical management;
- regulatory compliance;
- procurement and supplier coordination;
- voyage and port support;
- safety-management documentation and reporting;
- commercial management, including chartering support, where included in the management agreement.

The International Safety Management Code provides an international standard for safe ship management and operation and requires companies to establish and maintain a safety management system. It covers company responsibilities, resources and personnel, shipboard operating plans, emergency preparedness, reporting and review. [IMO — International Safety Management Code](https://www.imo.org/en/ourwork/humanelement/pages/ismcode.aspx)

This project focuses on the ship manager’s crew-management function, particularly crew rotations. This includes arranging replacements, coordinating travel for joining seafarers and organising the repatriation of off-signing seafarers.

The IMO also describes the human element as a shared responsibility involving seafarers, shore-based management, companies, regulators and other parties. This supports a human-centred approach rather than replacing professional judgement with automation. [IMO — Human Element](https://www.imo.org/en/ourwork/humanelement/pages/default.aspx)

## 3. Illustrative company profile

> 🧭
The profile below is a project assumption for Round 1. It is not a description of a named company or a sourced industry average. It should be validated during client discovery.

The assumed client is a medium-sized third-party ship manager with:

- approximately 25–50 managed vessels;
- several hundred active and relief seafarers;
- an 8–15-person crewing or marine-personnel team;
- crew sourced from several countries;
- voyages and crew changes across multiple regions;
- a mixture of spreadsheets, email, travel-agent systems and operational databases;
- limited capacity for a large custom-software programme;
- a requirement for clear human oversight and auditability.

### Relevant stakeholders

| Stakeholder | Main concern |
| --- | --- |
| Chief executive or managing director | Service reliability, cost, reputation and client retention |
| Head of crewing | Safe, compliant and timely crew rotations |
| Crewing officer | Documents, travel coordination, agents and exception handling |
| Vessel superintendent or operations team | Vessel schedule and operational continuity |
| Master | Safe manning and readiness of the onboard team |
| Seafarer | Safe travel, clear information, timely relief and welfare |
| Travel partner | Flight availability, ticketing, rebooking and disruption response |
| Port agent | Local formalities and transport between airport, hotel and vessel |
| Crewing agent | Local recruitment and placement of competent seafarers, document coordination and compliance with applicable recruitment requirements |

## 4. What is a crew change?

A crew change replaces one or more seafarers who are leaving a vessel (repatriations) with colleagues who are joining it (joiners). Although it sounds like a staffing handover, operationally it is an international, time-sensitive and complex logistics process.

A simplified joining process is:

1. The company identifies who is due to join or leave the vessel.
2. The vessel schedule and suitable joining port are confirmed.
3. The crewing team checks employment, passport, visa, medical and training readiness.
4. Flights and, where necessary, hotels are arranged.
5. A port agent coordinates immigration, local transport and vessel access.
6. The joining seafarer travels through one or more airports.
7. The seafarer reaches the port before the reporting deadline.
8. The handover occurs and the off-signing seafarer begins the return journey.

The duration of seafarers’ contracts varies. IMO guidance notes that seafarers typically work between four and six months on board, followed by a period of leave. [IMO — Crew changes and repatriation FAQ](https://www.imo.org/en/mediacentre/hottopics/pages/faq-on-crew-changes-and-repatriation-of-seafarers.aspx)

The International Chamber of Shipping’s crew-change protocols illustrate the number of parties involved: shipping companies, crewing agencies, seafarers, ports, airports, airlines, authorities and agents all participate in the end-to-end process. [ICS — Crew change process and protocols](https://www.ics-shipping.org/current-issue/the-covid-19-pandemic-the-crew-change-crisis)

To put this into perspective, during the height of the COVID-19 pandemic in August 2020, it was estimated that over 150,000 seafarers required immediate repatriation, with as many as 250,000 serving on extended crew contracts who were overdue to return home, in addition to those needing to join their ships to work and keep the world fleet moving. [ICS — Crew change process and protocols](https://www.ics-shipping.org/current-issue/the-covid-19-pandemic-the-crew-change-crisis)

## 5. Why crew changes matter

### Safety and fatigue

Crew changes help ensure that seafarers are relieved at the end of their service and that vessels continue to operate with appropriately qualified personnel. IMO guidance connects extended service and fatigue with physical and mental-health risks and increased risk of involvement in marine incidents. [IMO — Crew changes and repatriation FAQ](https://www.imo.org/en/mediacentre/hottopics/pages/faq-on-crew-changes-and-repatriation-of-seafarers.aspx)

The IMO continues to treat fatigue and work/rest compliance as safety-management priorities. [IMO — Seafarer fatigue, work and rest hours](https://www.imo.org/en/MediaCentre/PressBriefings/pages/Seafarer-fatigue-work-hours-harassment.aspx)

### Labour obligations and welfare

The Maritime Labour Convention, 2006 covers major aspects of seafarers’ employment and living conditions, including hours of work and rest, leave, repatriation, medical care, health and safety, and recruitment and placement services. [ILO — Maritime Labour Convention, 2006](https://www.ilo.org/international-labour-standards/maritime-labour-convention-2006)

This means crew-change planning is not merely an administrative convenience. It is connected with welfare, safe manning, contractual arrangements and regulatory responsibilities.

### Operational continuity

If a replacement does not arrive, the company may need to extend the service of the seafarer on board, move the change to a later port, purchase replacement tickets, arrange accommodation, incur overlapping employment costs, change agents or revise the rotation plans for both the joining and off-signing seafarers. In severe cases, the disruption can affect vessel schedules, safe manning or client confidence.

These potential effects are logically derived from the process and should be treated as project hypotheses until validated through interviews or real anonymised operational records.

## 6. Why crew changes fail or become delayed

Crew-change disruption is normally caused by a combination of factors rather than one isolated event.

### Travel disruption

- flight delay or cancellation;
- missed connection;
- insufficient connection time;
- limited alternative flights;
- baggage or airport disruption;
- weather or air-traffic restrictions.

### Documentation and regulatory readiness

- passport or medical certificate validity;
- visa or transit requirements;
- missing company or agent letters;
- immigration restrictions;
- inconsistent or late documentation;
- last-minute changes in local requirements.

### Vessel and port uncertainty

- changing vessel estimated time of arrival;
- berth or terminal changes;
- port restrictions;
- short notice from the vessel or client;
- insufficient airport-to-port transfer time;
- delayed confirmation from the local agent.

### Organisational causes

- information spread across email, spreadsheets and different systems;
- unclear ownership of follow-up actions;
- late escalation;
- incomplete handovers between team members;
- reliance on individual experience rather than a shared checklist;
- high exception-handling workload;
- medical or personal emergencies affecting a seafarer.


>💡
**The project’s central hypothesis is not that AI can eliminate disruption. It is that earlier, clearer identification of combined warning signs may help a crewing officer intervene sooner.**


## 7. Evidence from the crew-change crisis

During the COVID-19 period, crew-change restrictions exposed how dependent the process is on coordination between governments, shipping companies, airports, airlines, ports and agents. IMO reported in 2020 that approximately 150,000 seafarers needed to be changed over each month to support safety, health, welfare and fatigue compliance. [IMO — Crew-change protocols](https://www.imo.org/en/mediacentre/pressbriefings/pages/15-crew-changes-.aspx)

This figure is included as historical context, not as a current estimate for 2026. The pandemic was exceptional, but it demonstrated the operational and human consequences of barriers in the crew-travel chain.

## 8. Data and digitalisation context

The sector is becoming more digital. IMO made Maritime Single Windows mandatory from 1 January 2024 for electronic exchange of information connected with ships’ arrival, stay and departure from port. [IMO — Maritime Single Window](https://www.imo.org/en/mediacentre/pressbriefings/pages/maritime-single-window-advancing-digitalization-in-shipping.aspx)

### European workforce policy context

On 29 April 2026, EU ministers responsible for maritime affairs signed the Lefkosia Declaration during an informal ministerial meeting held under the Cyprus Presidency of the Council of the EU. The declaration places people at the centre of maritime policy and calls for stronger seafarer education, training, reskilling and upskilling in response to the green and digital transitions. It also promotes maritime careers and the equal participation of women in the sector. [Cyprus Presidency — Lefkosia Declaration](https://cyprus-presidency.consilium.europa.eu/en/news/ministers-responsible-for-maritime-affairs-signed-the-lefkosia-declaration/)

The accompanying summary highlights digitalisation, automation, cybersecurity, data protection, fair working conditions, social dialogue and human-centred workforce development. These themes are relevant to this project because any AI-enabled crew-management tool must be introduced with appropriate skills, safeguards and human oversight.


>📌
The Lefkosia Declaration provides strategic European policy context for a human-centred digital transition. It does not directly evidence the frequency, cost or causes of failed crew changes, so it should support the project rationale rather than be used as proof of the business case.

For a medium-sized ship manager, however, relevant information may still be distributed across:

- crewing systems;
- travel-agent itineraries;
- email;
- vessel schedules;
- spreadsheets;
- port-agent messages;
- public airport, weather and transport sources.

That fragmentation creates an opportunity for decision support, but also creates data-quality, integration, privacy and accountability risks. These risks will be developed separately in `research/opportunities_risks.md`.

## 9. Round 1 problem framing

### Primary problem

The crewing team may not consistently identify which upcoming crew-change plans combine several warning signs and therefore require earlier intervention.

### Consequences to investigate

- increased rebooking and accommodation costs;
- additional crewing-officer workload;
- late or failed relief;
- fatigue and welfare consequences;
- operational uncertainty for the vessel;
- reduced confidence from owners or clients;
- in severe cases, knock-on disruption to vessel operations and the wider supply chain.

These consequences are plausible hypotheses. Round 1 does not claim measured savings or failure rates without client evidence.

### Proposed decision to support

> Which upcoming crew-change plans should a crewing officer review first, and which risk factors require human action?

### Human responsibility

The crewing officer remains responsible for checking facts and deciding what to do. The proposed system must not:

- decide whether a person is legally permitted to travel;
- replace immigration or medical advice;
- make employment decisions;
- purchase or cancel travel autonomously;
- guarantee that a journey will succeed;
- infer sensitive personal characteristics.

## 10. Data available for Round 1

### Public data

- airport identifiers and coordinates from [OurAirports](https://ourairports.com/data/);
- port identifiers and coordinates from [UN/LOCODE](https://unece.org/trade/uncefact/unlocode);
- daily all-cause pre-departure delay data by airport from [EUROCONTROL — All Pre-Departure Delay dataset](https://ansperformance.eu/reference/dataset/all-pre-departure-delay/), with the [source workbook](https://www.eurocontrol.int/performance/data/download/xls/All_Pre-Departure_Delay.xlsx);
- estimated seafarer supply by economy, rank and indicator for 2015 and 2021 from [UNCTADstat — Seafarer supply, quinquennial](https://unctadstat.unctad.org/datacentre/dataviewer/US.Seafarers), with [dataset metadata](https://unctadstat.unctad.org/datacentre/reportInfo/US.Seafarers);
- optional weather data from [Open-Meteo](https://open-meteo.com/en/docs).

### Tableau Public data plan

The EUROCONTROL and UNCTADstat datasets are workable for the Round 1 dashboard, but they answer different questions and should not be forced into one row-level join.

- **EUROCONTROL** can show recent operational context: average all-cause pre-departure delay per departure for selected European airports.
- **UNCTADstat `US.Seafarers`** can show workforce context: estimated seafarer supply by economy and by seafarer type—officers, ratings and total—for 2015 and 2021.

In Tableau Public, use them as separate data sources or separate worksheets within one dashboard. A country-level seafarer-supply figure does not explain the delay performance of a particular airport, and no causal relationship should be implied.


> 📊 Recommended dashboard story: **workforce context from UNCTADstat + travel-disruption context from EUROCONTROL**. The UNCTADstat table is quinquennial and contains only 2015 and 2021, so it is suitable for structural context—not current workforce monitoring or forecasting.


### Synthetic data

Because real crew-change records may contain personal, employment and commercially sensitive information, Round 1 uses fictional operational records for:

- crew and vessel identifiers;
- itineraries and reporting deadlines;
- document-readiness status;
- transfer and agent status;
- planned cost and simulated disruption outcomes.

The synthetic records demonstrate the analytical concept. They are not evidence of actual industry failure rates, savings or model accuracy.

## 11. Key findings for the Round 1 pitch

1. Maritime trade is globally important, and safe vessel operation depends on effective coordination between shipboard and shore-based personnel.
2. Crew changes are multi-party, international logistics processes—not simple staff swaps.
3. Crew-change reliability is connected to safety, fatigue, welfare, labour obligations and operational continuity.
4. Warning signs may be distributed across travel, documentation, vessel and port information.
5. A medium-sized ship manager is a credible target because it has meaningful operational complexity but may have limited capacity for a large bespoke platform.
6. Decision support should prioritise and explain cases; qualified people must retain responsibility.
7. Round 1 can evaluate the opportunity using public reference data, synthetic operational scenarios, a Tableau communication layer and one light workflow POC.

## 12. Assumptions requiring validation

- [ ]  Typical number of crew changes per vessel and month
- [ ]  Current rate of delayed, rebooked or failed crew changes
- [ ]  Average rebooking, hotel, agent and administrative costs
- [ ]  Main systems used by the crewing team
- [ ]  Frequency and cause of document-related problems
- [ ]  Most important escalation thresholds
- [ ]  Availability and quality of travel and vessel data
- [ ]  Acceptable use of LLM-generated briefings
- [ ]  Required access controls, retention periods and audit trail
- [ ]  Definition of a successful pilot

## 13. Source register

| Source | Use in this document | Accessed |
| --- | --- | --- |
| [UNCTAD — Review of Maritime Transport](https://unctad.org/topic/transport-and-trade-logistics/review-of-maritime-transport) | Importance of maritime transport | 2026-08-31 |
| [UNCTAD — Review of Maritime Transport 2025](https://unctad.org/publication/review-maritime-transport-2025) | Recent trade and ton-mile context | 2026-08-31 |
| [IMO — ISM Code](https://www.imo.org/en/ourwork/humanelement/pages/ismcode.aspx) | Safety-management context | 2026-08-31 |
| [IMO — Human Element](https://www.imo.org/en/ourwork/humanelement/pages/default.aspx) | Human-centred safety responsibility | 2026-08-31 |
| [ILO — Maritime Labour Convention, 2006](https://www.ilo.org/international-labour-standards/maritime-labour-convention-2006) | Work, rest, welfare and repatriation context | 2026-08-31 |
| [IMO — Crew changes and repatriation FAQ](https://www.imo.org/en/mediacentre/hottopics/pages/faq-on-crew-changes-and-repatriation-of-seafarers.aspx) | Fatigue and welfare context | 2026-08-31 |
| [IMO — Crew-change protocols](https://www.imo.org/en/mediacentre/pressbriefings/pages/15-crew-changes-.aspx) | Historical crew-change scale and stakeholder chain | 2026-08-31 |
| [ICS — Crew-change protocols](https://www.ics-shipping.org/current-issue/the-covid-19-pandemic-the-crew-change-crisis) | End-to-end process complexity | 2026-08-31 |
| [IMO — Maritime Single Window](https://www.imo.org/en/mediacentre/pressbriefings/pages/maritime-single-window-advancing-digitalization-in-shipping.aspx) | Sector digitalisation context | 2026-08-31 |
| [Cyprus Presidency — Lefkosia Declaration](https://cyprus-presidency.consilium.europa.eu/en/news/ministers-responsible-for-maritime-affairs-signed-the-lefkosia-declaration/) | European workforce, skills and human-centred digital-transition context | 2026-08-31 |
| [EUROCONTROL — All Pre-Departure Delay dataset](https://ansperformance.eu/reference/dataset/all-pre-departure-delay/) | Daily all-cause airport-delay context for Tableau | 2026-08-31 |
| [EUROCONTROL — Source workbook](https://www.eurocontrol.int/performance/data/download/xls/All_Pre-Departure_Delay.xlsx) | Raw airport-delay data for Tableau analysis | 2026-08-31 |
| [UNCTADstat — Seafarer supply, quinquennial](https://unctadstat.unctad.org/datacentre/dataviewer/US.Seafarers) | Estimated seafarer supply by economy, rank and indicator for 2015 and 2021 | 2026-08-31 |
| [UNCTADstat — `US.Seafarers` metadata](https://unctadstat.unctad.org/datacentre/reportInfo/US.Seafarers) | Definitions, estimation methodology and source limitations | 2026-08-31 |

[Summary of the Lefkosia Declaration — uploaded reference](c3856865-dbb6-4856-9d88-6065f0e9a01f.pdf)

Summary of the Lefkosia Declaration — uploaded reference

## Next research document

After reviewing this sector framing, create `research/opportunities_risks.md` to map business value, operational risks, data limitations and preliminary trust concerns.