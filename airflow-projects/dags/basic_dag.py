from datetime import datetime
from random import randint

from airflow.decorators import dag, task

from helpers.sql_helpers import MySQLHelper

COLUMN_LIST = []
values = "?, "*len(COLUMN_LIST)
DB_TABLE = "DB.table"

SQL_QUERY = f"INSERT INTO {DB_TABLE}(field1, ...fieldX) VALUES ({values[:-1]})"


@dag(dag_id='example_dag', start_date=datetime(2022, 10, 29), catchup=False, tags=['example_dags'])
def main():

    @task(task_id='extract_task')
    def extract() -> dict:
        # For simplicity we will just return a random valued dictionary
        return {'first_column': randint(0, 11), 'second_column': randint(2000, 2500), 'third_column': randint(3000, 3500)}

    @task(task_id='transform_task')
    def transform(data: dict):
        return f"Random int: {extract['first_column']}"

    @task(task_id='load_task')
    def load(data: dict):
        # Send data to MySQL database so it can be accessed in MySQL workbench
        try:
            MySQLHelper.connect_to_mysql(data=data)
        except Exception as e:
            print(f"Exception occurred: {e}")
        return data

    # Define DAG flow
    load(transform(extract()))


main()
