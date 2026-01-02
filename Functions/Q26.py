# Using the @changecase decorator on two functions:
def changecase(func):
    def inner():
        return func().upper()
    return inner

@changecase
def newx():
    return "Hello, Harshit"

@changecase
def fun2():
  return "I am speed!"

print(newx())
print(fun2())