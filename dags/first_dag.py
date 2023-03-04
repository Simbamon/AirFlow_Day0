from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'simbamon',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag_v5',
    default_args=default_args,
    description='This is our first dag that we wrote',
    start_date=datetime(2023, 3, 3, 11),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello, this is to test out the first task"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hello, this is to test out the second task"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="echo hello, Im task 3 and will be running after task 1 at the same time as task 2"
    )

    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method 3
    task1 >> [task2, task3]