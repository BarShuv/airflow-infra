from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 14),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=3),
}

dag = DAG(
    "another_example_dag",  
    default_args=default_args,
    description="Another DAG with a different task",
    schedule_interval=timedelta(minutes=15), 
)

def print_another_message():
    print("This is a different DAG with a different task! ")

task2 = PythonOperator(
    task_id="print_another_message",
    python_callable=print_another_message,
    dag=dag,
)