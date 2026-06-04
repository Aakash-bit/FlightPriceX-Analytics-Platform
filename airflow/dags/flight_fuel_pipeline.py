from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "aakash",
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id="flight_fuel_pipeline",
    default_args=default_args,
    description="Flight Fuel Data Pipeline",
    start_date=datetime(2025, 6, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    fetch_fuel_data = BashOperator(
        task_id="fetch_fuel_data",
        bash_command="""
        cd /opt/airflow &&
        python /opt/airflow/scripts/fetch_fuel_data.py
        """
    )

    process_data = BashOperator(
        task_id="process_data",
        bash_command="""
        cd /opt/airflow &&
        python /opt/airflow/scripts/process_data.py
        """
    )

    load_to_elasticsearch = BashOperator(
        task_id="load_to_elasticsearch",
        bash_command="""
        cd /opt/airflow &&
        python /opt/airflow/scripts/load_to_elasticsearch.py
        """
    )

    fetch_fuel_data >> process_data >> load_to_elasticsearch