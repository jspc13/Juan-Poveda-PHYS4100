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
vx_initial = 0
v_initial = 0
x_initial = 0
y_initial = 0

t = np.arange(0,10,h)

#mass_model_rocket = initial_mass_model_rocket + dmass_model_rocketdt*t

def f(r):
    mass_model_rocket = r[0]
    dydt = r[2]
    dvdt = 1 / mass_model_rocket * (thrust_model_rocket - mass_model_rocket*gravity - drag_coefficient*r[2]**2 - r[2]*dmass_model_rocketdt)
    return np.array([dmass_model_rocketdt, dydt, dvdt])

r = [initial_mass_model_rocket, y_initial, v_initial]
r_points = np.zeros((len(t),3))

for i in range(len(t)):
    r_points[i] = r
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    r = r + k2

plt.plot(t, r_points[:,2])
plt.ylim(bottom=0)
#plt.plot(t,v)
plt.show()