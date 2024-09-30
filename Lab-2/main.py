import cars_package
import platform
import os
from docx import Document


fuel_prices = {
    "Petrol92": 48.70,
    "Petrol95": 50.60,
    "Petrol98": 52.70,
    "Petrol100": 56.50,
    "Diesel": 68.40,
    "Methane": 30.50,
}


def main():
    #doc = Document() - это мы документик создаем
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
                car = cars_package.Car(9.5, "Petrol92", 4)
                get_info(car)
            case 2:
                truck = cars_package.Truck(9.5, "Petrol92", 4000)
                get_info(truck)
            case 3:
                bus = cars_package.Bus(9.5, "Petrol92", 50)
                get_info(bus)
            case 4:
                print(", ".join(fuel_prices))
            case _:
                print("Неверный выбор. Попробуйте еще раз.")


    #doc.save("costs.docx") - ну это будет сохранять короче

def get_info(object):
    console_clear()
    user_input = input("Введите вес пассажиров и груза, протяженность пути и тип топлива через пробел: ").split()

    try:
        weight = float(user_input[0])
        distance = float(user_input[1])
        fuel_type = user_input[2]
    except ValueError:
        print("Неправильный формат ввода. Вес и протяженность пути должны быть числами.")
        exit()

    fuel_consumption = object.calculate_fuel_consumption(weight)
    travel_cost = object.calculate_travel_cost(distance, fuel_prices[fuel_type], fuel_consumption)
    print(f"Стоимость поездки на автомобиле на {user_input[1]} км будет стоить {travel_cost:.2f} рублей")
    input("Для продолжения нажмите любую кнопку")


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
