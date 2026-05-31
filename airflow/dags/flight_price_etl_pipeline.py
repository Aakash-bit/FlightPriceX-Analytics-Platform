from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="flight_price_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["FlightPriceX"],
) as dag:

    load_csv = BashOperator(
        task_id="load_csv_to_elasticsearch",
        bash_command="""
        echo "Starting FlightPriceX ETL..."
        python /opt/airflow/scripts/load_csv_spark_to_elasticsearch.py"
        echo "ETL Completed Successfully"
        """
    )

    load_csv