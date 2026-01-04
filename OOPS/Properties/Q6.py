# Change a class property:
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("May")
p2 = Person("Emily")

Person.lastname = "Aggarwal"

print(p1.lastname)
print(p2.lastname)