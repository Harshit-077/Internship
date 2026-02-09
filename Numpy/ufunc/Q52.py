# Find the symmetric difference of the set1 and set2:
import numpy as np
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
a1 = np.setxor1d(a1, a2, assume_unique=True)
print(a1)