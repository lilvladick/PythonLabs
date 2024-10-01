from cars_package import Car, Bus, Truck
import platform
import os
from docx import Document
import sqlite3


fuel_prices = {
    "Petrol92": 48.70,
    "Petrol95": 50.60,
    "Petrol98": 52.70,
    "Petrol100": 56.50,
    "Diesel": 68.40,
    "Methane": 30.50,
}


def main():
    choices = {
        1: "Автомобиль",
        2: "Грузовик",
        3: "Автобус",
        4: "Виды топлива"
    }

    while True:
        for key, value in choices.items():
            print(f"{key}. {value}")
        choice = int(input("Ваш выбор: "))
        if choice not in choices:
            print("Неправильный выбор. Пожалуйста, выберите один из доступных вариантов.")
            continue

        match choice:
            case 1:
                user_input = input("Введите значение расхода топлива, тип топлива и вместимость через пробел: ").split()
                car = Car(float(user_input[0]), user_input[1], float(user_input[2]))
                get_info(car)
            case 2:
                user_input = input("Введите значение расхода топлива, тип топлива и вместимость через пробел: ").split()
                truck = Truck(float(user_input[0]), user_input[1], float(user_input[2]))
                get_info(truck)
            case 3:
                user_input = input("Введите значение расхода топлива, тип топлива и вместимость через пробел: ").split()
                bus = Bus(float(user_input[0]), user_input[1], float(user_input[2]))
                get_info(bus)
            case 4:
                print(", ".join(fuel_prices))
            case _:
                print("Неверный выбор. Попробуйте еще раз.")


def get_info(obj):
    console_clear()
    doc = Document()
    user_input = input("Введите вес пассажиров и груза, протяженность пути и тип топлива через пробел: ").split()

    try:
        weight = float(user_input[0])
        distance = float(user_input[1])
        fuel_type = user_input[2]
    except ValueError:
        print("Неправильный формат ввода. Вес и протяженность пути должны быть числами.")
        exit()

    fuel_consumption = obj.calculate_fuel_consumption(weight)
    travel_cost = obj.calculate_travel_cost(distance, fuel_prices[fuel_type], fuel_consumption)
    result = f"Стоимость поездки на автомобиле на {user_input[1]} км будет стоить {travel_cost:.2f} рублей"
    print(result)
    choice = input("Сохранить результат в docx? (Да/Нет) [Нет]: ")
    if choice == 'Да':
        doc.add_paragraph(result)
        doc.save("costs.docx")
        print("Файл сохранен")
    save_to_sqlite3(obj, weight, distance, fuel_type, travel_cost)
    input("Для продолжения нажмите любую кнопку")
    console_clear()


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

def console_clear():
    op = platform.system()

    if op == 'Windows':
        os.system('cls')
    elif op in ['Linux', 'Darwin']:
        os.system('clear')
    else:
        print("Грязная консоль останется да-да")

if __name__ == "__main__":
    main()
