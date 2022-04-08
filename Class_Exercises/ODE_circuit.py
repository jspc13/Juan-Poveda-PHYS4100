import numpy as np
import matplotlib.pyplot as plt

RC = 0.1
Vout_initial = 0 # at t=0
h = 0.00001
t_array = np.arange(0,10,h)

def Vin(t):
    if (np.floor(2*t)) % 2 == 0:
        return 1
    else:
        return -1

#for t=0
#vout = 0 + h * ((1/RC)*Vin(0) - 0)

Vout = np.zeros(len(t_array)+1)
for i,t in enumerate (t_array):
    Vout[i+1] = Vout[i] + h * ((1/RC)*(Vin(t) - Vout[i]))

Vout = np.delete(Vout, len(t_array))
plt.plot(t_array,Vout)
plt.show()
