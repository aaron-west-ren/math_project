import numpy as np
from matplotlib import pyplot as plt
pi = 4* np.arctan(1)

a = -4
b = 4
n = 200

dx = (b-a)/n
x = np.arange(a,b,dx)

onepiece = np.piecewise(x, [x <= 0, x >= 0], [lambda x: -x, lambda x: 0])
twopiece = np.append(onepiece,onepiece)  # double down of onepiece!!

a = -4
b = 12
nn = len(twopiece)  # to increse the number of points change n from above
dx = (b-a)/nn
x = np.arange(a,b,dx) # redef of x to fit new expanded function

mm = 100 #  NOTE: CONTROLL n HERE
       #
m = np.arange(1,mm,1)  # m is an array [1, 2, 3, ... mm]

sum1 = 0  # Initilize someone!!
sum2 = 0  # no one cares about sumtwo

ao = 1
an = -.25 * (np.power(4 / (m * pi), 2) * (1 - np.cos(m * pi)))
bn = 4/(m * pi) * np.cos(m * pi)

#bn = ((4/(m *pi) * np.cos(n * pi)))

for i in m-1:
    sum1 = sum1 + an[i] * np.cos(m[i] * pi * x/4)
    sum2 = sum2 + bn[i] * np.sin(m[i] * pi * x/4)

estfx = 1 + sum1 + sum2
error = abs(twopiece - estfx) # NOTE: error analisis
sumerror = sum(error)
print(sumerror)

plt.plot(x, twopiece)
plt.plot(x, estfx, 'r-')
# plt.title('My Title\n' + r'$\alpha - \omega$ are LaTeX Markup')
plt.title('fourier Approximation of problem #9\n' + r'Aaron West 12/1/2021')

ax = plt.gca()

ax.set_aspect(1.0)

ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=2)
plt.show()
