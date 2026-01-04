# Class property vs instance property:
class Person:
    species = "Human" # Class property

    def __init__(self, name):
        self.name = name # Instance property


p1 = Person("Emily")
p2 = Person("May")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)