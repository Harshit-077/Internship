# Without the __str__() method:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("May", 20)
print(p1)