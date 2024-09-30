from .vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, fuel_consumption, fuel_type, passengers):
        super().__init__(fuel_consumption, fuel_type)
        self.passengers = passengers

    def calculate_fuel_consumption(self, weight):
        return self.fuel_consumption * (1 + weight / 100)

    def calculate_travel_cost(self, distance, fuel_price, fuel_consumption):
        fuel_consumed = fuel_consumption * distance / 100
        return fuel_consumed * fuel_price

    def __str__(self):
        return f"Машина с {self.passengers} пассажирами"