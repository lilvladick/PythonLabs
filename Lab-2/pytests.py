import pytest
from cars_package import Car, Bus, Truck
from cars_package.vehicle import Vehicle

fuel_prices = {
    "Petrol92": 48.70,
    "Petrol95": 50.60,
    "Petrol98": 52.70,
    "Petrol100": 56.50,
    "Diesel": 68.40,
    "Methane": 30.50,
}

@pytest.fixture
def fuel_prices_fixture():
    return fuel_prices

@pytest.fixture
def car():
    return Car(fuel_consumption=5, fuel_type='Petrol98', passengers=4)

@pytest.fixture
def truck():
    return Truck(fuel_consumption=17, fuel_type='Petrol92', cargo_capacity=8000)

@pytest.fixture
def bus():
    return Bus(fuel_consumption=12, fuel_type='Diesel', passenger_capacity=60)

"""Тестирование расчета расхода топлива"""

@pytest.mark.parametrize('load, expected_consumption', [
    (50, 7.5),
    (100, 10.0),
    (150, 12.5)
], ids=['50 кг', '100 кг', '150 кг']) # Вес людей и груза сверх снаряженной массы автомобиля

def test_car_calculate_fuel_consumption(car, load, expected_consumption):
    actual_consumption = car.calculate_fuel_consumption(load)
    assert actual_consumption == expected_consumption

@pytest.mark.parametrize('load, expected_consumption', [
    (4000, 25.5),
    (8000, 34.0),
    (1000, 19.125)
], ids=['4000 кг', '8000 кг', '1000 кг'])

def test_truck_calculate_fuel_consumption(truck, load, expected_consumption):
    actual_consumption = truck.calculate_fuel_consumption(load)
    assert actual_consumption == expected_consumption

@pytest.mark.parametrize('load, expected_consumption', [
    (2100, 18.0),
    (1400, 16.0),
    (1750, 17.0)
], ids=['30 человек', '15 человек', '25 человек']) # Примерный вес людей в автобусе

def test_bus_calculate_fuel_consumption(bus, load, expected_consumption):
    actual_consumption = bus.calculate_fuel_consumption(load)
    assert actual_consumption == expected_consumption

"""Тестирование расчета стоимости поездки"""

@pytest.mark.parametrize('distance, fuel_price, fuel_consumption, expected_cost', [
    (500, fuel_prices["Petrol98"], 7.5, 1976.25),
    (200, fuel_prices["Petrol95"], 7.5, 759.0),
    (1000, fuel_prices["Petrol100"], 7.5, 4237.5)
], ids=['500 км', '200 км', '1000 км'])
def test_car_calculate_travel_cost(car, distance, fuel_price, fuel_consumption, expected_cost):
    actual_cost = car.calculate_travel_cost(distance, fuel_price, fuel_consumption)
    assert actual_cost == expected_cost

@pytest.mark.parametrize('distance, fuel_price, fuel_consumption, expected_cost', [
    (500, fuel_prices["Petrol95"], 7.5, 1897.5),
    (200, fuel_prices["Diesel"], 7.5, 1026.0),
    (1000, fuel_prices["Methane"], 7.5, 2287.5)
], ids=['500 км', '200 км', '1000 км'])
def test_truck_calculate_travel_cost(truck, distance, fuel_price, fuel_consumption, expected_cost):
    actual_cost = truck.calculate_travel_cost(distance, fuel_price, fuel_consumption)
    assert actual_cost == expected_cost

@pytest.mark.parametrize('distance, fuel_price, fuel_consumption, expected_cost', [
    (500, fuel_prices["Methane"], 18.0, 2745.0),
    (200, fuel_prices["Petrol92"], 18.0, 1753.2),
    (1000, fuel_prices["Diesel"], 16.3, 11149.2)
], ids=['500 км', '200 км', '1000 км'])
def test_bus_calculate_travel_cost(bus, distance, fuel_price, fuel_consumption, expected_cost):
    actual_cost = bus.calculate_travel_cost(distance, fuel_price, fuel_consumption)
    assert actual_cost == expected_cost

"""Тестирование на неверных данных"""

@pytest.mark.parametrize("distance, fuel_price, fuel_consumption", [
    (-1, 1, 10),
    (1000, -1, 10),
    (1000, 1, -10),
    (-1000, -1, -10),
])
def test_car_calculate_travel_cost_invalid_params(car, distance, fuel_price, fuel_consumption):
    with pytest.raises(ValueError):
        car.calculate_travel_cost(distance, fuel_price, fuel_consumption)\

@pytest.mark.parametrize("distance, fuel_price, fuel_consumption", [
    (-1, 1, 10),
    (1000, -1, 10),
    (1000, 1, -10),
    (-1000, -1, -10),
])
def test_bus_calculate_travel_cost_invalid_params(bus, distance, fuel_price, fuel_consumption):
    with pytest.raises(ValueError):
        bus.calculate_travel_cost(distance, fuel_price, fuel_consumption)

@pytest.mark.parametrize("distance, fuel_price, fuel_consumption", [
    (-1, 1, 10),
    (1000, -1, 10),
    (1000, 1, -10),
    (-1000, -1, -10),
])
def test_truck_calculate_travel_cost_invalid_params(truck, distance, fuel_price, fuel_consumption):
    with pytest.raises(ValueError):
        truck.calculate_travel_cost(distance, fuel_price, fuel_consumption)