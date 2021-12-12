import numpy as np
import matplotlib.pyplot as plt

x = .5

a = .5

xx = np.arange(-10,10,.1)
xxExact = np.log(xx)

estfx =




exact = np.log(1.5)

n = 5
mapprox = 0
tol = .001

#for i in range(1,10,1):
#    mapprox = (np.power(-1,(i+1)) * np.power(x,i)/i+mapprox)
error = 1
i = 1
while error > tol:

    mapprox = (np.power(-1,(i+1)) * np.power(x,i)/i+mapprox)
    error = np.abs(exact - mapprox)
    i = i + 1

i = i - 1 # removes last i
print(i)

#error = np.abs(exact - mapprox)
print(error)

print(mapprox)

plt.plot(xxExact, xx)
plt.show()
