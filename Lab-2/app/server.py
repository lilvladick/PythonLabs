from enum import Enum
from fastapi import FastAPI
from cars_package.vehicle import Vehicle
from cars_package import Car, Truck, Bus
import platform
import os
from docx import Document
import sqlite3
from pydantic import BaseModel

app = FastAPI()

fuel_prices = {
    "Petrol92": 48.70,
    "Petrol95": 50.60,
    "Petrol98": 52.70,
    "Petrol100": 56.50,
    "Diesel": 68.40,
    "Methane": 30.50,
}

def console_clear():
    op = platform.system()

    if op == 'Windows':
        os.system('cls')
    elif op in ['Linux', 'Darwin']:
        os.system('clear')
    else:
        print("Грязная консоль останется да-да")

def save_to_sqlite3(obj, load, distance, fuel_type, travel_cost):
    sqlite_conn = sqlite3.connect('costs.db')
    cursor = sqlite_conn.cursor()

    vehicle_type = type(obj).__name__
    cursor.execute("""
               INSERT INTO travel_costs (vehicle_type, fuel_consumption, weight, distance, fuel_type, travel_cost)
               VALUES (?, ?, ?, ?, ?, ?)
           """, (vehicle_type, obj.calculate_fuel_consumption(load), load, distance, fuel_type, travel_cost))

    sqlite_conn.commit()
    print("Данные успешно сохранены в SQLite базе данных")

    sqlite_conn.close()

class car_type(Enum):
    car = 1
    bus = 2
    truck = 3

class request(BaseModel):
        car_type: car_type

        fuel_consumption: float
        fuel_type: str
        capacity: float
        weight: float
        distance: float


@app.post("/vehicle/")
def calculate_car_cost(request: request):
    vehicle = None
    match request.car_type:
        case car_type.car:
            vehicle = Car(request.fuel_consumption, request.fuel_type, passengers=4)
        case car_type.bus:
            vehicle = Bus(request.fuel_consumption, request.fuel_type, passenger_capacity=4)
        case car_type.truck:
            vehicle = Truck(request.fuel_consumption, request.fuel_type, cargo_capacity=8000)
    fuel_consumption = vehicle.calculate_fuel_consumption(request.weight)
    travel_cost = vehicle.calculate_travel_cost(request.distance, fuel_prices[request.fuel_type], fuel_consumption)
    result = f"Стоимость поездки на автомобиле на {request.distance} км будет стоить {travel_cost:.2f} рублей"
    #save_to_sqlite3(vehicle, request.weight, request.distance, request.fuel_type, travel_cost)
    return {"message": result}

@app.get("/fuel-types/")
def get_fuel_types():
    return {"fuel_types": list(fuel_prices.keys())}

@app.post("/save-to-docx/")
def save_to_docx(result: str):
    doc = Document()
    doc.add_paragraph(result)
    doc.save("costs.docx")
    return {"message": "Файл сохранен"}