# Add a property called graduationyear to the Student class:
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

x = Student("Harshit", "Sharma",2027)
x.printname()