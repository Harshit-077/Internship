# Create an inner class:
class Outer:
    def __init__(self):
        self.name = "Outer Class"
    class Inner:
        def __init__(self):
            self.name = "Inner Class"
        def display(self):
            print("This is inner class")

outer = Outer()
print(outer.name)