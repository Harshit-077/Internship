# Use a setter method to change a private property:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age < 0:
            raise ValueError('age cannot be negative')
        self.__age = age

p1 = Person("Harshit",20)
print(p1.name)
print(p1.get_age())
p1.set_age(26)
print(p1.get_age())