# Access multiple properties using self:
class Car:
    def __init__(self,brand,model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def show(self):
        print(f"Brand: {self.brand},\n Model: {self.model},\n Year: {self.year}")

c1 = Car("BMW", "M4", 2020)
c1.show()