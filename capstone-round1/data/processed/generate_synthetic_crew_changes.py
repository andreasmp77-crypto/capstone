import random
from datetime import datetime, timedelta, timezone
from pathlib import Path
import pandas as pd

SEED = 42
random.seed(SEED)

OUTPUT = Path('/data/analysis/synthetic_crew_change_plans.csv')
SAMPLE_OUTPUT = Path('/data/analysis/synthetic_crew_change_plans_sample_10.csv')

ranks = [
    'Master', 'Chief Officer', 'Second Officer', 'Chief Engineer',
    'Second Engineer', 'Third Engineer', 'Electrician', 'Bosun',
    'Able Seafarer', 'Cook'
]
rank_weights = [5, 9, 11, 5, 9, 11, 8, 10, 22, 10]

origin_airports = ['MNL', 'DEL', 'BOM', 'CMB', 'DAC', 'CGK']
passport_by_origin = {
    'MNL': 'PH', 'DEL': 'IN', 'BOM': 'IN',
    'CMB': 'LK', 'DAC': 'BD', 'CGK': 'ID'
}
connection_airports = ['IST', 'DOH', 'DXB', 'FRA', 'CDG']

ports = {
    'DEHAM': {'airport': 'HAM', 'transfer': 45},
    'DEBRV': {'airport': 'BRE', 'transfer': 75},
    'NLRTM': {'airport': 'AMS', 'transfer': 75},
    'BEANR': {'airport': 'BRU', 'transfer': 50},
    'DKCPH': {'airport': 'CPH', 'transfer': 30},
    'NOOSL': {'airport': 'OSL', 'transfer': 50},
    'GRPIR': {'airport': 'ATH', 'transfer': 60},
    'CYLMS': {'airport': 'LCA', 'transfer': 50},
    'SGSIN': {'airport': 'SIN', 'transfer': 35},
    'AEDXB': {'airport': 'DXB', 'transfer': 45},
}

# Provisional scenario categories. Replace with EUROCONTROL-derived values later.
airport_delay_risk = {
    'HAM': 'Medium', 'BRE': 'Low', 'AMS': 'High', 'BRU': 'Medium',
    'CPH': 'Medium', 'OSL': 'Low', 'ATH': 'Medium', 'LCA': 'Low',
    'SIN': 'Low', 'DXB': 'Medium'
}

visa_values = ['Verified', 'Pending verification', 'Manual specialist check', 'Potential issue']
visa_weights = [75, 15, 7, 3]
weather_values = ['Low', 'Medium', 'High']
weather_weights = [70, 25, 5]
ticket_values = ['Not requested', 'Quoted', 'Reserved', 'Ticketed']
ticket_weights = [4, 8, 28, 60]
eta_confidence_values = ['High', 'Medium', 'Low']
eta_confidence_weights = [60, 30, 10]

start_date = datetime(2026, 3, 1, tzinfo=timezone.utc)
end_date = datetime(2026, 8, 30, tzinfo=timezone.utc)

def weighted(values, weights):
    return random.choices(values, weights=weights, k=1)[0]

def iso_utc(dt):
    return dt.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def risk_points(connection_count, connection_minutes, buffer_minutes, visa_status,
                delay_risk, weather_risk, agent_confirmed):
    score = 0
    reasons = []

    if connection_count == 1:
        if connection_minutes < 60:
            score += 25
            reasons.append(f'Tight connection: {connection_minutes} minutes')
        elif connection_minutes < 90:
            score += 15
            reasons.append(f'Short connection: {connection_minutes} minutes')

    if buffer_minutes < 240:
        score += 25
        reasons.append(f'Arrival buffer below 4 hours: {buffer_minutes} minutes')
    elif buffer_minutes <= 480:
        score += 15
        reasons.append(f'Arrival buffer between 4 and 8 hours: {buffer_minutes} minutes')

    visa_score = {
        'Verified': 0,
        'Pending verification': 20,
        'Manual specialist check': 25,
        'Potential issue': 35,
    }[visa_status]
    score += visa_score
    if visa_score:
        reasons.append(f'Visa/document status: {visa_status}')

    delay_score = {'Low': 0, 'Medium': 8, 'High': 15}[delay_risk]
    score += delay_score
    if delay_score:
        reasons.append(f'Airport historical delay indicator: {delay_risk}')

    weather_score = {'Low': 0, 'Medium': 5, 'High': 10}[weather_risk]
    score += weather_score
    if weather_score:
        reasons.append(f'Weather indicator: {weather_risk}')

    if not agent_confirmed:
        score += 10
        reasons.append('Port agent transfer not confirmed')

    score = min(score, 100)
    level = 'Low' if score <= 24 else 'Medium' if score <= 49 else 'High'
    if not reasons:
        reasons = ['No material risk factor identified under the prototype rules']
    return score, level, '; '.join(reasons)

