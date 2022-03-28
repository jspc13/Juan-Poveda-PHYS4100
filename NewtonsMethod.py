import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

def P(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

def calcderivative(x):
    return (924*6)*x**5 - (2772*5)*x**4 + (3150*4)*x**3 - (1680*3)*x**2 + (420*2)*x - 42

def guessroot(x):
    return x - P(x)/calcderivative(x)

x = np.arange(0,1,0.001)
y = P(x)
plt.plot(x,y)
#plt.show()

guess = [0.03, 0.16, 0.38, 0.61, 0.81, 0.91]
for g in guess:
    epsilon = 1
    x = g
    while epsilon > 1e-10:
            x2 = guessroot(x)
            epsilon = np.abs(x2 - x)
            x = x2
    print(x, x2, P(x))