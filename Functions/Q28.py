# A decorator factory that takes an argument and transforms the casing based on the argument value.
def changecase(n):
    def changecase(func):
        def inner():
            if n==1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return inner
    return changecase
@changecase(2)
def myfunc():
    return "Hello how are you?"
print(myfunc())
