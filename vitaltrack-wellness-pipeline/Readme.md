# 📱 VitalTrack Wellness Data Pipeline

**Project Type:** Portfolio Project  
**Industry:** HealthTech / Wellness Analytics  
**Technologies:** SQL (BigQuery), Python (Pandas), Airflow-style DAG

---

## 🧠 Project Overview

**VitalTrack** is a fictional wellness app that tracks heart rate, step count, and sleep patterns for thousands of users. You were brought on as a **freelance data engineer** to help the company transition from raw API logs to a clean, queryable analytics pipeline.

The goal is to create a robust and scalable data pipeline that:
- Ingests and cleans JSON logs from mobile devices
- Calculates user activity metrics (e.g., rolling averages)
- Loads data into BigQuery (or SQLite for demo)
- Powers analytics dashboards and data science models

---

## 🚀 What You'll Build

### ✅ 1. SQL: Heart Rate Trends

Use window functions to find:
- The **latest heart rate per user**
- A **7-day rolling average**

```sql
SELECT
  user_id,
  heart_rate,
  recorded_at,
  AVG(heart_rate) OVER (
    PARTITION BY user_id
    ORDER BY recorded_at
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS avg_hr_7d,
  CASE WHEN recorded_at = MAX(recorded_at) OVER (PARTITION BY user_id)
       THEN TRUE ELSE FALSE END AS is_latest
FROM heart_rate_logs
```

---

### ✅ 2. Python: Flatten Raw Mobile Data

Flatten nested JSON like this:

```json
{
  "user": {"id": 101, "name": "Bita"},
  "metrics": {"steps": 8721, "sleep": {"hours": 7.5, "quality": "good"}},
  "timestamp": "2024-10-02T08:00:00"
}
```

Into a flat record:

```python
{
  "user_id": 101,
  "user_name": "Bita",
  "steps": 8721,
  "sleep_hours": 7.5,
  "sleep_quality": "good",
  "timestamp": "2024-10-02T08:00:00"
}
```

---

### ✅ 3. DAG Logic: Airflow-Style Pipeline

Build a simple function-based DAG that runs daily:

```python
def extract_logs_from_api():
    ...

def transform_activity_data():
    ...

def load_to_bigquery():
    ...

# Simulated DAG
if __name__ == "__main__":
    extract_logs_from_api()
    transform_activity_data()
    load_to_bigquery()
```

---

## 📦 Folder Structure

```
vitaltrack-wellness-pipeline/
├── sql/
│   └── heart_rate_window.sql
├── python/
│   ├── flatten_json.py
│   └── dag_logic.py
├── README.md
```

## 👩‍💻 Author

**Bita Ashoori**  
Freelance & Enterprise Data Engineer  
📫 [LinkedIn](https://www.linkedin.com/in/bashoori) • 🌐 [GitHub Portfolio](https://github.com/bashoori)