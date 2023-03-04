from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'simbamon',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


def greet(name, age):
    print("Hello Python!\n")
    print(f"my name is {name}, " f"and I am {age} years old")
with DAG(
    default_args=default_args,
    dag_id='dag_with_python_operator_v02',
    description='Our first dag using python operator',
    start_date=datetime(2023, 3, 3),
    schedule_interval='@daily',
) as dag:
    task1 = PythonOperator(
        task_id='greet_with_python',
        python_callable=greet,
        op_kwargs={'name': 'Jesse', 'age': 23}
    )

    task1