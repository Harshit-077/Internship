# Draw out a sample for pareto distribution with shape of 2 with size 2x3:
import numpy as np
x = np.random.pareto(2, size=(2,3))
print(x)