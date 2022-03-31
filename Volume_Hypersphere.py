import numpy as np

rng = np.random.default_rng(12345)
N = 10
x = rng.random(N) * 2 - 1
y = rng.random(N) * 2 - 1
for i in range(N):
    function_x_y = 0
    if x[i]**2 + y[i]**2 <= 1:
        function_x_y = function_x_y + 1
    print(function_x_y)

I = (4 / N) * function_x_y

print(I)