from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import logging
import os
import shutil

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'email_on_failure': False,
}

def backup_data():
   
    src = '/usr/local/airflow/shared/tmp/data/input_file.csv'
    dst = '/usr/local/airflow/shared/tmp/backup/input_file_backup.csv'

    logging.info("Starting backup job...")
    
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source file not found: {src}")

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    logging.info(f"Backup completed: {dst}")

with DAG(
    dag_id='windows_backup_migration_dag',
    description='Migrate Windows Scheduled Task to Airflow DAG',
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    run_backup_job = PythonOperator(
        task_id='run_backup_job',
        python_callable=backup_data
    )

    run_backup_job