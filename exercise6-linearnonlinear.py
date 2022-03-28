import numpy as np
import astropy.constants as c
import astropy.units as u
import matplotlib.pyplot as plt

def function1(E):
    w = 1e-9 * u.m
    insideroot = (((w ** 2) * c.m_e * E) / (2 * c.hbar **2 ))
    return np.tan(np.sqrt(insideroot.value))

def function2(V,E):
    return np.sqrt((V - E)/E)

def function3(V,E):
    return (-1)*np.sqrt(E/(V - E))

EineV = np.arange(0,21,0.0001) * u.eV 
VineV = 20 * u.eV
V = VineV.to(u.J)
E = EineV.to(u.J)
y1 = function1(E)
y1[:-1][np.diff(y1) < 0] = np.nan
plt.plot(EineV,y1)
plt.plot(EineV,function2(V,E))
plt.plot(EineV,function3(V,E))
plt.ylim(-15,15)
plt.show()

def bisection(guess1,guess2,even=True):
    "'This function checks that the guesses have opposite signs, if so, calculates the bisection"
    x1_ineV = guess1 * u.eV
    x2_ineV = guess2 * u.eV
    x1 = x1_ineV.to(u.J)
    x2 = x2_ineV.to(u.J)
    epsilon = 0.001 * u.eV
    if even:
        f1 = function1(x1) - function2(V,x1)
        f2 = function1(x2) - function2(V,x2)
    else:
        f1 = function1(x1) - function3(V,x1)
        f2 = function1(x2) - function3(V,x2)

    if (f1 < 0 and f2 > 0) or (f1 > 0 and f2 < 0):
        while np.abs(x1-x2) > epsilon:
            midpoint = 0.5 * (x1 + x2)
            if even:
                f3 = function1(midpoint) - function2(V,midpoint)
            else:
                f3 = function1(midpoint) - function3(V,midpoint)
            if np.sign(f3) == np.sign(f1):
                x1 = midpoint
            else:
                x2 = midpoint
    else:
        print("Your guesses have the same sign")
    return 0.5 * (x1+x2)

print("According to the graph, the first set of even points guesses are: 2 and 3.26, which gives us the first energy level:", bisection(2,3.26))
print("According to the graph, the second set of even points guesses are: 6.3 and 9, which gives us the second energy level:", bisection(6.3,9))
print("According to the graph, the thrid set of even points guesses are: 13 and 17.6, which gives us the third energy level:", bisection(13,17.6))
print("According to the graph, the first set of odd points guesses are: 0.5 and 2.2, which gives us the fourth energy level:", bisection(0.5,2.2))
print("According to the graph, the second set of odd points guesses are: 3.8 and 6.4, which gives us the fifth energy level:", bisection(3.8,6.4))
print("According to the graph, the third set of odd points guesses are: 9.9 and 12.6, which gives us the sixth energy level:", bisection(9.9,12.6))


