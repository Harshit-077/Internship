# Split the array in 4 parts:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])

narr = np.array_split(arr, 4)

print(narr)