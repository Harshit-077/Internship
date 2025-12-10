# Q7: The "is" operator returns True if both variables point to the same object:
# The is not operator returns True if both variables do not point to the same object:
x = [1,2]
y = [3,4]
z = x
print(x is z)
print(x is y)
print(x==y)
print( x is not y)