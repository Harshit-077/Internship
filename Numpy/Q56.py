# Access the splitted arrays:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
narr = np.array_split(arr, 3)

print(narr[0])
print(narr[1])
print(narr[2])