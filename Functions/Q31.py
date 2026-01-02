# Try returning the name from a decorated function and you will not get the same result:
def changecase(func):
    def inner():
        return func().upper()
    return inner
@changecase
def fun1():
    return "Harshit"
print(fun1.__name__)