# Paula Daly Solution to Problem 10 March 2019
# Plotting

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4)
# plotting functions
plt.plot(x, x)
plt.plot(x, x**x)
plt.plot(x, 2**x)

# Display Legend
plt.legend(['y = x', 'y = x2', 'y=2x'], loc='upper left')

plt.show()

