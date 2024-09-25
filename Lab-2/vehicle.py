from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_consumption, fuel_type):
        self._fuel_consumption = fuel_consumption
        self._fuel_type = fuel_type

    """Расход топлива"""
    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if value < 0:
            raise ValueError("Расход топлива не может быть отрицательным")
        self._fuel_consumption = value

    """Тип топлива"""
    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        self._fuel_type = value

    """Подсчет расхода топлива в зависимости от загрузки"""
    @abstractmethod
    def calculate_fuel_consumption(self, load):
        pass

    """Подсчет стоимости поездки"""
    @abstractmethod
    def calculate_travel_cost(self, distance, fuel_price):
        pass