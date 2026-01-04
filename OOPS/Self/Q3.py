# Use the words myobject and abc instead of self:
class Person:
    def __init__(myobject,name):
        myobject.name = name
    def display(abc):
        print("Hi "+abc.name)

p1 = Person("Emily")
p2 = Person("May")
p1.display()
p2.display()