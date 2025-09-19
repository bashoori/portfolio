"""
📊 Streamlit Dashboard: FHIR Patient Overview (with Filters)

This version includes filters for gender, birth year, and condition keyword.

Author: Bita Ashoori
"""

import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# -------------------------------
# Load SQLite data
# -------------------------------
conn = sqlite3.connect("../data/output/fhir_data.db")

@st.cache_data
def load_data():
    patients = pd.read_sql("SELECT * FROM patients", conn)
    conditions = pd.read_sql("SELECT * FROM conditions", conn)
    return patients, conditions

patients, conditions = load_data()

# -------------------------------
# Streamlit Layout
# -------------------------------
st.title("🏥 FHIR Patient Data Dashboard (with Filters)")

st.markdown("Visualize synthetic healthcare data extracted from Synthea-generated FHIR bundles.")

# Summary stats
st.subheader("📋 Dataset Overview")
col1, col2 = st.columns(2)
col1.metric("Total Patients", len(patients))
col2.metric("Total Conditions", len(conditions))

# -------------------------------
# Filters
# -------------------------------
st.sidebar.header("🔎 Filter Options")

gender_filter = st.sidebar.multiselect(
    "Select Gender", options=patients["Gender"].dropna().unique(), default=patients["Gender"].dropna().unique()
)

birth_year_min, birth_year_max = st.sidebar.slider(
    "Select Birth Year Range",
    int(patients["Birth Date"].str[:4].dropna().min()),
    int(patients["Birth Date"].str[:4].dropna().max()),
    (1980, 2010)
)

condition_keyword = st.sidebar.text_input("Search Condition (Keyword)", "")

# -------------------------------
# Apply filters
# -------------------------------
patients['Birth Year'] = pd.to_datetime(patients['Birth Date'], errors='coerce').dt.year
filtered_patients = patients[
    (patients['Gender'].isin(gender_filter)) &
    (patients['Birth Year'] >= birth_year_min) &
    (patients['Birth Year'] <= birth_year_max)
]

if condition_keyword:
    filtered_conditions = conditions[conditions['Condition'].str.contains(condition_keyword, case=False, na=False)]
else:
    filtered_conditions = conditions

# -------------------------------
# Charts
# -------------------------------
st.subheader("🧍 Gender Distribution")
gender_chart = filtered_patients['Gender'].value_counts().reset_index()
gender_chart.columns = ['Gender', 'Count']
st.plotly_chart(px.pie(gender_chart, values='Count', names='Gender', title="Gender Breakdown"))

st.subheader("📆 Birth Year Distribution")
st.plotly_chart(px.histogram(filtered_patients.dropna(subset=['Birth Year']), x='Birth Year', nbins=30))

st.subheader("🩺 Top Conditions (Filtered)")
top_conditions = filtered_conditions['Condition'].value_counts().head(10).reset_index()
top_conditions.columns = ['Condition', 'Count']
st.plotly_chart(px.bar(top_conditions, x='Condition', y='Count', title="Top 10 Reported Conditions"))

st.markdown("---")
st.caption("Built by Bita Ashoori • Data Engineering Portfolio")
