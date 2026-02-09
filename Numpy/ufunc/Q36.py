# Find the GCD for all of the numbers in the following array:
import numpy as np
x = np.array([1,2,3,4,5])
y = np.gcd.reduce(x)
print(y)