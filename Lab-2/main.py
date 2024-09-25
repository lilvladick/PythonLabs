import cars_package
from docx import Document

def main():
    #doc = Document() - это мы документик создаем

    car = cars_package.Car(8.5, "бензин", 4)
    truck = cars_package.Truck(25, "дизель", 10000)
    bus = cars_package.Bus(20, "соляра", 30)

    print(car)
    print(f"Стоимость поездки на автомобиле: {car.calculate_travel_cost(100, 50):.2f} рублей")

    print(bus)
    print(f"Стоимость поездки на автобусе: {bus.calculate_travel_cost(100, 50):.2f} рублей")

    print(truck)
    print(f"Стоимость поездки на грузовике: {truck.calculate_travel_cost(100, 50):.2f} рублей")

    #doc.save("costs.docx") - ну это будет сохранять короче

if __name__ == "__main__":
    main()
