"""
Ongoing project to demonstrate knowledge of building airflow dags.

This example dag is to extract data from somewhere, transform is then send it to a MySQL database
"""

import os

from datetime import datetime
from random import randint

import mysql.connector

from airflow.decorators import dag, task

COLUMN_LIST = []
values = "?, "*len(COLUMN_LIST)
DB_TABLE = "DB.table"

SQL_QUERY = f"INSERT INTO {DB_TABLE}(field1, ...fieldX) VALUES ({values[:-1]})"


def connect_to_mysql(data: dict):
    try:
        connection = mysql.connector.connect(
            host=os.environ['LOCALHOST'],
            user=os.environ['USER'],
            passwd=os.environ['PASSWORD']
        )
        print(f"Connection successfully established : {connection}")

        mycursor = connection.cursor()
        mycursor.execute(SQL_QUERY, data)

        connection.commit()
    except Exception as e:
        print(f"Exception occurred while trying to connect to MySQL: {e}.")
    
    return connection


@dag(dag_id='example_dag', start_date=datetime(2022, 10, 29), catchup=False, tags=['example_dags'])
def main():

    @task(task_id='extract_data', python_callable='')
    def extract():
        # For simplicity we will just return a random valued dictionary
        return {'first_column': randint(0, 11), 'second_column': randint(2000, 2500), 'third_column': randint(3000, 3500)}

    @task(task_id='transform_data')
    def transform():
        pass

    @task(task_id='load_data')
    def load(data):
        # Send data to MySQL database so it can be accessed in MySQL workbench
        try:
            a = f""
        except Exception as e:
            print(f"Exception occurred: {e}")
        finally:
            connect_to_mysql(data=data)


main()
