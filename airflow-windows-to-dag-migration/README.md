# 🌬️ Airflow DAG: Windows Scheduler Migration

This project demonstrates how to **migrate a Windows Task Scheduler job** into a **modular Apache Airflow DAG** using Python.

---

## 🧠 Scenario

A company previously ran a daily `.bat` or `.py` script using Windows Task Scheduler to copy files from a source folder to a backup directory.

---

## 🚀 What This DAG Does

✅ Simulates the legacy Windows job using Airflow  
✅ Backs up a file from `/tmp/data/input_file.csv` to `/tmp/backup/input_file_backup.csv`  
✅ Leverages Airflow’s built-in logging, retries, and scheduling  
✅ Fully deployable on any Airflow instance via `PythonOperator`

---

## 📂 Project Structure

```
data-engineering-portfolio/
├── airflow-docker/
│   └── docker-airflow/
│       ├── dags/
│       │   └── windows_backup_dag.py
│       ├── docker-compose-LocalExecutor.yml
│       └── …
├── airflow-windows-to-dag-migration/
│   ├── dags/
│   │   └── windows_backup_dag.py
│   ├── tmp/
│   │   ├── data/input_file.csv
│   │   └── backup/input_file_backup.csv
│   └── …

```
---

## ⚙️ How It Works

- Airflow runs in Docker using **LocalExecutor**
- A DAG named `windows_backup_migration_dag` runs **daily**
- It copies:
  - From → `/tmp/data/input_file.csv`
  - To → `/tmp/backup/input_file_backup.csv`

---

## 🐳 Setup Instructions

1. Clone the repo and navigate to the project folder:

   ```bash
   cd airflow-docker/docker-airflow

2. Update volume mount in docker-compose-LocalExecutor.yml:
   
  volumes:
  
	  - ./dags:/usr/local/airflow/dags
	  - ../../airflow-windows-to-dag-migration/tmp:/usr/local/airflow/shared/tmp   

3. Start, Stop and Restart Airflow:
   
        Start Airflow:
        docker-compose -f docker-compose-LocalExecutor.yml up -d

        Stop Airflow:
        docker-compose -f docker-compose-LocalExecutor.yml down

        Restart Airflow:
        docker-compose -f docker-compose-LocalExecutor.yml restart

5.	Access Airflow UI
   
	•	Visit: http://localhost:8080 or your GitHub Codespaces proxy URL
  
7.	Trigger the DAG:
   
	•	Go to windows_backup_migration_dag
	•	Turn it ON and trigger manually
	•	Confirm that input_file_backup.csv is created


 ## 🧩 DAG Logic (Simplified)
 
	 src = '/usr/local/airflow/shared/tmp/data/input_file.csv'
 
	 dst = '/usr/local/airflow/shared/tmp/backup/input_file_backup.csv'
 
	 shutil.copyfile(src, dst)
 


  ## ✅ Outcome
 
✨ Legacy Windows task is replaced with a modern, testable Airflow workflow

✨ Daily file backup is handled via a DAG

✨ Containerized setup ensures development and testing consistency


![Airflow DAG Screenshot](https://github.com/bashoori/repo/blob/master/airflow-windows-to-dag-migration/airflow.png?raw=true)


⸻

👩‍💻 Author

Created by Bita Ashoori
Data Engineer | Cloud Enthusiast | Automation Advocate
