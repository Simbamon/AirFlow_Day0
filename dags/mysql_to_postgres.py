import time
from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.decorators import task
from airflow.utils.task_group import TaskGroup
from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook
from airflow.hooks.base_hook import BaseHook
import pandas as pd
from sqlalchemy import create_engine
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'simbamon',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def get_src_tables():
    hook = MsSqlHook(mssql_conn_id="ms_sql_server")
    sql = """select  t.name as table_name  
     from sys.tables t where t.name in ('DimProduct','DimProductSubcategory','DimProductCategory') """
    df = hook.get_pandas_df(sql)
    print(f"this is df{df}")

with DAG(
    default_args=default_args,
    dag_id='testing_db_connection_v01',
    start_date=datetime(2023, 3, 9),
    schedule_interval='@daily',
) as dag:
    get_src_tables = PythonOperator(
        task_id='get_src',
        python_callable=get_src_tables
    )

    get_src_tables