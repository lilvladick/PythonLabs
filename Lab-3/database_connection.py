import psycopg2
from psycopg2 import Error

def database_connect():
    try:
        connection = psycopg2.connect(
            host='localhost',
            port=5430,
            database='Doska24',
            user='postgres',
            password='admin'
        )

        return connection
    except (Exception, Error) as error:
        print("Connection ERROR", error)
        return None

def make_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor
    except (Exception, Error) as error:
        print("Query ERROR", error)
        return None

def database_close_connection(connection):
    if connection is not None:
        connection.close()
        print("Connection Closed")