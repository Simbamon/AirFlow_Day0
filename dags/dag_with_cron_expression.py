from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'simbamon',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

#Use crontab.guru for generating cron expression

with DAG(
    dag_id='dag_with_cron_expression_v04',
    default_args=default_args,
    description='This is our first dag that we wrote',
    start_date=datetime(2023, 3, 3),
    schedule_interval='0 3 * * Mon-Fri'
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression"
    )