from  fastapi import FastAPI
from postgre import database_connection
from models import Advertisements, AdvertisementsRequest
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/get_data")
async def get_data():
    connection = database_connection.database_connect()
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price, category, seller_contacts FROM products")
    result = cursor.fetchall()
    cursor.close()
    database_connection.database_close_connection(connection)
    return [{"title": row[0],
             "description": row[1],
             "price": row[2],
             "category": row[3],
             "seller_contacts": row[4],} for row in result]

@app.post("/save_data")
async def save_data(data: AdvertisementsRequest):
    connection = database_connection.database_connect()
    advertisements = Advertisements()
    advertisements.title = data.title
    advertisements.description = data.description
    advertisements.price =data.price
    advertisements.category = data.category
    advertisements.seller_contacts = data.seller_contacts
    database_connection.save_data(connection, advertisements)
    database_connection.database_close_connection(connection)
    return data