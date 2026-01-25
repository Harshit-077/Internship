# Create a filter array that will return only even elements from the original array:
import numpy as np
arr1 = np.array([1,2,3,69,48,135,32,40])
filter_arr = arr1%2==0
arr2 = arr1[filter_arr]
for x in arr2:
    print(x)