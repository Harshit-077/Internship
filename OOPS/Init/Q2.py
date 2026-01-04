# Set a default value for the age parameter:
class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age

p1 = Person("Harshit",20)
p2 = Person("someone")
print(p1.name,p1.age)
print(p2.name,p2.age)