# Add a method called welcome to the Student class:
from typing import override


class Person:
  def __init__(self, fn, ln):
    self.fname = fn
    self.lname = ln

  def printname(self):
    print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fn, ln,grad):
        super().__init__(fn, ln)
        self.graduationyear = grad
        # Person.__init__(self, fn, ln)
    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)
    @override
    def printname(self):
        print(self.fname, self.lname, self.graduationyear)

x = Student("Harshit", "Sharma",2027)
x.printname()
x.welcome()