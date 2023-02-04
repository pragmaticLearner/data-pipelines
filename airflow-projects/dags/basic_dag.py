import aiohttp

from datetime import datetime
from random import randint

from airflow.decorators import dag, task
from fpl import FPL

from helpers.sql_helpers import MySQLHelper


async def _main_session():
    session = aiohttp.ClientSession()
    fpl = FPL(session)

    await session.close()


# Elements to be changed for the urls
element_id: int = 0
event_id: int = 0

urls = {'base_url': "https://fantasy.premierleague.com/api/",
        'general_information_path': "bootstrap-static/",
        'fixtures': 'fixtures/',
        'player_data': f"element-summary/{element_id}/",
        'gameweek_live_data': f'event/{event_id}/live/'}


@dag(dag_id='example_dag', start_date=datetime(2022, 10, 29), catchup=False, tags=['example_dags'])
def main():

    @task(task_id='extract_task')
    def extract() -> dict:
        return "hello extract"

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

    # Define the DAG's flow
    load(transform(extract()))


main()
