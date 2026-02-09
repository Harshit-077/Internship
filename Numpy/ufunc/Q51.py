# Find the difference of the set1 from set2:
import numpy as np
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
x = np.setdiff1d(set1, set2, assume_unique=True)
print(x)