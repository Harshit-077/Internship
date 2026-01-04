# Add a new property to an object:
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Harshit")

p1.age = 25
p1.city = "Tokyo"

print(p1.name)
print(p1.age)
print(p1.city)