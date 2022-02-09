import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * (x-1)
a = 1
derivatives = np.zeros(8)
delta = np.zeros(8)
for i in range(8):
    delt = 10**((i+1)*-2)
    der = (f(a+delt) - f(a)) / delt
    derivatives[i] = der
    delta[i] = delt
print(derivatives)
print(delta)
plt.scatter(delta,derivatives)
plt.xscale("log")
plt.show()