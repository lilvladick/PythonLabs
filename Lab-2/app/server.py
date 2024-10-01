from enum import Enum
from fastapi import FastAPI
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
    with sqlite3.connect('database/costs.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS travel_costs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicle_type TEXT NOT NULL,
                fuel_consumption REAL NOT NULL,
                weight REAL NOT NULL,
                distance REAL NOT NULL,
                fuel_type TEXT NOT NULL,
                travel_cost REAL NOT NULL);""")

            vehicle_type = type(obj).__name__
            cursor.execute(
                "INSERT INTO travel_costs (vehicle_type, fuel_consumption, weight, distance, fuel_type, travel_cost) VALUES (?, ?, ?, ?, ?, ?)",
                (vehicle_type, obj.calculate_fuel_consumption(load), load, distance, fuel_type, travel_cost))
            conn.commit()
        except Exception as e:
            print(e)
            # Обработка ошибок
            pass

    print("Данные успешно сохранены в SQLite базе данных")


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
