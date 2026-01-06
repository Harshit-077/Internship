# Create a method in a class:
class Person:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print("Hello "+self.name)
p1 = Person("Harshit")
p1.greet()