def choose_outcome(level, active_reasons):
    probabilities = {
        'Low': [('On time', 90), ('Delayed but completed', 7), ('Rebooked', 2), ('Failed crew change', 1)],
        'Medium': [('On time', 70), ('Delayed but completed', 18), ('Rebooked', 7), ('Failed crew change', 5)],
        'High': [('On time', 40), ('Delayed but completed', 25), ('Rebooked', 15), ('Failed crew change', 20)],
    }
    outcomes, weights = zip(*probabilities[level])
    outcome = weighted(outcomes, weights)
    if outcome == 'On time':
        return outcome, 0, True, 0, 'No disruption'

    reason_candidates = []
    if 'connection' in active_reasons.lower():
        reason_candidates += ['Missed connection', 'Flight delay']
    if 'visa/document' in active_reasons.lower():
        reason_candidates += ['Document issue']
    if 'weather' in active_reasons.lower():
        reason_candidates += ['Severe weather', 'Flight delay']
    if 'port agent' in active_reasons.lower():
        reason_candidates += ['Port transfer issue']
    if 'airport historical delay' in active_reasons.lower():
        reason_candidates += ['Flight delay', 'Flight cancellation']
    if not reason_candidates:
        reason_candidates = ['Flight delay', 'Vessel ETA change']
    reason = random.choice(reason_candidates)

    if outcome == 'Delayed but completed':
        delay = random.randint(30, 360)
        extra_cost = random.choice([0, 75, 120, 180, 250, 350])
        completed = True
    elif outcome == 'Rebooked':
        delay = random.randint(180, 1080)
        extra_cost = random.randint(250, 1100)
        completed = True
    else:
        delay = random.randint(720, 2880)
        extra_cost = random.randint(900, 3500)
        completed = False
    return outcome, delay, completed, extra_cost, reason

