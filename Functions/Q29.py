# One decorator for upper case, and one for adding a greeting:
def changecase(func):
    def inner():
        return func().upper()
    return inner

def addgreet(func):
    def inner():
        return func()+", how are you?"
    return inner

@changecase
@addgreet
def myfunc():
    return "Harshit"
print(myfunc())