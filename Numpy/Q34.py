# Print the value of the base attribute to check if an array owns it's data or not:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
z = arr.copy()
a = arr.view()
print(z.base)
print(a.base)