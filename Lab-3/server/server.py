from  fastapi import FastAPI
from postgre import database_connection
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

@app.post("/upload_data")
async def get_data():
    pass