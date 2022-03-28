import numpy as np
import matplotlib.pyplot as plt

dow = np.loadtxt("dow.txt")
plt.plot(dow)
#plt.show()
coefficients_of_FFT = np.fft.rfft(dow)
coefficients_of_FFT[len(coefficients_of_FFT) * 0.1:] = 