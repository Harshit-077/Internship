# Convert the array into a 1D array:

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
narr = arr.reshape(-1)
print(narr)