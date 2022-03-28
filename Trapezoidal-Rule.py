import numpy as np

def f(x):
    return x**4 - 2*x + 1

def I(a,b,n):
    deltax = (b-a)/n
    fsum = 0
    for k in range(n):
        fsum = fsum + f(a + k * deltax)
    F = deltax * (f(a)/2 + f(b)/2 + fsum)
    return F

e = (1/3) * (I(0,2,20) - I(0,2,10))
print(e)
