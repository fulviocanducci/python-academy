import mysql.connector
from mysql.connector.connection import MySQLConnection

from constants import DB_HOST
from constants import DB_USER
from constants import DB_PASSWORD
from constants import DB_NAME


def get_connection() -> MySQLConnection:
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )