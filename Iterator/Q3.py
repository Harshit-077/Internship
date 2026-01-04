# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
lass = MyClass()
ite = iter(lass)
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
