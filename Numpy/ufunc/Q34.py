# Find the LCM of all values of an array where the array contains all integers from 1 to 10:
import numpy as np
x = np.arange(1,11)
y = np.lcm.reduce(x)
print(y)