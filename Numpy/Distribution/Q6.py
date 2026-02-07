# Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0:
import numpy as np
x = np.random.logistic(1,2,size=(2,3))
print(x)