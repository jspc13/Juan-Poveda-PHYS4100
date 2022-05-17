import numpy as np

def p(x):
    return 1/(2*np.sqrt(x))

def g(x):
    return 1 / (np.exp(x)+1)

def w(x):
    return x**(-0.5)

N = 1000000
rng = np.random.default_rng(12345)
x = rng.random(N)**2
sum = 0

for i in range(N):
    sum = sum + g(x[i])

I = 2*sum / N

print(I)
