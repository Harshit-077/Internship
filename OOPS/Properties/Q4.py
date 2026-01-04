# Delete the age property:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("May",20)
del p1.age
print(p1.age)