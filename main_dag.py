import datetime as dt

import airflow
from airflow.example_dags.tutorial import default_args
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=2),
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
}
dag = DAG(
    'collect_dag',
    default_args=default_args,
    description='DAG',
    schedule_interval=None,
    tags=['vkParser'],
)

BashOperator(
    task_id='main_task',
    bash_command='python3 vk_itis_parser.py; python3 words_handler.py; python3 write_to_db.py',
    dag=dag,
)