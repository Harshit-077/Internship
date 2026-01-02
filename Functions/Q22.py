# The function will print the local x, and then the code will print the global x:
x = 100
def newx():
    x = 200
    print(x)
newx()
print(x)