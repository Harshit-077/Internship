# Find intersection of the following two set arrays:
import numpy as np
a1 = np.array([1,2,3,4,3,1])
a2 = np.array([4,6,4,2,5,6])

x = np.intersect1d(a1,a2, assume_unique=True)
print(x)