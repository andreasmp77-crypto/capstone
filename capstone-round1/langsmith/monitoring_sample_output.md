# W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-01

# LangSmith Monitoring Sample

```$ python monitoring_sample.py```

Found 5 selected cases.

============================================================
Testing AI briefing for: CC-0005
Model: gpt-5-nano
============================================================
Input tokens: 382
Output tokens: 2135
Total tokens: 2517

AI RISK BRIEFING:
{
  "executive_assessment": "High operational risk for CC-0005 (score 55). Visa status is pending verification; ticket status is quoted but not confirmed; arrival buffer is below 4 hours (231 minutes). Route complexity is medium with a shortest connection of 154 minutes. Live weather is manageable but gusts up to 34.6 km/h could affect transfers. Immediate human review is recommended before proceeding.",
  "key_risk_drivers": [
    "Visa status pending verification (+25)",
    "Ticket status is quoted but not confirmed (+10)",
    "Arrival buffer below 4 hours (+20)"
  ],
  "recommended_actions": [
    "Verify visa status immediately with the issuing authority and obtain/validate all required documents",
    "Secure ticket confirmation or reissue with a confirmed itinerary; ensure seat allocations and payment status",
    "Do not authorize crew handover until visa verification and ticket confirmation are completed; consider delaying departure if necessary",
    "Increase arrival buffer where feasible: reschedule to arrive earlier or adjust connection to provide > 4 hours buffer",
    "Reassess connection viability (154 minutes) and explore alternative connections or ports if delays are anticipated",
    "Review live weather impact on ground transfers; arrange contingency transport if gusts affect transfers",
    "Ensure all documentation in the system is up-to-date and flagged for compliance"
  ],
  "ai_recommendation": "Escalate for human review. Do not proceed with handover while visa and ticket statuses are unresolved and arrival buffer is insufficient. Monitor weather and connection constraints and implement mitigation actions as above.",
  "recommendation_rationale": "The risk is driven by pending visa verification (+25), unconfirmed ticket (+10), and a critical arrival buffer (<4 hours, +20). These deterministic drivers underpin a High risk designation and warrant human oversight.",
  "assessment_limitation": "Assessment based solely on the provided operational data; no external verification or updates beyond what's supplied."
}

============================================================
Testing AI briefing for: CC-0007
Model: gpt-5-nano
============================================================
Input tokens: 318
Output tokens: 2976
Total tokens: 3294

AI RISK BRIEFING:
{
  "executive_assessment": "No quantified operational risk detected for CC-0007 based on current data. The route has High complexity but there is ample buffer (204 minutes) against a 45-minute shortest connection; visa Verified and ticketed; no weather constraints. Proceed with cautious monitoring and be prepared to activate contingency plans if delays arise.",
  "key_risk_drivers": [
    "High route complexity (multi-leg transfer)"
  ],
  "recommended_actions": [
    "Continue to monitor CC-0007 in real time for delays across legs; trigger escalation if the connection time is threatened.",
    "Maintain scheduled ground transportation coordination and contingency planning to utilize the 204-minute arrival buffer.",
    "Reconfirm all departure steps with the agent and port authorities to preserve schedule integrity.",
    "If any leg shows delay approaching the 45-minute connection, activate the contingency plan (alternative routing or standby crew)."
  ],
  "ai_recommendation": "Proceed with the crew change as planned; no immediate actions required, but ensure continuous monitoring of connection performance given high route complexity.",
  "recommendation_rationale": "Rationale: All required preconditions are satisfied (visa verified, ticketed) and there is substantial arrival buffer. The only notable factor is route complexity, which increases exposure to delays, so ongoing monitoring is warranted. No action is required unless risk indicators increase or a delay materializes.",
  "assessment_limitation": "Assessment based solely on the provided data. No live risk score, deterministic risk drivers, or weather constraints beyond what is stated. Missing information that could affect risk (e.g., port congestion, crew welfare concerns, ground transport reliability) is not accounted for."
}

============================================================
Testing AI briefing for: CC-0002
Model: gpt-5-nano
============================================================
Input tokens: 317
Output tokens: 2252
Total tokens: 2569

AI RISK BRIEFING:
{
  "executive_assessment": "Current data for CC-0002 indicates no immediate operational risk. Visa status is Verified and ticket is Reserved. Route complexity is Medium. Shortest connection time is 116 minutes with an arrival buffer of 184 minutes. No live weather conditions. No deterministic risk drivers identified. The plan appears feasible with adequate buffer to accommodate standard delays.",
  "key_risk_drivers": [],
  "recommended_actions": [
    "Proceed with CC-0002 as planned; maintain the current schedule.",
    "Continue monitoring connection times and arrival buffer; escalate if the buffer reduces significantly or the shortest connection time increases beyond current plan.",
    "Maintain visa and ticket status checks; ensure no changes to Verified/Reserved statuses.",
    "Coordinate with the ship's master and port agent to reaffirm ETA and gate clearance; confirm documentation readiness.",
    "Prepare a contingency window or alternate transfer option in case of unforeseen delays; keep stakeholders informed."
  ],
  "ai_recommendation": "Proceed with CC-0002 as planned; maintain continuous monitoring and readiness to adjust if conditions change.",
  "recommendation_rationale": "All provided indicators show no risk drivers and a buffer (184 minutes) that comfortably exceeds the required connection time (116 minutes). No weather constraints are present. Therefore, the prudent course is to proceed with standard monitoring and contingency readiness without additional risk mitigation steps.",
  "assessment_limitation": "Assessment is based solely on the provided snapshot. Any changes to weather, route, visa status, or ticket status after this point are not reflected and could affect risk."
}

============================================================
Testing AI briefing for: CC-0003
Model: gpt-5-nano
============================================================
Input tokens: 318
Output tokens: 2781
Total tokens: 3099

AI RISK BRIEFING:
{
  "executive_assessment": "No live operational risk detected for CC-0003. Although route complexity is High, a substantial arrival buffer (328 minutes) relative to a short connection (56 minutes) provides cushion. Documentation is in order (Ticketed, Visa Verified) and no weather constraints are present. Proceed with the crew change as planned, with ongoing monitoring and a contingency plan for potential transfer delays.",
  "key_risk_drivers": [
    "High route complexity",
    "Shortest connection time: 56 minutes",
    "Arrival buffer: 328 minutes (mitigating factor)",
    "Documentation status: Ticketed, Visa Verified",
    "Weather conditions: None"
  ],
  "recommended_actions": [
    "Proceed with CC-0003 as planned.",
    "Maintain real-time monitoring of connection times and port conditions; confirm that the 56-minute transfer remains achievable.",
    "Preserve the 328-minute arrival buffer and communicate any schedule changes to all stakeholders.",
    "Prepare a contingency transfer plan (including potential re-ticketing) if delays compromise the connection window.",
    "Confirm transfer arrangements with port authorities and ensure crew are ready for timely transfer at arrival."
  ],
  "ai_recommendation": "Proceed with the crew change as planned. No immediate risk; due to high route complexity, maintain active monitoring and keep a contingency transfer plan ready in case the 56-minute connection becomes unachievable.",
  "recommendation_rationale": "Deterministic risk drivers are none and risk level is None. The substantial arrival buffer mitigates potential delays in a high-complexity route, while ticketing and visa verification indicate readiness. No weather constraints present. Vigilance remains prudent given route complexity.",
  "assessment_limitation": "Assessment is based solely on the provided data; no risk score recalculation performed. Real-time changes (delays, port congestion, weather shifts) external to the provided information could alter risk and would require re-evaluation."
}

============================================================
Testing AI briefing for: CC-0001
Model: gpt-5-nano
============================================================
Input tokens: 318
Output tokens: 1901
Total tokens: 2219

AI RISK BRIEFING:
{
  "executive_assessment": "No operational risk detected for CC-0001 (risk score and level: None). With visa verified and ticketed, route complexity medium, shortest connection 102 minutes, and arrival buffer 694 minutes, there is ample time to manage the connection. No live weather impact observed.",
  "key_risk_drivers": [],
  "recommended_actions": [
    "Maintain current crew change plan as no risk factors identified.",
    "Continue to monitor for any change in risk factors or schedule disruptions; recheck connection time if delays occur.",
    "Verify that arrival buffer remains adequate against potential delays; adjust only if new information reduces buffer.",
    "Confirm ticket and visa status remain valid; escalate if any ticket or visa issue arises."
  ],
  "ai_recommendation": "No immediate risk mitigation required. Proceed with existing plan and maintain vigilant monitoring for changes in risk factors or schedule. Escalate to human review only if risk level becomes High or if critical deviations occur.",
  "recommendation_rationale": "Current data show no deterministic risk drivers and a generous arrival buffer relative to the connection time, with no weather or visa/ticket issues flagged. Actions focus on maintaining visibility and readiness rather than mitigation.",
  "assessment_limitation": "Assessment based solely on the provided data. Lacks external factors such as port congestion, crew availability fluctuations, or potential operational disruptions not reflected in the current dataset."
}

============================================================
LANGSMITH MONITORING EXPERIMENT COMPLETED
============================================================
Cases tested: 5
Model tested: gpt-5-nano

CASE SUMMARY:
- CC-0005 | gpt-5-nano | Input: 382 | Output: 2135 | Total: 2517
- CC-0007 | gpt-5-nano | Input: 318 | Output: 2976 | Total: 3294
- CC-0002 | gpt-5-nano | Input: 317 | Output: 2252 | Total: 2569
- CC-0003 | gpt-5-nano | Input: 318 | Output: 2781 | Total: 3099
- CC-0001 | gpt-5-nano | Input: 318 | Output: 1901 | Total: 2219

EXPERIMENT TOKEN SUMMARY:
Total input tokens: 1653
Total output tokens: 12045
Total tokens consumed: 13698

All AI briefing tests completed successfully.
