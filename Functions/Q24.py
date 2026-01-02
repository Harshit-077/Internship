# If you use the nonlocal keyword, the variable will belong to the outer function:
def fun1():
    x = 100
    def fun2():
        nonlocal x
        x = 200
        print(x)
    fun2()
    print(x)
fun1()