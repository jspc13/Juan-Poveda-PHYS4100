from statistics import mode
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Model Rocket
#Define constants
initial_mass_model_rocket = 0.05 # in kg
dmass_model_rocketdt = -0.002 #mass burn rate in Kg/s
thrust_model_rocket = 15 # in N
drag_coefficient = 0.02
gravity = 9.8
v_0 = 0 
h = 0.01

t = np.arange(0,1,h)

def mass_model_rocket(t):
    return  initial_mass_model_rocket + dmass_model_rocketdt*t

def model(v,t):
    dvdt = 1/mass_model_rocket(t) * (thrust_model_rocket - mass_model_rocket(t)*gravity - drag_coefficient*v**2 - v*dmass_model_rocketdt)
    return dvdt

v = odeint(model, v_0, t)

plt.plot(t,v)
plt.show()