def create_candidate(index):
    port_code = random.choice(list(ports))
    destination = ports[port_code]['airport']
    origin = random.choice(origin_airports)

    connection_count = weighted([0, 1], [25, 75])
    connection = ''
    connection_minutes = None
    if connection_count == 1:
        valid_hubs = [h for h in connection_airports if h not in {origin, destination}]
        connection = random.choice(valid_hubs)
        connection_minutes = random.randint(45, 180)

    random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
    departure = start_date + timedelta(seconds=random_seconds)
    departure = departure.replace(minute=random.choice([0, 15, 30, 45]), second=0, microsecond=0)

    duration_hours = random.randint(7, 13) if connection_count == 0 else random.randint(11, 22)
    arrival = departure + timedelta(hours=duration_hours, minutes=random.choice([0, 15, 30, 45]))

    buffer_minutes = random.randint(90, 900)
    transfer_minutes = ports[port_code]['transfer']
    reporting_deadline = arrival + timedelta(minutes=transfer_minutes + buffer_minutes)
    vessel_eta = reporting_deadline + timedelta(hours=random.randint(1, 8))

    plan_created = (departure - timedelta(days=random.randint(7, 45))).date().isoformat()
    visa_status = weighted(visa_values, visa_weights)
    documents_verified = visa_status == 'Verified'
    weather = weighted(weather_values, weather_weights)
    delay_risk = airport_delay_risk[destination]
    agent_confirmed = weighted([True, False], [85, 15])

    score, level, reasons = risk_points(
        connection_count, connection_minutes, buffer_minutes, visa_status,
        delay_risk, weather, agent_confirmed
    )

    route_complexity = 'Low' if connection_count == 0 else ('High' if connection_minutes < 90 else 'Medium')
    outcome, delay, completed, extra_cost, outcome_reason = choose_outcome(level, reasons)

    base_cost = random.randint(550, 1500)
    if connection_count == 1:
        base_cost += random.randint(100, 450)
    if destination in {'SIN', 'DXB'}:
        base_cost = max(450, base_cost - random.randint(100, 300))

    ticket_status = weighted(ticket_values, ticket_weights)
    if visa_status == 'Potential issue' and ticket_status == 'Ticketed':
        ticket_status = 'Reserved'

    return {
        'crew_change_id': f'CC-{index:04d}',
        'plan_created_date': plan_created,
        'vessel_code': f'VSL-{random.randint(1, 18):03d}',
        'seafarer_id': f'SEA-{random.randint(1, 95):04d}',
        'rank': weighted(ranks, rank_weights),
        'movement_type': 'Joining',
        'origin_airport': origin,
        'connection_airport': connection,
        'destination_airport': destination,
        'number_of_connections': connection_count,
        'shortest_connection_minutes': connection_minutes if connection_count else '',
        'scheduled_departure': iso_utc(departure),
        'scheduled_arrival': iso_utc(arrival),
        'estimated_travel_cost_eur': base_cost,
        'joining_port': port_code,
        'vessel_eta': iso_utc(vessel_eta),
        'reporting_deadline': iso_utc(reporting_deadline),
        'port_transfer_minutes': transfer_minutes,
        'port_agent_confirmed': agent_confirmed,
        'vessel_eta_confidence': weighted(eta_confidence_values, eta_confidence_weights),
        'passport_country_code': passport_by_origin[origin],
        'passport_valid': True,
        'visa_status': visa_status,
        'medical_valid': True,
        'documents_verified': documents_verified,
        'ticket_status': ticket_status,
        'airport_delay_risk': delay_risk,
        'weather_risk': weather,
        'route_complexity': route_complexity,
        'arrival_buffer_minutes': buffer_minutes,
        'risk_score': score,
        'risk_level': level,
        'risk_reasons': reasons,
        'ai_risk_briefing': '',
        'human_review_status': 'Not reviewed',
        'actual_outcome': outcome,
        'actual_delay_minutes': delay,
        'crew_change_completed': completed,
        'additional_cost_eur': extra_cost,
        'outcome_reason': outcome_reason,
    }

# Exact target mix: 90 Low, 38 Medium, 22 High.
targets = {'Low': 90, 'Medium': 38, 'High': 22}
accepted = []
counts = {key: 0 for key in targets}
attempts = 0
while len(accepted) < sum(targets.values()):
    attempts += 1
    candidate = create_candidate(len(accepted) + 1)
    level = candidate['risk_level']
    if counts[level] < targets[level]:
        accepted.append(candidate)
        counts[level] += 1
    if attempts > 100000:
        raise RuntimeError('Could not reach target risk distribution')

# Reassign stable IDs after rejection sampling.
for i, record in enumerate(accepted, start=1):
    record['crew_change_id'] = f'CC-{i:04d}'

df = pd.DataFrame(accepted)
df.to_csv(OUTPUT, index=False, encoding='utf-8')
df.head(10).to_csv(SAMPLE_OUTPUT, index=False, encoding='utf-8')

print(f'Seed: {SEED}')
print(f'Rows: {len(df)}')
print('Risk distribution:', df['risk_level'].value_counts().to_dict())
print('Outcome distribution:', df['actual_outcome'].value_counts().to_dict())
print(f'Output: {OUTPUT}')
print(f'Sample: {SAMPLE_OUTPUT}')
