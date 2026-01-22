# Change data type from float to integer by using 'i' as parameter value:
import numpy as np
arr = np.array([1.1, 2.1, 3.1])

narr = arr.astype('i')

print(narr)
print(narr.dtype)