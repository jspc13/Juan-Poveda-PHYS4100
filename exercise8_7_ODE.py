import numpy as np
import matplotlib.pyplot as plt

h = 0.01 # in seconds
t_array = np.arange(0,100,h)
#define initial conditons
mass = 1
radius = 0.08 
angle_thetta = np.radians(30) # angle wrt to the horizontal
Velocity_ball = 100
density_air = 1.22 # density of air
coefficient_of_drag = 0.47 # coefficient of drag for a sphere
gravity = 9.8
x_initial = 0
y_initial = 0
Vx_initial = Velocity_ball * np.cos(angle_thetta)
Vy_initial = Velocity_ball * np.sin(angle_thetta)

def f(r, mass = 1):
    dx_dt = r[2]
    dy_dt = r[3]
    dVx_dt = ((-1 * np.pi * radius**2 * density_air * coefficient_of_drag * r[2]) / (2 * mass)) * np.sqrt(r[2]**2 + r[3]**2)
    dVy_dt = -gravity + (((-1 * np.pi * radius**2 * density_air * coefficient_of_drag * r[3]) / (2 * mass)) * np.sqrt(r[2]**2 + r[3]**2))
    return np.array([dx_dt, dy_dt, dVx_dt, dVy_dt])

def runge_kutta(mass):
    r = [x_initial,y_initial,Vx_initial,Vy_initial]
    r_points = np.zeros((len(t_array),4))
    for i in range(len(t_array)):
        r_points[i] = r
        k1 = h*f(r, mass = mass)
        k2 = h*f(r+0.5*k1, mass = mass)
        r = r + k2
    return r_points

run1 = runge_kutta(1)
run2 = runge_kutta(10)
run3 = runge_kutta(100)
run4 = runge_kutta(1000)

plt.plot(run1[:,0], run1[:,1], label = 'Mass = 1 kg')
plt.plot(run2[:,0], run2[:,1], label = 'Mass = 10 kg')
plt.plot(run3[:,0], run2[:,1], label = 'Mass = 100 kg')
plt.plot(run4[:,0], run2[:,1], label = 'Mass = 1000 kg')
plt.legend(loc = 'upper left')
plt.ylim(0, 150)
plt.xlim(0, 1000)
plt.show()