'''
W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-09-01
'''
# ============================================================
# Crew Travel Copilot AI - LangSmith Monitoring Sample
#
# This script:
# 1. Fetches selected crew-change cases from Airtable
# 2. Sends each case to an OpenAI model for AI risk assessment
# 3. Uses the same assessment prompt as the n8n workflow
# 4. Sends traces to LangSmith for observability
# 5. Captures latency and token usage for monitoring
# ============================================================

import os
import json
import requests

from dotenv import load_dotenv
from openai import OpenAI
from langsmith import traceable
from langsmith.wrappers import wrap_openai


# ============================================================
# CONFIGURATION
# ============================================================

# Load environment variables from the local .env file
load_dotenv()

# Airtable configuration
AIRTABLE_TOKEN = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

# OpenAI configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LangSmith configuration
# These are read automatically by the LangSmith SDK from .env
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")

# Model used for this monitoring experiment
MODEL = "gpt-5-nano"

# Selected cases for the LangSmith monitoring experiment
SELECTED_CASES = [
    "CC-0005",
    "CC-0007",
    "CC-0002",
    "CC-0003",
    "CC-0001",
]


# ============================================================
# CLIENT INITIALIZATION
# ============================================================

# Create the standard OpenAI client
#
# wrap_openai() automatically instruments OpenAI calls so
# LangSmith can capture:
# - LLM inputs and outputs
# - model name
# - latency
# - token usage
# - other available LLM metadata
client = wrap_openai(
    OpenAI(api_key=OPENAI_API_KEY)
)


# ============================================================
# AIRTABLE DATA RETRIEVAL
# ============================================================

@traceable(
    name="Fetch Crew Change Cases",
    run_type="chain"
)
def fetch_selected_cases():
    """
    Fetch the five selected crew-change cases directly from Airtable.
    """

    # Get Airtable configuration from environment variables
    airtable_api_key = os.getenv("AIRTABLE_API_KEY")
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("AIRTABLE_TABLE_NAME")

    # The five cases selected for the LangSmith monitoring experiment
    selected_case_ids = [
        "CC-0005",
        "CC-0007",
        "CC-0002",
        "CC-0003",
        "CC-0001",
    ]

    # Airtable API endpoint
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}"

    # Authentication headers
    headers = {
        "Authorization": f"Bearer {airtable_api_key}"
    }

    # Build an Airtable formula to retrieve only the selected cases
    formula = "OR(" + ",".join(
        [
            f"{{crew_change_id}}='{case_id}'"
            for case_id in selected_case_ids
        ]
    ) + ")"

    # Send the request to Airtable
    response = requests.get(
        url,
        headers=headers,
        params={
            "filterByFormula": formula
        },
        timeout=30
    )

    # Raise an error if the Airtable request fails
    response.raise_for_status()

    # Extract records from the Airtable response
    records = response.json().get("records", [])

    # Sort records according to our intended test order
    records.sort(
        key=lambda record: selected_case_ids.index(
            record["fields"].get("crew_change_id")
        )
    )

    return records

# ============================================================
# AI RISK BRIEFING GENERATION
# ============================================================

@traceable(
    name="Generate AI Risk Briefing",
    run_type="chain"
)
def generate_ai_briefing(case, model=MODEL):
    """
    Generate an AI operational risk briefing.

    Uses the same prompt and assessment logic as the
    existing n8n Crew Travel Copilot workflow.

    The function itself is traced as a LangSmith "chain".
    The wrapped OpenAI call inside it is automatically
    captured as a nested LLM trace.
    """

    # Extract operational fields from the Airtable record
    fields = case["fields"]

    # Build the prompt dynamically using Airtable data
    # This mirrors the prompt used in the n8n workflow
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

    # Send the prompt to OpenAI
    #
    # Because the client is wrapped with wrap_openai(),
    # LangSmith should automatically capture this as an
    # LLM child run including token usage.
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        # Force the response to be valid JSON
        response_format={
            "type": "json_object"
        },
    )

    # Convert the JSON response text into a Python dictionary
    briefing = json.loads(
        response.choices[0].message.content
    )

    # Extract token usage directly from the OpenAI API response
    token_usage = {
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
    }

    # Return both the AI assessment and token usage
    return {
        "briefing": briefing,
        "token_usage": token_usage,
    }


# ============================================================
# MAIN EXPERIMENT
# ============================================================

def main():
    """
    Run the complete LangSmith monitoring experiment.
    """

    # Retrieve selected crew-change cases from Airtable
    cases = fetch_selected_cases()

    print(f"\nFound {len(cases)} selected cases.\n")

    # Store all experiment results
    all_results = []

    # Process each crew-change case individually
    for case in cases:

        # Extract crew change ID for display and reporting
        crew_change_id = case["fields"].get(
            "crew_change_id",
            "Unknown"
        )

        print("=" * 60)
        print(f"Testing AI briefing for: {crew_change_id}")
        print(f"Model: {MODEL}")
        print("=" * 60)

        # Generate AI risk briefing
        result = generate_ai_briefing(
            case,
            model=MODEL
        )

        # Separate the briefing from token usage
        briefing = result["briefing"]
        token_usage = result["token_usage"]

        # Print token usage immediately for each case
        print(
            f"Input tokens: "
            f"{token_usage['input_tokens']}"
        )
        print(
            f"Output tokens: "
            f"{token_usage['output_tokens']}"
        )
        print(
            f"Total tokens: "
            f"{token_usage['total_tokens']}"
        )

        # Print the AI assessment
        print("\nAI RISK BRIEFING:")
        print(
            json.dumps(
                briefing,
                indent=2
            )
        )

        # Store the complete result for final summary
        all_results.append({
            "crew_change_id": crew_change_id,
            "model": MODEL,
            "briefing": briefing,
            "token_usage": token_usage,
        })

        print()

    # ========================================================
    # EXPERIMENT SUMMARY
    # ========================================================

    print("=" * 60)
    print("LANGSMITH MONITORING EXPERIMENT COMPLETED")
    print("=" * 60)

    print(f"Cases tested: {len(all_results)}")
    print(f"Model tested: {MODEL}")

    print("\nCASE SUMMARY:")

    # Initialise counters for aggregate token consumption
    total_input_tokens = 0
    total_output_tokens = 0
    total_tokens = 0

    # Display each case and accumulate token totals
    for item in all_results:

        usage = item["token_usage"]

        total_input_tokens += usage["input_tokens"]
        total_output_tokens += usage["output_tokens"]
        total_tokens += usage["total_tokens"]

        print(
            f"- {item['crew_change_id']} | "
            f"{item['model']} | "
            f"Input: {usage['input_tokens']} | "
            f"Output: {usage['output_tokens']} | "
            f"Total: {usage['total_tokens']}"
        )

    # Display total token consumption across all test cases
    print("\nEXPERIMENT TOKEN SUMMARY:")
    print(
        f"Total input tokens: "
        f"{total_input_tokens}"
    )
    print(
        f"Total output tokens: "
        f"{total_output_tokens}"
    )
    print(
        f"Total tokens consumed: "
        f"{total_tokens}"
    )

    print("\nAll AI briefing tests completed successfully.")


# ============================================================
# SCRIPT ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()