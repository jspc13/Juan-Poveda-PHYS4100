import numpy as np

def f(x):
    return x**4 - 2*x + 1

a = float(input("Lower limit of integration a = "))
b = float(input("Lower limit of integration b = "))
n = int(input("Number of slices n = "))
deltax = (b-a)/n
N1 = n // 2
N2 = (n // 2) - 1
fsum = 0

for k in range(1,N1):

    fsum = fsum + f(a + (2*k - 1) * deltax)

s = 0

for i in range(1,N2):

    s = s + f(a + 2*i*deltax)

F = deltax * (1/3) * (f(a) + f(b) + 4*fsum + 2*s)

print(F)