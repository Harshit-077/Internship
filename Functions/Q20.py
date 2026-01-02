# The local variable can be accessed from a function within the function:
def fun1():
    x = 100
    def fun2():
        print(x)
    fun2()

fun1()