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
        connection.autocommit = False

        return connection
    except (Exception, Error) as error:
        print("Connection ERROR", error)
        return None


def get_data(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except (Exception, Error) as error:
        print("Query ERROR", error)
        return None


def database_close_connection(connection):
    if connection is not None:
        connection.close()
        print("Connection Closed")

def save_data():
    pass