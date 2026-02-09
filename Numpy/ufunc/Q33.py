# Find the LCM of the values of the following array:
import numpy as np
x = np.array([2,7,3,8,25])
c = np.lcm.reduce(x)
print(c)