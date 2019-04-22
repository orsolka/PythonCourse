import matplotlib.pyplot as plt
import numpy as np
c = np.random.poisson(5, 10000)
n_bins = 50
count, bins, ignored = plt.hist(c, n_bins, density=False, color = 'red')
plt.show()
