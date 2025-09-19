# 🧩 DBT Models - Patient Engagement Pipeline

This folder contains the **SQL models** used to transform and organize raw event and feedback data into clean, analytics-ready tables.

The models simulate a standard dbt pipeline used in real-world healthcare and customer engagement analytics.

---

## 📂 Model Structure

| Folder | Purpose |
|:-------|:--------|
| `staging/` | Raw data cleaning and standardization (staging layer) |
| `marts/` | Final analytic tables for dashboards and KPIs (mart layer) |

---

## 🗂 Models Overview

### `staging/stg_event_logs.sql`
- Cleans raw event logs.
- Parses timestamps and standardizes event schema.
- Prepares base data for downstream transformations.

### `marts/user_sessions.sql`
- Aggregates user session data.
- Captures:
  - Session start time
  - Session end time
  - Total number of user interactions
- Materialized as an **incremental table** for performance optimization.

### `marts/nps_scores.sql`
- Analyzes Net Promoter Score (NPS) feedback.
- Categorizes users into:
  - Promoters (score 9-10)
  - Passives (score 7-8)
  - Detractors (score 0-6)
- Supports tracking of user satisfaction trends over time.

---

## 🔧 Materialization Strategy

| Model | Materialization Type |
|:------|:----------------------|
| `stg_event_logs` | View |
| `user_sessions` | Incremental Table |
| `nps_scores` | Table |

✅ Incremental materialization used where appropriate to optimize run times for large datasets.

---

## 📋 Notes

- Models are written in **standard SQL** and structured to work with **dbt 1.6.5**.
- Models use **ref()** to manage dependencies dynamically.
- Designed to be modular and extensible for additional customer engagement analytics features (e.g., churn prediction, feature usage trends).

---

## 📈 How These Models Fit the Pipeline

```plaintext
(raw tables: event_logs, nps_feedback)
            ↓
(staging models: stg_event_logs)
            ↓
(mart models: user_sessions, nps_scores)