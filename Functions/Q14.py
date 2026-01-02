# A function that calculates the sum of any number of values:
def calc(*x):
    total = 0
    for n in x:
        total+=n
    return total
sun = calc(1,2,3,4,5)
print(sun)