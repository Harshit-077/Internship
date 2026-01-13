# Pass the outer class instance to the inner class:
class Outer:
    def __init__(self):
        self.name = "Outer Class"
    class Inner:
        def __init__(self):
            self.name = "Inner Class"
            self.outer = outer
        def display(self):
            print(f"This is outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner()
inner.display()
