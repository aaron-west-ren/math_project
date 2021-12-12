import numpy as np
import scipy.special
import matplotlib.pyplot as plt

"""
    Math Project Problem 3b: plot the first, fourth,
    and 10th partial sum over the interval of convergeance

    f(x) = sum x^n/ n!

"""

n = np.arange(1,4,1)
print(n[0])

x = np.arange(-10,10,1)

b = np.power(x,n) / scipy.special.factorial(n)
print(b)

sum4 =0
#for i in range(1,4,1):
#    sum4 = sum4 + (np.power(x,i) / scipy.special.factorial(n))
#   for i in enumerate(n):
#print(sum4)
