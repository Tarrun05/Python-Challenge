# Created a class named Vehicle and displayed it's Informations

class Vehicle:
    def __init__(self, RegNo, Fuel, Mileage):
        self.RegNo = RegNo
        self.Fuel = Fuel
        self.Mileage = Mileage
    def __str__(self):
        return f"1. Vehicle's register number is { self.RegNo } and that is of fuel type { self.Fuel } and gives mileage upto { self.Mileage } \n"

vehicle = Vehicle(578, "Petrol", "36.2 Km/L")
print(vehicle)

# Created another class named Bike which is inherited from Vehicle class to display Bike's informations

class Bike(Vehicle):
    def __init__(self, RegNo, Fuel, Mileage):
        super().__init__(RegNo, Fuel, Mileage)
    def __str__(self):
        return f"2. Bike's register number is { self.RegNo } and that is of fuel type { self.Fuel } and gives mileage upto { self.Mileage } \n"

bike = Bike(258, "Petrol", "17.3 Km/L")
print(bike)

# Created another class named Car which is inherited from Vehicle class to display Car's informations

class Car(Vehicle):
    def __init__(self, RegNo, Fuel, Mileage):
        super().__init__(RegNo, Fuel, Mileage)
    def __str__(self):
        return f"3. Car's register number is { self.RegNo } and that is of fuel type { self.Fuel } and gives mileage upto { self.Mileage } \n"

car = Car(633, "Diesel", "12.4 Km/L")
print(car)