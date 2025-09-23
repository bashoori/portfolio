# Player Session ETL (Airflow + Python + SQLite)

## What you’ll learn
- How to structure a small ETL repo
- How to write clean, testable ETL code (pure Python functions)
- How to schedule a daily job in Airflow using execution dates
- How to keep pipelines idempotent

## Prereqs
- GitHub Codespaces (or local dev with Python 3.10+)
- Basic terminal usage

## 1) Create virtual env & install deps
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
---------------------
1) Create & activate venv
python -m venv .venv
source .venv/bin/activate
python -V  # should show 3.12.x

2) Install dependencies (Py3.12 constraints)
pip install --upgrade pip
pip install "apache-airflow==2.9.3" \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.3/constraints-3.12.txt"
pip install pandas==2.2.2 pyarrow==17.0.0

3) Set environment & init Airflow
export REPO_ROOT="$(pwd)"
export AIRFLOW_HOME="$REPO_ROOT/airflow"
mkdir -p "$AIRFLOW_HOME/dags" "$AIRFLOW_HOME/logs"

airflow db init
airflow users create \
  --username admin --firstname Bita --lastname Ashoori \
  --role Admin --email bita@example.com --password admin

4) Quick manual ETL test (before Airflow)
python src/etl.py 2025-09-18
python src/etl.py 2025-09-19
python src/etl.py 2025-09-20

5) Verify results (utility script)
python src/query_results.py

6) Start Airflow (two terminals)
airflow webserver -p 8080
airflow scheduler

7) Run via Airflow

8) Verify again
python src/query_results.py
