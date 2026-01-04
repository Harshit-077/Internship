# Access the properties of an object:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("BMW", "M4")

print(car1.brand)
print(car1.model)