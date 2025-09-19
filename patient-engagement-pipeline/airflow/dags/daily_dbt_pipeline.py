from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'bita',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='daily_dbt_pipeline',
    default_args=default_args,
    description='Run DBT pipeline daily',
    schedule_interval='@daily',
    catchup=False
) as dag:

    run_dbt = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd /dbt/project && dbt run'
    )

    run_docs = BashOperator(
        task_id='generate_dbt_docs',
        bash_command='cd /dbt/project && dbt docs generate'
    )

    run_dbt >> run_docs