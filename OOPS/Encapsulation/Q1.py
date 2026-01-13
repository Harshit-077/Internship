# Create a private class property named __age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
p1 = Person("Harshit",20)
print(p1.name)