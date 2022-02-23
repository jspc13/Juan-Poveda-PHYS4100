import numpy as np
import scipy.constants as cons
import astropy.units as u

def f(x):
    top = x**3
    bottom = np.exp(x)-1
    return top/bottom

a = 0.00001
b = 100
n = 1000
deltax = (b-a)/n
N1 = n // 2
N2 = (n // 2) - 1
fsum = 0
for k in range(1,N1):
    fsum = fsum + f(a + (2*k - 1) * deltax)
s = 0
for i in range(1,N2):
    s = s + f(a + 2*i*deltax)
integral = deltax * (1/3) * (f(a) + f(b) + 4*fsum + 2*s)
sigma = ((cons.k**4 * (u.J /u.K)**4)/(4*cons.pi**2*cons.c**2 * (u.m / u.s)**2 * cons.hbar**3 * (u.J * u.s)**3)) * integral
print(sigma)
