# Given 10 trials for coin toss generate 10 data points:
import numpy as np
x = np.random.binomial(10,0.5,size=(10))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(np.random.binomial(n=10, p=0.5, size=10))

plt.show()