# Functions with arguments can also be decorated:
def changecase(func):
  def inner(x):
    return func(x).upper()
  return inner

@changecase
def fun2(nam):
  return "Hello " + nam

print(fun2("Harshit"))