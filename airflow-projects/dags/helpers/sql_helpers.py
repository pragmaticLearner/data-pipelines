import os
import mysqlclient as sql

from typing import Dict


class MySQLHelper:

    def __init__(self, sql_query: str, data: Dict) -> None:
        self.sql_query = sql_query
        self.data = data

    def connect_to_mysql(self, data: dict):
        try:
            connection = sql.connector.connect(
                host=os.environ['LOCALHOST'],
                user=os.environ['USER'],
                passwd=os.environ['PASSWORD']
            )
            print(f"Connection successfully established : {connection}")

            mycursor = connection.cursor()
            mycursor.execute(self.sql_query, data)

            connection.commit()
        except Exception as e:
            print(f"Exception occurred while trying to connect to MySQL: {e}.")

        return connection
