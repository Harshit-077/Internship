# Draw out a sample for dice roll:
import numpy as np
x = np.random.multinomial(6, [1/6,1/6,1/6,1/6,1/6,1/6])
print(x)