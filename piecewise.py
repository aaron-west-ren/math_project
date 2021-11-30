# question 9

import numpy as np
from matplotlib import pyplot as plt
import array
import math

pi = 4* np.arctan(1)     # here is a neat way to calculate pi
print(pi)
a = -pi
b = pi
n = 100

dx  = (b-a)/n
x = np.arange(a,b,dx)

# the following is my workaround for creating the peasewise result
onePeriod = np.piecewise(x, [x <= 0, x >= 0], [lambda x: 0, lambda x: x])
twoPeriod = np.append(onePeriod,onePeriod)
fourPeriod = np.append(twoPeriod,twoPeriod)
y = fourPeriod
print(y)
# re definition of a, b, and n
a = -3*pi # error
b = 5*pi
n = n*4
dx  = (b-a)/n
x = np.arange(a,b,dx)



mm = 100
m = np.arange(1,mm,1) # number of terms in sum
a0 = pi/4



an = (np.cos(m*pi)-1)/(pi*np.power(m,2))
bn = (np.cos(m*pi))/m

print(an[0])
sum1 = 0
sum2 = bn[0]
print(sum1)

for i in m-1:
    print(i)
    sum1 = sum1 + an[i] * np.cos(pi*x)
    sum2 = sum2 + bn[i] * np.sin(pi*x)


estfx = a0 + sum1 - sum2

print(estfx)
plt.figure(figsize=(25, 25))
#plt.style.use('seaborn-poster')
plt.plot(x,y, x, estfx)
plt.title(r'Taylor Approximation ex.1')

ax = plt.gca()
ax.grid(True)
ax.set_aspect(1.0)

ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=2)
#ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
#ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
#ax.xaxis.set_major_formatter(plt.FuncFormatter(multipleformatter()))
plt.show()
