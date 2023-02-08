from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from Twitter_airflow_project import run_etl

default_args = {
    'owner': 'hisyam',
    'depends_on_past': False,
    'start_date': datetime(2022, 8, 12),
    'email': ['hisyamimran1996@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='DAG for twitter ETL project',
    schedule_interval=timedelta(days=1),
)

dag_run_etl = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag, 
)

dag_run_etl

