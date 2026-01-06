# Create a class named Student, which will inherit the properties and methods from the Person class:
class Person:
  def __init__(self, fn, ln):
    self.fname = fn
    self.lname = ln

  def printname(self):
    print(self.fname, self.lname)

class Student(Person):
    pass

x = Person("Harshit", "Sharma")
x.printname()
