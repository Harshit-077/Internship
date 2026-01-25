# Create a filter array that will return only values higher than 42:
import numpy as np
arr1 = np.array([1,2,3,69,48,135,32,40])
filter_arr = []
for x in arr1:
    if x > 42:
        filter_arr.append(x)
for x in filter_arr:
    print(x)
