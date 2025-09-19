"""
📊 Streamlit Dashboard: FHIR Patient Overview

This app connects to the local SQLite database `fhir_data.db` and displays summary statistics
and interactive charts about the parsed FHIR patient data.


to run in bash :  
cd /workspaces/data-engineering-portfolio/healthcare-FHIR-data-pipeline/scripts streamlit run dashboard_app.py


Deploy the Streamlit App Publicly:  https://streamlit.io/cloud


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
st.title("🏥 FHIR Patient Data Dashboard")

st.markdown("Visualize synthetic healthcare data extracted from Synthea-generated FHIR bundles.")

# Summary stats
st.subheader("📋 Dataset Overview")
col1, col2 = st.columns(2)
col1.metric("Total Patients", len(patients))
col2.metric("Total Conditions", len(conditions))

# Gender distribution
st.subheader("🧍 Gender Distribution")
gender_chart = patients['Gender'].value_counts().reset_index()
gender_chart.columns = ['Gender', 'Count']
st.plotly_chart(px.pie(gender_chart, values='Count', names='Gender', title="Gender Breakdown"))

# Birth year histogram
st.subheader("📆 Birth Year Distribution")
patients['Birth Year'] = pd.to_datetime(patients['Birth Date'], errors='coerce').dt.year
st.plotly_chart(px.histogram(patients.dropna(subset=['Birth Year']), x='Birth Year', nbins=30))

# Conditions by type
st.subheader("🩺 Top 10 Conditions")
top_conditions = conditions['Condition'].value_counts().head(10).reset_index()
top_conditions.columns = ['Condition', 'Count']
st.plotly_chart(px.bar(top_conditions, x='Condition', y='Count', title="Top 10 Reported Conditions"))

st.markdown("---")
st.caption("Built by Bita Ashoori • Data Engineering Portfolio")
