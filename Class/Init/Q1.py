# Create a class named Person, use the __init__() method to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Harshit",20)
print(p1.name)
print(p1.age)