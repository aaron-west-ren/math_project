import math
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return np.log(x)

def linApprox(l):
    return (x-1) # found for when x= 1

def quadraticApprox(Q):
    return .5 * np.square(x-1)

x = np.arange(0.01,4,.1)

y = function(x)

l = linApprox(x)
print(x)
Q = quadraticApprox(x)
print(Q)
q = l + Q
print(q)

print(l)
plt.plot(x,y)
plt.plot(x,l)
plt.plot(x,q)
plt.grid()
plt.xlim(0,4)
plt.ylim(-2,2)
plt.title("liner and quadratic approximations for ln(x) ")
plt.show()
