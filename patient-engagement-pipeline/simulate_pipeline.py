"""
simulate_pipeline.py

This script simulates a simplified version of a DBT (Data Build Tool) pipeline
by performing data transformations locally using Python and Pandas.

Instead of using dbt models with SQL, we manually:
- Load raw event logs and NPS feedback data
- Perform staging, cleaning, and transformation steps
- Generate user session aggregates and NPS score categorizations
- Print output tables for use in dashboards and analysis

Author: Bita Ashoori
"""

# Import libraries
import pandas as pd
from datetime import datetime

# ==========================================================
# Step 1: Load Raw Mock Data (simulating 'source()' in DBT)
# ==========================================================

# Load app event logs (similar to raw_event_logs in a warehouse)
events = pd.read_json('data/mock_events.json')

# Load NPS feedback scores
nps = pd.read_csv('data/nps_feedback.csv')

print("🔹 Raw Events Data Sample:")
print(events.head())

print("\n🔹 Raw NPS Feedback Data Sample:")
print(nps.head())

# ==========================================================
# Step 2: Simulate DBT Staging Layer ('stg_event_logs.sql')
# ==========================================================

# Clean and convert timestamp fields
events['event_time'] = pd.to_datetime(events['timestamp'])

# Simulated "staging" step - output is similar to a stg_event_logs model

# ==========================================================
# Step 3: Simulate DBT Model - 'user_sessions.sql'
# ==========================================================

# Aggregate events by user to create session summaries
user_sessions = events.groupby('user_id').agg(
    session_start=('event_time', 'min'),
    session_end=('event_time', 'max'),
    total_events=('event_id', 'count')
).reset_index()

# This simulates the transformation logic inside 'user_sessions.sql'

print("\n✅ Simulated User Sessions Table:")
print(user_sessions)

# ==========================================================
# Step 4: Simulate DBT Model - 'nps_scores.sql'
# ==========================================================

# Create a helper function to categorize NPS feedback
def categorize_nps(score):
    if score >= 9:
        return 'Promoter'
    elif score >= 7:
        return 'Passive'
    else:
        return 'Detractor'

# Apply NPS categorization logic
nps['nps_category'] = nps['feedback_score'].apply(categorize_nps)

# Convert timestamps for feedback
nps['feedback_date'] = pd.to_datetime(nps['timestamp'])

# This simulates the transformation logic inside 'nps_scores.sql'

print("\n✅ Simulated NPS Scores Table:")
print(nps[['user_id', 'feedback_score', 'feedback_date', 'nps_category']])

# ==========================================================
# Step 5: Save transformed outputs to CSV
# ==========================================================

user_sessions.to_csv('data/user_sessions.csv', index=False)
nps[['user_id', 'feedback_score', 'feedback_date', 'nps_category']].to_csv('data/nps_scores.csv', index=False)

print("\n✅ Transformed data saved as CSV files for dashboard building!")

# ==========================================================
# Notes:
# - This script manually simulates key stages of a DBT pipeline.
# - In a production environment, DBT would manage SQL models, DAGs, testing, and documentation automatically.
# ==========================================================