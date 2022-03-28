import numpy as np
from random import random

def f(x):
    return (np.sin( 1 / (x * (2 - x))))**2

N = 10000 # number of points to evaluate the integral
rng = np.random.default_rng(12345)
count = 1
x = rng.random(N) * 2
y = f(x)
for i in range(N): 
    if y < f(x):
        count = count + 1

Integral_answer = 2 * count /N
print(Integral_answer)

