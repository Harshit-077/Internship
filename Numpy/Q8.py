# Create an array with 5 dimensions and verify that it has 5 dimensions:
import numpy as np
a = np.array([1,2,3,4,5],ndmin=5)
print(a)
print(a.ndim)