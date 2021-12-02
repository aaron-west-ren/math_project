import numpy as np
from matplotlib import pyplot as plt
pi = 4* np.arctan(1)

a = -4
b = 4
n = 200

dx = (b-a)/n
x = np.arange(a,b,dx)

onepiece = np.piecewise(x, [x <= 0, x >= 0], [lambda x: -x, lambda x: 0])

plt.plot(x, onepiece)
plt.show()
