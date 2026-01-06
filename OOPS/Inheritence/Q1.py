# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self, fn, ln):
    self.fname = fn
    self.lname = ln

  def printname(self):
    print(self.fname, self.lname)


x = Person("Harshit", "Sharma")
x.printname()