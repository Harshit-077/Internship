# A method that accesses object properties:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")

p1 = Person("Harshit",20)
p1.greet()