# Change data type from integer to boolean:
import numpy as np
arr = np.array([1, 0, 3])
narr = arr.astype(bool)

print(narr)
print(narr.dtype)