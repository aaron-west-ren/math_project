import numpy as np
from matplotlib import pyplot as plt

pi = 4 * np.arctan(1)

a = -pi
b = pi
n = 200

dx = (b-a)/n
x = np.arange(a,b,dx)

onepiece = np.piecewise(x, [x <= 0,x >=0], [lambda x: 0, lambda x: x])
twopiece = np.append(onepiece,onepiece)
fourpiece = np.append(twopiece,twopiece)  # fourpice is the piecewise function evaluated four times, total length is 8pi


a = -3 * pi
b = 5 * pi
nn = len(fourpiece)
dx = (b-a)/nn
x = np.arange(a,b,dx) # redefinition of x

mm = 10
m = np.arange(1,mm,1)  # this is the nmber of terms in each sum

an = (np.cos(m*pi)-1)/(pi*np.power(m,2))
bn = (np.cos(m*pi))/m

sum2 = 0
sum1 = 0
for i in m-1:
    sum1 = sum1 + an[i] * np.cos(m[i] * x)
    sum2 = sum2 + bn[i] * np.sin(m[i] * x)


a0 = pi/4
estfx = a0 + sum1 - sum2
error = estfx-fourpiece

print(error)

plt.figure(figsize=(25, 25))
plt.plot(x, fourpiece, x, estfx)
plt.title(r'Taylor Approximation ex.1')

ax = plt.gca()
ax.grid(True)
ax.set_aspect(1.0)

ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=2)
plt.show()
