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

figure,ax=plt.subplots(1,3, figsize = (16,7))
ax[0].plot(ck_squared_wave * np.conjugate(ck_squared_wave))
ax[0].set_title('Ck Squared Wave')
ax[0].set_yscale('log')
ax[1].plot(ck_sawtooth * np.conjugate(ck_sawtooth))
ax[1].set_title('Ck Sawtooth Wave')
ax[1].set_yscale('log')
ax[2].plot(ck_modulated_sine * np.conjugate(ck_modulated_sine))
ax[2].set_title('Ck Modulated Sine Wave')
ax[2].set_yscale('log')
plt.show()

