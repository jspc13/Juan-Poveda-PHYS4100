import numpy as np
import matplotlib.pyplot as plt
from cmath import exp,pi

time_months = np.loadtxt("sunspots.txt", usecols = 0)
sunspots = np.loadtxt("sunspots.txt", usecols = 1)
#plt.plot(time_months, sunspots, linewidth=0.6)
#plt.xlabel("Months")
#plt.ylabel("Sunspots")
#plt.show()

def dft(y):
    "'This function calculates the Discrete Fourier Transform, and returns Ck'"
    N = len(y) #Take N with a value equal to the length of the provided 'y'
    c = np.zeros(N//2+1, complex) # Creates an array of zeros with shape N//2 + 1
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n] * exp(-2j*pi*k*n*n/N)
    return c

fourier_sunspot = dft(sunspots) #ck from the function
ck_squared = np.abs(fourier_sunspot * np.conjugate(fourier_sunspot))
xaxis = np.arange
plt.bar(ck_squared)
plt.ylabel("$\|C_k|^2$")
plt.xlabel("k")
plt.show()