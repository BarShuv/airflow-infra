from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 14),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "example_dag",
    default_args=default_args,
    description="A simple DAG",
    schedule_interval=timedelta(minutes=10),  
)

def print_hello():
    print("Hello, Airflow! ")

task1 = PythonOperator(
    task_id="print_hello",
    python_callable=print_hello,
    dag=dag,
)

task1
