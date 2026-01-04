# Call one method from another method using self:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        return "Hi "+self.name
    def update(self):
        x = self.greet()
        print(x + ", Welcome to Person class")

p1 = Person("May",20)
p1.update()