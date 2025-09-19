import os
import sqlite3
from datetime import datetime, timedelta

import pandas as pd
import altair as alt
import streamlit as st

WAREHOUSE_DB = os.getenv("WAREHOUSE_DB", "./data/warehouse.db")
TABLE = "fact_daily_kpis"

st.set_page_config(page_title="Telemetry KPIs", page_icon="📊", layout="wide")
st.title("📊 Telemetry KPIs Dashboard")
st.caption("Bronze → Silver → Gold → Warehouse (simulated in SQLite)")

# sidebar filters
with st.sidebar:
    st.header("Filters")
    today = datetime.utcnow().date()
    start_date = st.date_input("Start date", today - timedelta(days=14))
    end_date = st.date_input("End date", today)
    if st.button("🔄 Refresh"):
        st.experimental_rerun()

def load_data(start, end):
    if not os.path.exists(WAREHOUSE_DB):
        return pd.DataFrame()
    conn = sqlite3.connect(WAREHOUSE_DB)
    q = f"""
    SELECT dt, dau, events, purchases, revenue
    FROM {TABLE}
    WHERE dt BETWEEN ? AND ?
    ORDER BY dt
    """
    df = pd.read_sql(q, conn, params=(start.isoformat(), end.isoformat()), parse_dates=["dt"])
    conn.close()
    return df

df = load_data(start_date, end_date)

if df.empty:
    st.warning("No data found. Run your ETL first!")
    st.stop()

# KPI cards
latest = df.iloc[-1]
c1, c2, c3, c4 = st.columns(4)
c1.metric("DAU (latest)", latest["dau"])
c2.metric("Events (latest)", latest["events"])
c3.metric("Purchases (latest)", latest["purchases"])
c4.metric("Revenue (latest)", f"${latest['revenue']:.2f}")

st.markdown("---")

# charts
left, right = st.columns(2)
with left:
    st.subheader("Revenue Trend")
    chart = alt.Chart(df).mark_line(point=True).encode(
        x="dt:T", y="revenue:Q", tooltip=["dt:T", "revenue:Q"]
    )
    st.altair_chart(chart, use_container_width=True)

with right:
    st.subheader("DAU vs Purchases")
    melted = df.melt(id_vars="dt", value_vars=["dau", "purchases"], var_name="metric", value_name="value")
    chart2 = alt.Chart(melted).mark_bar().encode(
        x="dt:T", y="value:Q", color="metric:N", tooltip=["dt:T", "metric:N", "value:Q"]
    )
    st.altair_chart(chart2, use_container_width=True)

st.markdown("---")
st.subheader("Raw Data")
st.dataframe(df, use_container_width=True)
