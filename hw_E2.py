a, m = 3., 2.
import matplotlib.pyplot as plt
import numpy as np
s = (np.random.pareto(a, 1000) + 1) * m
count, bins, _ = plt.hist(s, 100, density=True, color='g')
fit = a*m**a / bins**(a+1)
plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
plt.show()
