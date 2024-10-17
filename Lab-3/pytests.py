import pytest
from psycopg2 import Error
from postgre import database_connect, get_data, database_close_connection, save_data
from models import Advertisements

test_data = [
    Advertisements(title="Test", description="TEST", price=10.99, category="Электроника", seller_contacts="Саня Хмурый"),
    Advertisements(title="Test 2", description="TEST 2", price=5.99, category="Электроника", seller_contacts="Егор Нехмуренко")
]

test_queries = [
    "SELECT * FROM products",
    "SELECT title FROM products WHERE category = 'Электроника'",
]

@pytest.fixture
def db_connection():
    connection = database_connect()
    yield connection
    database_close_connection(connection)

@pytest.mark.parametrize("data", test_data)
def test_save_data(db_connection, data):
    if db_connection is None:
        pytest.skip("Database connection failed")
    result = save_data(db_connection, data)
    assert result is not None, "Save data failed"

@pytest.mark.parametrize("query", test_queries)
def test_get_data(db_connection, query):
    if db_connection is None:
        pytest.skip("Database connection failed")
    result = get_data(db_connection, query)
    assert result is not None, "Get data failed"

def test_database_connect():
    connection = database_connect()
    assert connection is not None, "Failed to connect to the database"
    database_close_connection(connection)

def test_database_close_connection():
    connection = database_connect()
    if connection is not None:
        database_close_connection(connection)
        with pytest.raises(Error):
            connection.cursor()

def test_save_data_error(db_connection):
    if db_connection is None:
        pytest.skip("Database connection failed")
    invalid_data = Advertisements(title="Invalid", description="TEST", price="invalid", category="Электроника", seller_contacts="Саня Хмурый")
    result = save_data(db_connection, invalid_data)
    assert result is None, "Expected save data to fail"

def test_get_data_error(db_connection):
    if db_connection is None:
        pytest.skip("Database connection failed")
    invalid_query = "SELECT * FROM fake_products"
    result = get_data(db_connection, invalid_query)
    assert result is None, "Expected get data to fail"