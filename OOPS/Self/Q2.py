# The self parameter links the method to the specific object:
class Person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Hi "+self.name)
p1 = Person("Harshit")
p2 = Person("May")
p1.display()
p2.display()