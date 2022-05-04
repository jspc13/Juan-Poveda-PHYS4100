import numpy as np
from random import random
import matplotlib.pyplot as plt

def f(x):
    m = 1
    b = 0
    return m*x + b

rng = np.random.default_rng(12345)
x = rng.uniform(0,1,50)
y = f(x) + 0.2*rng.normal(0,1,50)

plt.scatter(x,y)
plt.show()

