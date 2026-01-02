# A variable created outside of a function is global and can be used by anyone:
x = 100
def fun1():
    print(x)
fun1()
print(x)