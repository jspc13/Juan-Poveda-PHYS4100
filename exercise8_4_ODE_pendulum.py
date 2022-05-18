import numpy as np
import matplotlib.pyplot as plt

#define initial conditions
l = 0.1 # in meters
theta_initial = np.radians(150)
gravity = 9.8
omega_initial = (-1) * gravity / l * np.sin(theta_initial)
h = 0.09 # in seconds
t_array = np.arange(0,6,h)

def f(r):
    dthetadt = r[1]
    domegadt = (-1) * gravity / l * np.sin(r[0])
    return np.array([dthetadt, domegadt])

def runge_kutta():
    r = [theta_initial, omega_initial]
    r_points = np.zeros((len(t_array),2))
    for i in range(len(t_array)):
        r_points[i] = r
        k1 = h*f(r)
        k2 = h*f(r+0.5*k1)
        k3 = h*f(r+0.5*k2)
        k4 = h*f(r+k3)
        r = r + 1/6 * (k1 + 2*k2+ 2*k3 + k4)
    return r_points

run1 = runge_kutta()
#print(run1)

plt.plot(t_array, run1[:,0], linewidth = 1)
plt.show()