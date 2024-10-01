from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, fuel_consumption, fuel_type, cargo_capacity):
        super().__init__(fuel_consumption, fuel_type)
        self.cargo_capacity = cargo_capacity


    def calculate_fuel_consumption(self, load):
        if load < 0:
            raise ValueError("Вес не может быть отрицательным")
        return self.fuel_consumption * (1 + load / self.cargo_capacity)


    def calculate_travel_cost(self, distance, fuel_price, fuel_consumption):
        if distance < 0 or fuel_price <=0 or fuel_consumption <= 0:
            raise ValueError("Ни один из параметром не должен быть меньше нуля")
        fuel_consumed = fuel_consumption * distance / 100
        return fuel_consumed * fuel_price

    def __str__(self):
        return f"Грузовик вмещает {self.cargo_capacity} груза"