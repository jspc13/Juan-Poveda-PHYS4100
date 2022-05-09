import numpy as np
from random import random
import matplotlib.pyplot as plt

def f(x):
    m = 1
    b = 0
    return m*x + b

N = 100
i = 0
new_params_zero = np.zeros(N)
new_params_one = np.zeros(N)
for i in range(N):
    rng = np.random.default_rng()
    x = rng.uniform(0,1,50)
    y = f(x) + 0.2 * rng.normal(0,1,50)
    sigma = np.ones(50) * 0.2
    params, error_matrix = np.polyfit(x, y, 1, w = 1/sigma, cov=True)
    new_x = np.linspace(0,1)
    new_params_zero[i] = params[0]
    new_params_one[i] = params[1]

plt.hist(new_params_zero)
plt.hist(new_params_one)
plt.show()
