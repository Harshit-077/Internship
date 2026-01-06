# A method that changes a property value:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        self.age += 1
        print(f"Hello, I am {self.name} and I will be {self.age} years old this year.")

p1 = Person("Harshit",20)
p1.greet()