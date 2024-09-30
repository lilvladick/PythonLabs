from .vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, fuel_consumption, fuel_type, passenger_capacity):
        super().__init__(fuel_consumption, fuel_type)
        self.passenger_capacity = passenger_capacity

    def calculate_fuel_consumption(self, load):
        return self.fuel_consumption * (1 + load / 100)

    def calculate_travel_cost(self, distance, fuel_price, fuel_consumption):
        fuel_consumed = fuel_consumption * distance / 100
        return fuel_consumed * fuel_price

    def __str__(self):
        return f"Автобус вмещает {self.passenger_capacity} пассажиров"