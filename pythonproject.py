class Car:

    total_cars = 0
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        Car.total_cars += 1

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

    def discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
        print(f"Discount applied! New price: ${self.price}")



class ElectricCar(Car):
    def __init__(self, brand, model, price, battery_range):
        super().__init__(brand, model, price)
        self.battery_range = battery_range

    def car_info(self):
            super().show_info()
            print(f"Battery range: {self.battery_range}")

class GasCar(Car):
    def __init__(self, brand, model, price, fuel_type):
        super().__init__(brand, model, price)
        self.fuel_type = fuel_type

    def car_info(self):
            super().show_info()
            print(f"Fuel type: {self.fuel_type}")

cars = [
    ElectricCar("Tesla", "Model 3", 45000, 500),
    GasCar("Toyota", "Corolla", 20000, "Petrol"),
    ElectricCar("Nissan", "Leaf", 30000, 350),
    GasCar("Honda", "Civic", 22000, "Petrol")
]


print("=== Car Inventory ===\n")
for car in cars:
    car.car_info()


print(f"Total cars created: {Car.total_cars}")

print("\n=== Testing Discount ===")
cars[0].discount(15)