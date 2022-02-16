import time
import timeit
import numpy as np

start = time.time()
def f(x):
    return np.sqrt(1-x**2)

N = int(input("Please enter the number of steps = "))
print("Program took ", timeit.timeit("2/N","N=1000"), "to divide 2/N")
h = 2/N
s = 0
for k in range(N):
    xk = -1 + h*k
    s = s + f(xk)
print(s*h)

end = time.time()
print(f"Program took :{end-start} seconds to run")