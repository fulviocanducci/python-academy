import mysql.connector
from mysql.connector.connection import MySQLConnection

def get_connection() -> MySQLConnection:
    return mysql.connector.connect(
        host="192.168.2.65",
        user="adm",
        password="adm123@",
        database="db"
    )