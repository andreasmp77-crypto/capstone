'''
W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-01
'''
import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI
from langsmith import traceable

# Load variables from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

# The five cases selected for the LangSmith experiment
SELECTED_CASES = [
    "CC-0005",
    "CC-0007",
    "CC-0002",
    "CC-0003",
    "CC-0001",
]

@traceable(
    name="Fetch Crew Change Cases from Airtable",
    run_type="tool"
)
def fetch_cases_from_airtable():
    """Fetch all required crew change records from Airtable."""

    url = (
        f"https://api.airtable.com/v0/"
        f"{AIRTABLE_BASE_ID}/"
        f"{AIRTABLE_TABLE_NAME}"
    )

    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}"
    }

    all_records = []
    params = {}

    while True:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        all_records.extend(data.get("records", []))

        # Airtable returns an offset when more pages exist
        if "offset" in data:
            params["offset"] = data["offset"]
        else:
            break

    # Keep only our five selected cases
    selected_records = []

    for record in all_records:
        fields = record.get("fields", {})

        if fields.get("crew_change_id") in SELECTED_CASES:
            selected_records.append({
                "record_id": record["id"],
                "crew_change_id": fields.get("crew_change_id"),
                "fields": fields
            })

    return selected_records


# AI Risk Briefing function

@traceable(
    name="Generate AI Risk Briefing",
    run_type="llm"
)
def generate_ai_briefing(case, model="gpt-5-nano"):
    """
    Generate an AI operational risk briefing.

    Uses the same prompt and assessment logic as the
    existing n8n Crew Travel Copilot workflow.
    """

    # Extract the Airtable fields dictionary from the selected case
    fields = case["fields"]

    # Build the prompt dynamically using the operational data
    # retrieved from Airtable
    prompt = f"""
You are an AI Operational Risk Analyst supporting maritime crew change operations.

Your role is to interpret the provided operational risk assessment and provide concise decision support for a human operations manager.

IMPORTANT RULES:

1. Do NOT recalculate or modify the deterministic risk score.
2. Do NOT contradict the provided risk level.
3. Base your assessment only on the operational data provided.
4. Do NOT invent missing information.
5. Clearly distinguish facts from recommendations.
6. Consider documentation, ticket status, connection constraints, arrival buffer and live weather conditions where relevant.
7. Provide practical and actionable recommendations.
8. If the risk level is High, recommend human review.
9. Keep the assessment concise and suitable for operational decision-making.

Analyse the following crew change:

CREW CHANGE ID:
{fields.get("crew_change_id")}

LIVE OPERATIONAL RISK SCORE:
{fields.get("live_operational_risk_score")}

LIVE OPERATIONAL RISK LEVEL:
{fields.get("live_operational_risk_level")}

DETERMINISTIC RISK DRIVERS:
{fields.get("live_risk_reasons")}

VISA STATUS:
{fields.get("visa_status")}

TICKET STATUS:
{fields.get("ticket_status")}

ROUTE COMPLEXITY:
{fields.get("route_complexity")}

SHORTEST CONNECTION:
{fields.get("shortest_connection_minutes")} minutes

ARRIVAL BUFFER:
{fields.get("arrival_buffer_minutes")} minutes

LIVE WEATHER CONDITIONS:
{fields.get("live_weather_summary")}

Provide the assessment using the required structured output format.

The JSON output must contain exactly these fields:

{{
  "executive_assessment": "string",
  "key_risk_drivers": ["string"],
  "recommended_actions": ["string"],
  "ai_recommendation": "string",
  "recommendation_rationale": "string",
  "assessment_limitation": "string"
}}
"""

    # Send the prompt to the selected OpenAI model
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        # Request a valid JSON object rather than free-form text
        response_format={"type": "json_object"},
    )

    # Convert the JSON text returned by the model into a Python dictionary
    return json.loads(response.choices[0].message.content)

# --------------------------------------------------
# TEST: Airtable retrieval + one OpenAI model call
# --------------------------------------------------

print("\nFetching selected crew-change cases from Airtable...\n")

# Retrieve the five selected cases from Airtable
cases = fetch_cases_from_airtable()

print(f"Found {len(cases)} selected cases.")

# Use only the first case for this initial connectivity test
test_case = cases[0]

print(f"\nTesting AI briefing for: {test_case['crew_change_id']}")
print("Model: gpt-5-nano\n")

# Generate the structured AI risk briefing
result = generate_ai_briefing(
    test_case,
    model="gpt-5-nano"
)

# Print the structured result in a readable JSON format
print(json.dumps(result, indent=2))

print("\nSingle-model AI test completed successfully.")