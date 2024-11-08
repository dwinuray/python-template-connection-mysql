# db_connection.py
import mysql.connector
from sqlalchemy import create_engine

# init
host = ""
user = ""
password = ""
database = ""

# MySQL Connector connection
def get_mysql_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# SQLAlchemy Engine connection
def get_sqlalchemy_engine():
    return create_engine(f'mysql://{user}:{password}@{host}/{database}')


