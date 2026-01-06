# Use the Student class to create an object, and then execute the printname method:
class Person:
  def __init__(self, fn, ln):
    self.fname = fn
    self.lname = ln

  def printname(self):
    print(self.fname, self.lname)

class Student(Person):
    pass

x = Student("Harshit", "Sharma")
x.printname()