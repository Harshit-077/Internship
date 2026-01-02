# A basic decorator that uppercases the return value of the decorated function.
def changecase(func):
    def inner():
        return func().upper()
    return inner

@changecase
def newx():
    return "Hello, Harshit"
print(newx())