import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as cons

def square_wave(x):
    N = int(len(x))
    y = np.zeros(N)
    y[0:N//2] = 1
    y[N//2:] = - 1
    return y

def sawtooth(x):    
    return x

def modulated_sine(x):
    N = len(x)
    return np.sin((cons.pi * x) / N) * np.sin((20 * cons.pi * x) / N)

x = np.linspace(0,1000,1000)
#plt.plot(sawtooth(x))
#plt.plot(square_wave(x))
#plt.plot(modulated_sine(x))
#plt.show()

ck_squared_wave = np.fft.rfft(square_wave(x))
ck_sawtooth = np.fft.rfft(sawtooth(x))
ck_modulated_sine = np.fft.rfft(modulated_sine(x))

plt.plot(ck_squared_wave * np.conjugate(ck_squared_wave))
plt.xlim([0,20])
plt.yscale("log")
#plt.plot(ck_sawtooth * np.conjugate(ck_sawtooth))
#plt.plot(ck_modulated_sine * np.conjugate(ck_modulated_sine))
plt.show()

