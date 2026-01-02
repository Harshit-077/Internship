# Import functools.wraps to preserve the original function name and docstring.
import functools
def changecase(func):
    @functools.wraps(func)
    def inner():
        return func().upper()
    return inner

@changecase
def fun1():
    return "Hi i am Harshit, how are you?"
print(fun1.__name__)