import numpy as np

def r(x,y):
    return x**2 + y**2
rng = np.random.default_rng(12345)
N = 100
x = rng.random(N) * 2 - 1
y = rng.random(N) * 2 - 1
for i in range(N):
    r = r(x[i],y[i])
Integral_answer = 4 / N * r
print(Integral_answer)