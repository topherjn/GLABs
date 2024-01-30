class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# add a type (like sedan or whatever)
class Car(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

# add number of wheels
class Truck(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

# add displacement in cubic centimeters
class MotorCycle(Vehicle):
    def __init__(self, make, model, year, cc):
        super().__init__(make, model, year)
        self.cc = cc

# test
vehicles = [Car('Mazda', 'Miata', 2006, 'Sport'), Truck('Cheverolet', 'S-10', 1984, 4), MotorCycle('Indian', 'Scout', 1920, 606)]

for vehicle in vehicles:
    print(f"Make: {vehicle.make}, Model: {vehicle.model}, Year: {vehicle.year}")
    # downcast for specifics for each derived class
    if isinstance(vehicle,Car):
        print(f"Type: {vehicle.type}")
    if isinstance(vehicle,Truck):
        print(f"Number of Wheels: {vehicle.num_wheels}")
    if isinstance(vehicle,MotorCycle):
        print(f"Displacement in Cubic Centimeters: {vehicle.cc}")



