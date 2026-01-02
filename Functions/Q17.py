# Using * to unpack a list into arguments:
def max(*x):
    total = 0
    for x in x:
        total+=x
    return total
numbers = [1,2,3]
maximum = max(*numbers)
print(maximum)