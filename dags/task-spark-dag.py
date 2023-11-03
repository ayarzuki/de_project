from datetime import timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# spark_dag = DAG(
#     dag_id="spark_airflow_dag",
#     default_args=default_args,
#     schedule_interval=None,
#     dagrun_timeout=timedelta(minutes=60),
#     description="Test for spark submit",
#     start_date=days_ago(1),
# )

# Initialize the DAG
dag = DAG(
    'retail_analysis_dag',
    default_args=default_args,
    description='Analyze retail data using Spark',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 9, 21),
    catchup=False
)

# Extract = SparkSubmitOperator(
#     application="/spark-scripts/spark-example.py",
#     conn_id="spark_tgs",
#     task_id="spark_submit_task",
#     dag=spark_dag,
# )

# Spark Job task using SparkSubmitOperator
spark_job = SparkSubmitOperator(
    # task_id='spark_job',
    task_id='spark_submit_task',
    application="/spark-scripts/task-spark.py",  # path to your Spark script
    name="retail-analysis",
    conn_id="spark_tgs",  # connection ID for Spark
    # conn_id="postgres_tgs",  # connection ID for Spark
    # conf={"spark.some.config": "some-value"},  # any other Spark configurations
    dag=dag
)

# application="/spark-scripts/spark-example.py",
#     conn_id="spark_tgs",
#     task_id="spark_submit_task",
#     dag=spark_dag,

spark_job
