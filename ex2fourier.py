import numpy as np
from matplotlib import pyplot as plt
pi = 4 * np.arctan(1)
a = -1
b = 1

n = 200

dx = (b-a)/n
x = np.arange(a,b,dx)

onepiece = np.piecewise(x, [x <= 0, x >=0], [lambda x: -x, lambda x: x])
print(onepiece)
ao = .5

mm = 4
m = np.arange(1,mm,1)

an = 2/np.power(m*pi,2)*(np.cos(m*pi)-1)
print(an)

sum1 = 0

for i in m-1:
    sum1 = sum1 + an[i] * np.cos(m[i]* pi * x)
    #note bn = 0 for odd function
estfx = ao + sum1
plt.plot(x,onepiece, 'b' , label="f(x)")
plt.plot(x, estfx, 'r', label="Fourier Approximation of f(x)")
plt.title(r'Fourier Approximation ex2 Aaron West 11/30/2021')
ax = plt.gca()

ax.legend(frameon=False, loc='upper center', ncol=2)
plt.show()
