import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 + 0.5 * np.tanh(2*x)
def ans(x):
    return (1/np.cosh(2*x))**2
h = 1e-5
x = np.linspace(-2,2)
central = (f(x+(h/2)) - f(x-(h/2)))/h
answer = ans(x)
plt.scatter(x,central, marker='.', color='k')
plt.scatter(x,answer, marker='_', color='r')
plt.show()


#def centraldifference(x):
    #h = 1e-2
    #return (P(x + h/2) - P(x - h/2)) / h
