# Add the __init__() function to the Student class:
class Person:
  def __init__(self, fn, ln):
    self.fname = fn
    self.lname = ln

  def printname(self):
    print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fn, ln):
        super().__init__(fn, ln)
        # Person.__init__(self, fn, ln)

x = Student("Harshit", "Sharma")
x.printname()