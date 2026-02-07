# Check if a function is a ufunc:
import numpy as np
def add(x,y):
    return x+y
print(type(np.add))