# Draw out a sample for zipf distribution with distribution parameter 2 with size 2x3:
import numpy as np
x = np.random.zipf(2,size=(2,3))
print(x)