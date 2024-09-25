from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, fuel_consumption, fuel_type, passengers):
        super().__init__(fuel_consumption, fuel_type)
        self.passengers = passengers

    def calculate_fuel_consumption(self, load):
        return self.fuel_consumption * (1 + load / 100)

    def calculate_travel_cost(self, distance, fuel_price):
        fuel_consumed = self.calculate_fuel_consumption(0) * distance / 100
        return fuel_consumed * fuel_price

    def __str__(self):
        return f"Машина с {self.passengers} пассажирами"