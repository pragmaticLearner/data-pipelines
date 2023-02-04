import os

from typing import Dict


class MySQLHelper:

    def __init__(self, sql_query: str, data: Dict) -> None:
        self.sql_query = sql_query
        self.data = data

    def connect_to_mysql(self, data: dict):
        try:
            print("Hello!!!")
        except Exception as e:
            print(f"Goodbye!!!")
