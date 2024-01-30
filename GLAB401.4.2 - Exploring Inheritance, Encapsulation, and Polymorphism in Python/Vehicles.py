class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

class Truck(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

class MotorCycle(Vehicle):
    def __init__(self, make, model, year, cc):
        super().__init__(make, model, year)
        self.cc = cc

vehicles = [Car('Mazda', 'Miata', 2006, 'Sport'), Truck('Cheverolt', 'S-10', 1984, 4), MotorCycle('Indian', 'Scout', 1920, 606)]



