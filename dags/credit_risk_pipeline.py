from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from ingestion.kaggle_download import download_dataset
from ingestion.bronze_loader import upload_to_s3
from ingestion.silver_transform import clean_data
from ingestion.gold_transform import create_features

default_args = {
    "owner": "AO",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

dag = DAG(
    "credit_risk_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
)

task_1 = PythonOperator(
    task_id="kaggle_download",
    python_callable=download_dataset,
    dag=dag
)

task_2 = PythonOperator(
    task_id="bronze_to_s3",
    python_callable=upload_to_s3,
    dag=dag
)

task_3 = PythonOperator(
    task_id="silver_transform",
    python_callable=clean_data,
    dag=dag
)

task_4 = PythonOperator(
    task_id="gold_features",
    python_callable=create_features,
    dag=dag
)

task_1 >> task_2 >> task_3 >> task_4