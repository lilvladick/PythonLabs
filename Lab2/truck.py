from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, fuel_consumption, fuel_type, cargo_capacity):
        super().__init__(fuel_consumption, fuel_type)
        self.cargo_capacity = cargo_capacity


    def calculate_fuel_consumption(self, load):
        return self.fuel_consumption * (1 + load / self.cargo_capacity)


    def calculate_travel_cost(self, distance, fuel_price):
        fuel_consumed = self.calculate_fuel_consumption(0) * distance / 100
        return fuel_consumed * fuel_price