# Stop after 20 iterations:
class MyClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
lass = MyClass()
ite = iter(lass)
for y in ite:
    print(y)