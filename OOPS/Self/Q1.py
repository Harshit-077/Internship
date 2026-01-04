# Use self to access class properties:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Hi "+self.name)
p1 = Person("Harshit",20)
p1.display()