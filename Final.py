import numpy as np
import matplotlib.pyplot as plt

#Model Rocket
#Define constants
initial_mass_model_rocket = 0.05 # in kg
dmass_model_rocketdt = -0.002 #mass burn rate in Kg/s
thrust_model_rocket = 15 # in N
drag_coefficient = 0.02
gravity = 9.8
gravitational_constant = 6.67e-11 # Newton's Gravitational Constant
mass_earth = 5.972e24
radius_earth = 6.37e6
distance_from_radius = 500 # distance covered by the rocket outside of the Earth, in meters
v_0 = 0 
h = 0.01
vx_initial = 0
vy_initial = 0
x_initial = 0
y_initial = 0

t = np.arange(0,10,h)

#mass_model_rocket = initial_mass_model_rocket + dmass_model_rocketdt*t

def f(r):
    mass_model_rocket = r[0]
    dxdt = r[3]
    dydt = r[4]
    dvxdt = 1 / mass_model_rocket * ((r[3]/np.sqrt(r[3]**2 + r[4]**2) * thrust_model_rocket) - (drag_coefficient*r[3]*np.sqrt(r[3]**2 + r[4]**2)) - (r[3]*dmass_model_rocketdt))
    dvydt = 1 / mass_model_rocket * ((r[4]/np.sqrt(r[3]**2 + r[4]**2) * thrust_model_rocket) - (gravitational_constant*((mass_model_rocket*mass_earth)/(radius_earth+distance_from_radius)**2)) - (drag_coefficient*r[4]*np.sqrt(r[3]**2 + r[4]**2)) - (r[4]*dmass_model_rocketdt))
    return np.array([dmass_model_rocketdt, dxdt, dydt, dvxdt, dvydt])


def runge_kutta():
    r = [initial_mass_model_rocket, x_initial, y_initial, vx_initial, vy_initial]
    r_points = np.zeros((len(t),5))

    for i in range(len(t)):
        r_points[i] = r
        k1 = h*f(r)
        k2 = h*f(r+0.5*k1)
        r = r + k2
    return r_points

plt.plot(t, r_points[:,2])
plt.ylim(bottom=0)
#plt.plot(t,v)
#plt.show()

#need to make runga a function, add the mass argument just like for the lab exercise. Maybe also would be good to add thrust, gravity and drag as arguments of the f(x) function