# Data Research

### **1. Recommended data strategy**

I recommend using **three layers**:

| **Layer** | **Purpose** | **Recommended source** |
| --- | --- | --- |
| Core operational data | Represents planned crew changes | Synthetic CSV created by us |
| Historical risk evidence | Grounds airport-delay indicators | EUROCONTROL |
| Reference/enrichment data | Adds airports, ports, and weather | OurAirports, UN/LOCODE, Open-Meteo |

## **3. Recommended public data sources**

### **A. EUROCONTROL airport-delay data — recommended**

EUROCONTROL publishes European aviation performance data, including airport-level pre-departure delays.

[EUROCONTROL performance data downloads](https://ansperformance.eu/data/)

[EUROCONTROL aviation data](https://www.eurocontrol.int/our-data)

[EUROCONTROL Aviation Data Repository for Research](https://www.eurocontrol.int/dashboard/aviation-data-research)

The performance downloads include measures such as:

- daily total pre-departure delay by airport;
- air-traffic-control-related delay;
- airport performance;
- traffic and network indicators.

#### **How we would use it**

We would calculate airport-level indicators such as:

- average delay minutes;
- percentage of high-delay days;
- monthly delay trend;
- airport disruption category;
- seasonal risk.
- We could then attach an airport risk indicator to each synthetic crew journey.

#### **Caveat**

EUROCONTROL data may provide airport-level or aviation-network performance rather than a complete passenger itinerary history. It is useful for a **risk indicator**, but it should not be presented as proof that one specific future flight will be delayed.

That distinction demonstrates honest transparency.

### **B. OurAirports — strongly recommended**

[OurAirports](https://ourairports.com/data/) provides regularly updated downloadable CSV files covering airports, countries, and regions.

Useful links:

[OurAirports data downloads](https://ourairports.com/data/)

[Airport data dictionary](https://ourairports.com/help/data-dictionary.html)

[Direct airports CSV](https://ourairports.com/data/airports.csv)

[GitHub data repository](https://github.com/davidmegginson/ourairports-data)

Useful fields include:

- airport name;
- IATA and ICAO codes;
- country and region;
- latitude and longitude;
- airport type.

#### **How we would use it**

It can turn codes such as FRA, IST, and MNL into readable dashboard information and enable maps.

Example:

MNL → Ninoy Aquino International Airport → Philippines
IST → Istanbul Airport → Türkiye
HAM → Hamburg Airport → Germany

#### **Caveat**

This is community-maintained open reference data. It is appropriate for a student dashboard, but a production system would use an operationally governed airport-data provider.

### **C. UN/LOCODE port and location data — strongly recommended**

UN/LOCODE is the United Nations location-code system used for ports and other trade and transport locations.

[Official UN/LOCODE page](https://unece.org/trade/uncefact/unlocode)

[Official downloads](https://unece.org/trade/cefact/UNLOCODE-Download)

[Code list by country](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)

It can provide:

- port or location code;
- country;
- location name;
- function indicators;
- coordinates where available.

#### **How we would use it**

The synthetic crew-change record can contain:

joining_port_unlocode = DEHAM

Power BI can then display:

DEHAM → Hamburg, Germany

This creates a standard link between crew-change plans and port locations.

#### **Caveat**

UN/LOCODE is reference data, not a live vessel-arrival service. It tells us **where the port is**, not whether the vessel will arrive on time.

### **D. US Bureau of Transportation Statistics — useful alternative**

The US Bureau of Transportation Statistics provides detailed public airline on-time performance and causes-of-delay data.

[Airline On-Time Statistics](https://www.transtats.bts.gov/ontime/)

[On-Time Performance database information](https://transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD)

[BTS airline performance data](https://www.bts.gov/browse-statistical-products-and-data/bts-publications/airline-service-quality-performance-234-time)

It includes fields such as:

- origin and destination airports;
- scheduled and actual times;
- cancellations;
- arrival delays;
- delay causes.

#### **Advantages**

It is detailed, structured, public, and suitable for Power BI.

#### **Limitation**

It primarily covers US domestic aviation. Many realistic crew-change routes would involve Europe, Africa, and Asia.

#### **My recommendation**

Use BTS only if EUROCONTROL proves difficult to clean or too aggregated. We should not combine huge datasets merely to appear sophisticated.

## **4. APIs we could use**

### **A. Open-Meteo — best API for the Round 1 POC**

[Open-Meteo](https://open-meteo.com/)

[Forecast API documentation](https://open-meteo.com/en/docs)

[Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api)

It offers:

- forecast and historical weather;
- global coverage;
- JSON responses;
- no API key for the open, non-commercial service.
- Possible weather fields include:
- precipitation;
- wind speed and gusts;
- visibility-related conditions;
- thunderstorms or severe-weather indicators.

#### **Example use**

- When a crew-change record is submitted, n8n could:
- look up the destination airport coordinates;
- request the weather forecast;
- check whether weather conditions exceed predefined thresholds;
- add a weather warning to the risk briefing.

Conceptual request:

https://api.open-meteo.com/v1/forecast
    ?latitude=...
    &longitude=...
    &hourly=precipitation,wind_speed_10m,wind_gusts_10m

We should build the actual request from the current documentation when we reach the n8n step.

#### **Why this is my first-choice API**

It is accessible, explainable, and easy to connect using n8n’s [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest).

It demonstrates an authentic API integration without making the whole POC dependent on an expensive commercial provider.

### **B. Aviationstack — possible optional flight API**

[Aviationstack website](https://aviationstack.com/)

[API documentation](https://aviationstack.com/documentation)

[Pricing and feature availability](https://aviationstack.com/pricing)

It advertises access to:

- real-time flight status;
- schedules;
- airports and airlines;
- delays;
- historical flight information.

#### **Possible Round 1 use**

Given a flight number and date, n8n could attempt to retrieve its status or delay information and add that to the alert.

#### **Caveats**

- Requires an API key.
- Endpoint availability can depend on the subscription tier.
- Historical, future-schedule, or HTTPS access may have plan restrictions.
- We should confirm the current free-tier capabilities before designing around it.
- It must be treated as a demo integration, not a production source of guaranteed travel information.

**Recommendation:** optional enhancement—not a core dependency.

### **C. OpenSky Network — interesting but not recommended for this POC**

[OpenSky API](https://opensky-network.org/data/api)

[Official API documentation](https://openskynetwork.github.io/opensky-api/)

[Available datasets](https://opensky-network.org/data)

OpenSky provides live and historical aircraft-position information for research and non-commercial purposes.

However, its documentation explicitly warns that it does **not** provide conventional commercial data such as airport schedules and passenger flight delays.

It is good for:

- aircraft movements;
- trajectories;
- live airspace information;
- aviation research.
- It is not ideal for:
- missed-connection assessment;
- passenger itinerary planning;
- fare comparisons;
- reliable commercial flight-status workflows.

**Recommendation:** do not use it merely because it is free. It solves a different problem.

### **D. AISStream — possible vessel-position API, but not for Round 1**

[AISStream](https://aisstream.io/)

[AISStream documentation](https://aisstream.io/documentation)

[GitHub repository](https://github.com/aisstream/aisstream)

It provides a free real-time AIS stream over WebSockets and can return vessel-position messages.

#### **Possible use**

It could eventually help demonstrate that a vessel’s position or ETA has changed.

#### **Why I would avoid it initially**

- It uses a continuous **WebSocket stream**, not a simple one-time REST request.
- That adds unnecessary n8n and data-processing complexity.
- AIS destination and ETA fields are entered onboard and may be missing, stale, or inaccurate.
- A position alone does not reliably prove the vessel’s crew-change readiness.
- For Round 1, use a synthetic vessel_eta and clearly state that production deployment would integrate with the ship manager’s fleet system or a commercial AIS provider.

### **E. MarineTraffic — production-style option, probably not needed now**

[MarineTraffic API documentation](https://servicedocs.marinetraffic.com/)

[Ports information endpoints](https://servicedocs.marinetraffic.com/tag/Ports-Information/)

[MarineTraffic API service description](https://support.marinetraffic.com/en/articles/9552659-api-services)

Available capabilities include:

- vessel positions;
- port calls;
- vessel ETA;
- expected and predictive port arrivals;
- port congestion;
- voyage forecasts.

#### **Caveat**

This is a commercial service with contract-specific access and call limits. It is useful in a production architecture discussion and cost estimate, but we should not make the student POC depend on it unless you already have access.

### **F. Visa and document-requirement APIs — production only**

#### **IATA Timatic**

[IATA Timatic](https://www.iata.org/en/services/compliance/timatic/)

[IATA Timatic product information](https://www.iata.org/en/publications/timatic/)

Timatic is used by airlines and travel professionals for passport, visa, and health-document requirements.

#### **Sherpa**

[Sherpa developer documentation](https://docs.joinsherpa.io/)

[Visa Requirements API quickstart](https://docs.joinsherpa.io/requirements-api/quickstart-visa.html)

Sherpa provides entry, passport, visa, and travel-document requirements through an API.

#### **Caveats**

These are commercial or business-access services.

Visa eligibility depends on more than nationality and destination. Transit points, residence status, document type, purpose, length of stay, and seafarer-specific arrangements can matter.

A prototype must not claim that an LLM has made an authoritative visa determination.

For Round 1, use synthetic categories:

Plain Text

verified
pending review
potential transit visa issue
manual specialist check required

The output should say:

> “Visa/document status requires verification through an authorised source.”
> 

That is safer and more credible than pretending our prototype can provide legal immigration clearance.

### Crew Statistics

## Open Tabular and API Datasets

- **UNCTADstat (UN Trade and Development):** Provides structured time-series tables on seafarer supply by nationality, rank (officers vs. ratings), and flag registration.unctadstat.unctad+1
    - **Dataset:** *Seafarer supply, quinquennial (Table `US.Seafarers`)*.unctadstat.unctad+1
    - **Access:** Download directly as CSV/Excel or query programmatically via the [UNCTADstat Data Centre](https://unctadstat.unctad.org/datacentre/reportInfo/US.Seafarers).unctadstat.unctad+1
- **EMSA STCW-IS Portal:** Contains EU and non-EU officer and master certificate/endorsement records categorized by issuing nation and citizenship.emsa.europa+1
    - **Access:** Download aggregated tabular views from the [EMSA STCW-IS Statistics Module](https://portal.emsa.europa.eu/web/stcw/seafarers-stats) or retrieve public reports via the [EU Open Data Portal (data.europa.eu)](https://data.europa.eu/).emsa.europa+2
- **ILOSTAT (International Labour Organization):** Tracks employment in water transport, labour demographics, and safety metrics.
    - **Access:** Structured bulk downloads (CSV) and a REST API via the [ILOSTAT Bulk Data Portal](https://ilostat.ilo.org/data/bulk/).

---

## Machine-Readable National Registers

| Country / Source | Data Type | Access Format |
| --- | --- | --- |
| **Philippines (DMW / OpenStat)** | Annual deployment counts of marine officers and ratings | CSV / Excel via [PSA OpenStat](https://openstat.psa.gov.ph/) |
| **India (DGS / e-Governance)** | Registered seafarers with valid INDoS and CDCs | Tabular monthly returns via [DGS India](https://www.dgshipping.gov.in/) |
| **UK Maritime & Coastguard Agency (MCA)** | Seafarer certificates and manning statistics | Open government tables via [GOV.UK Statistics](https://www.gov.uk/government/organisations/maritime-and-coastguard-agency) |

---

## Global Aggregates (BIMCO / ICS)

The most comprehensive macro dataset remains the quinquennial **BIMCO/ICS Seafarer Workforce Report** (covering ~1.9 million seafarers across the top supplier nations: Philippines, Russian Federation, Indonesia, China, India, Ukraine, etc.).[unctad](https://unctad.org/system/files/official-document/rmt2021_en_0.pdf)

While the full report is commercial, the underlying country totals and rank splits are regularly aggregated and released in open formats through UNCTAD’s *Review of Maritime Transport* and UNCTADstat.