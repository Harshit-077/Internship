# If you use the global keyword, the variable belongs to the global scope:
x = 100
def newx():
    global x
    x = 200
    print(x)
newx()
print(x)