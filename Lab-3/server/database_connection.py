import psycopg2
from psycopg2 import Error
from advertisements import Advertisements


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


def make_query(connection, query):
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


def insert_data(data: Advertisements, connection):
    try:
        id = str(make_query(connection, "SELECT COUNT(*) FROM products;"))
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO products (id, title, description, price, category, images, seller_contacts) VALUES ({id}, "
            f"{data.title}, {data.description}, {data.price}, {data.category}, {data.images}, {data.seller_contacts});")
        rowcount = cursor.rowcount
        if rowcount == 1:
            print("Insert successfully.")
        else:
            print("Insert failed.")

        connection.commit()
        return cursor
    except (Exception, Error) as error:
        print("Query ERROR", error)
        return None
