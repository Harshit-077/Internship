# Make a view, change the original array, and display both arrays:
# Make a view, change the view, and display both arrays:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
a = arr.view()
arr[0] = 100
print(arr)
print(a)