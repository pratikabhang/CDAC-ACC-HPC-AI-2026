class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Vehicle:", self.year, self.make, self.model)


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        print("Car:", self.year, self.make, self.model)
        print("Number of doors:", self.num_doors)


vehicle = Vehicle("Volkswagen", "Virtus", 2024)
car = Car("BMW", "X5", 2024, 5)

vehicle.display_info()
car.display_info()