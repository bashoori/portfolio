
# 🏥 Patient Engagement Analytics Pipeline

This project simulates a **Customer Data Engineer** pipeline for a healthcare engagement platform.  
It ingests, transforms, and analyzes mock user events and feedback data, inspired by real-world setups like League's healthcare platform.


# 🩺 Patient Engagement Analytics Pipeline

**Simulated project based on a real-world Customer Data Engineer scenario at League**  
**Tech Stack**: GCP | BigQuery | DBT | Airflow | Looker | GitHub Actions | Python | SQL

---

## 📘 Project Overview

This project simulates the deployment of a cloud-native, customer-facing analytics pipeline for a digital healthcare client. The goal is to track user engagement on a wellness platform and deliver clean, scalable data models to support KPI dashboards for customer teams. This mirrors responsibilities from a Customer Data Engineer role at League.

---

## 🎯 Objectives

- Ingest app interaction logs and feedback data
- Build a data pipeline using GCP, DBT, and Airflow
- Transform and model raw data into meaningful analytics
- Deliver self-serve dashboards using Looker
- Simulate real-world CI/CD deployment with GitHub Actions
- Document the full process for client onboarding

---

## 🛠 Tech Stack

| Category       | Tool                                       |
|----------------|--------------------------------------------|
| Cloud Platform | Google Cloud (BigQuery, Pub/Sub, Cloud Functions) |
| Data Modeling  | DBT (Data Build Tool)                      |
| Orchestration  | Apache Airflow                             |
| CI/CD          | GitHub Actions                             |
| Dashboards     | Looker                                     |
| Languages      | SQL, Python                                |

---

## 🧱 Architecture

Mobile App Logs → GCP Pub/Sub → BigQuery (Raw Layer)
→ DBT (Transformations)
→ BigQuery (Analytics Layer)
→ Looker Dashboards
>>>>>>> 485bb667cf50404d5e3acb7de9c5e67569206eda

---

## 📂 Project Structure

<<<<<<< HEAD
| Folder | Purpose |
|:-------|:--------|
| `data/` | Contains mock input datasets (events and feedback) and final transformed CSVs |
| `dbt/` | Contains simulated dbt SQL models and project structure |
| `dashboards/` | Final dashboard images built from processed data |
| `simulate_pipeline.py` | Python script that simulates dbt transformations |

---

## 🔹 Technologies Used

- **Python 3.10+** (simulating dbt transformations with Pandas)
- **Pandas** (data wrangling)
- **Google Sheets ** (for dashboards)
- **SQL Logic Simulation** (no actual dbt cloud run, but full dbt structure)

---

## 🔧 Key Components

| Component | Details |
|:----------|:--------|
| Mock Events Data | JSON file simulating app events (login, feature use, feedback) |
| NPS Feedback Data | CSV file with Net Promoter Scores |
| Simulated Transformations | Python script applying SQL-like transformations |
| Output Data | `user_sessions.csv` and `nps_scores.csv` used for dashboards |
| Dashboard Mockups | Visual representations of engagement metrics |

---

## 📊 Dashboards

| Dashboard | Description | File |
|:----------|:-------------|:-----|
| **Daily Active Users (DAU)** | Line chart of user login activity | `dashboards/dau_chart.png` |
| **Feature Usage Breakdown** | Bar chart of feature interactions | `dashboards/feature_usage.png` |
| **NPS Score Distribution** | Pie chart of Promoters, Passives, Detractors | `dashboards/nps_distribution.png` |
| **Engagement Funnel** | Funnel showing user journey (Login → Feature Use → Feedback) | `dashboards/engagement_funnel.png` |

---

## 📚 Key Metrics 

This project tracks and analyzes the following key user engagement metrics:

| Concept | Description |
|:--------|:------------|
| **Net Promoter Score (NPS)** | A customer loyalty metric based on user feedback scores (0–10). Users are categorized as Promoters (9–10), Passives (7–8), or Detractors (0–6). Higher Promoter percentages indicate greater user satisfaction and growth potential. |
| **Engagement Funnel** | A visualization of user journey stages: from logging into the platform, using core features, to submitting feedback. It helps identify user drop-off points and optimize platform engagement. |
| **User Sessions** | Aggregated user activity records showing when users start and end their sessions and how many interactions they perform. Session data enables tracking of active usage patterns and product stickiness over time. |

✅ These metrics demonstrate real-world customer data analysis skills, essential for improving user retention, satisfaction, and overall platform success.

---

## 🧠 Simulated DBT Flow

While full dbt wasn't installed (due to Python 3.12 limitations), this project simulates:

- **Staging Layer** (`stg_event_logs`): Clean raw events
- **Mart Layer** (`user_sessions`, `nps_scores`): Build analytic tables
- **Incremental Logic**: Only process updated records (simulated)

✅ This demonstrates familiarity with **dbt model structure**, **incremental materialization**, and **data pipeline best practices**.

---

## ✍️ Author

**Bita Ashoori**  
🔗 [LinkedIn](https://www.linkedin.com/in/bitaashoori/)

---

## 📣 Notes

- Data is mock/generated for educational purposes only.
- No personally identifiable health information (PHI) used.
- Project created as part of professional portfolio to simulate Customer Data Engineer role tasks.

---

🔥 *Thank you for reviewing! Always happy to connect and discuss data engineering, dbt, cloud analytics, and customer engagement platforms.*
=======
/data
├── mock_events.json
├── nps_feedback.csv

/dbt
├── models/
├── macros/
├── dbt_project.yml

/airflow
├── dags/
└── utils/

/dashboards
└── dashboard_mockups/

.github/
└── workflows/
└── ci.yml

README.md

---

## 🧪 Mock Data

Sample mock data was created to simulate mobile app usage and user feedback for engagement tracking.

### `mock_events.json`
```json
[
  {
    "event_id": "evt_001",
    "user_id": "user_001",
    "event_type": "login",
    "feature_name": null,
    "timestamp": "2025-04-01T12:01:00Z"
  },
  {
    "event_id": "evt_002",
    "user_id": "user_001",
    "event_type": "feature_use",
    "feature_name": "meditation_audio",
    "timestamp": "2025-04-01T12:05:00Z"
  },
  {
    "event_id": "evt_003",
    "user_id": "user_002",
    "event_type": "feedback",
    "feature_name": null,
    "feedback_score": 8,
    "timestamp": "2025-04-01T13:30:00Z"
  }
]
>>>>>>> 485bb667cf50404d5e3acb7de9c5e67569206eda
This is my Replit version
