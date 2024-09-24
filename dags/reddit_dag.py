import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline
from etls.PostgresFileOperator import PostgresFileOperator
from utils.constants import file_postfix

default_args = {
    'owner': 'Martin Rubio',
    'start_date': datetime(2024, 9, 11)
}


with DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    
) as dag:

    extract = PythonOperator(
        task_id='reddit_extraction',
        python_callable=reddit_pipeline,
        op_kwargs={
            'file_name': f'reddit_{file_postfix}',
            'subreddit': 'dataengineering',
            'time_filter': 'day',
            'limit': 100
        },

    )

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres_default',
        sql=f'''
        CREATE TABLE IF NOT EXISTS reddit_{file_postfix} (
            id text DEFAULT 'unknown',
            title text DEFAULT 'no_title',
            score int DEFAULT 0,
            num_comments int DEFAULT 0,
            author text DEFAULT 'anonymous',
            created_utc text DEFAULT '1970-01-01T00:00:00Z',
            url text DEFAULT 'no_url',
            over_18 boolean DEFAULT FALSE,
            edited boolean DEFAULT FALSE,
            spoiler boolean DEFAULT FALSE,
            stickied boolean DEFAULT FALSE
        );
        ''',
        
    )

    insert_data = PostgresFileOperator(
        task_id = "insertar_data",
        operation="write",
        config={"table_name":f"reddit_{file_postfix}"},
        
    )

    extract >> create_table >> insert_data
