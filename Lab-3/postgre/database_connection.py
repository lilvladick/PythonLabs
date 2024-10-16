import psycopg2
from psycopg2 import Error
from models import Advertisements


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
        cursor.close()
        return result
    except (Exception, Error) as error:
        print("Query ERROR", error)
        return None


def database_close_connection(connection):
    if connection is not None:
        connection.close()
        print("Connection Closed")

def save_data(connection, data: Advertisements):
    try:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO products (title, description, price, category, seller_contacts) VALUES ('{data.title}','{data.description}',{data.price},'{data.category}','{data.seller_contacts}')")
        connection.commit()
        cursor.close()

    except (Exception, Error) as error:
        print("Query ERROR", error)
        connection.rollback()
        return None