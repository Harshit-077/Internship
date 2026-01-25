# Create a filter array that will return only values higher than 42:
import numpy as np
arr1 = np.array([1,2,3,69,48,135,32,40])
filter_arr = arr1>42
arr2 = arr1[filter_arr]
for x in arr2:
    print(x)