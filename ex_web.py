

from sympy import series, Symbol
from sympy.functions import sin, cos, exp
from sympy.plotting import plot
import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = 13,10
plt.rcParams['lines.linewidth'] = 2


# Define symbol
x = Symbol('x')


# Function for Taylor Series Expansion

def taylor(function, x0, n):
    """
    Parameter "function" is our function which we want to approximate
    "x0" is the point where to approximate
    "n" is the order of approximation
    """
    return function.series(x,x0,n).removeO()


print('sin(x) =', taylor(sin(x), 0, 4))

print('cos(x) =', taylor(cos(x), 0, 4))

print('e(x) =', taylor(exp(x), 0, 4))
