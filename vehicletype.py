class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def info(self):
        print("This is a vehicle")

class car(Vehicle):
    def __init__(self, brand , model):
        super().__init__(brand)
        self.model = model

    def info(self):
        print("This is a car")
        
car1 = car("BMW", "M4")
print(car1.brand)
print(car1.model)

car1.info()
print(issubclass(car, Vehicle))