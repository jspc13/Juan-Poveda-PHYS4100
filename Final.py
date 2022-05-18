import numpy as np
import matplotlib.pyplot as plt

#Define Constants
initial_mass_model_rocket = 0.05 # in kg
dmdt_model_rocket = -0.002 #mass burn rate in Kg/s
thrust_model_rocket = 15 # in N
drag_coefficient_model_rocket = 0.02
initial_mass_rocket = 20000 # in Kg
dmdt_rocket = 0.046 * initial_mass_rocket * (-1) # mass burn rate Kg/s
v_exhaust_rocket = 500 # velocity of exhaust in m/s
drag_coefficient_rocket = 0.1
gravity = 9.8
gravitational_constant = 6.67e-11 # Newton's Gravitational Constant
mass_earth = 5.972e24
radius_earth = 6.37e6
distance_from_radius = 500 # distance covered by the rocket outside of the Earth, in meters
vx_initial = 0
vy_initial = 0
x_initial = 0
y_initial = 0
h = 0.01
t = np.arange(0,10,h)
v_0 = 0 

#mass_model_rocket = initial_mass_model_rocket + dmass_model_rocketdt*t

def model_rocket(r):
    mass_model_rocket = r[0]
    dxdt = r[3]
    dydt = r[4]
    dvxdt = 1 / mass_model_rocket * ((r[3]/np.sqrt(r[3]**2 + r[4]**2) * thrust_model_rocket) - (drag_coefficient*r[3]*np.sqrt(r[3]**2 + r[4]**2)) - (r[3]*dmdt_model_rocket))
    dvydt = 1 / mass_model_rocket * ((r[4]/np.sqrt(r[3]**2 + r[4]**2) * thrust_model_rocket) - (gravitational_constant*((mass_model_rocket*mass_earth)/(radius_earth+distance_from_radius)**2)) - (drag_coefficient*r[4]*np.sqrt(r[3]**2 + r[4]**2)) - (r[4]*dmdt_model_rocket))
    return np.array([dmdt_model_rocket, dxdt, dydt, dvxdt, dvydt])

def rocket(r, v_exhaust, dmdt, drag_coefficient):
    mass = r[0]
    dxdt = r[3]
    dydt = r[4]
    dvxdt = 1 / mass * ((r[3]/np.sqrt(r[3]**2 + r[4]**2) * v_exhaust * np.absolute(dmdt)) - (drag_coefficient*r[3]*np.sqrt(r[3]**2 + r[4]**2)) - (r[3]*dmdt))
    dvydt = 1 / mass * ((r[4]/np.sqrt(r[3]**2 + r[4]**2) * v_exhaust * np.absolute(dmdt)) - (gravitational_constant*((mass*mass_earth)/(radius_earth+distance_from_radius)**2)) - (drag_coefficient*r[4]*np.sqrt(r[3]**2 + r[4]**2)) - (r[4]*dmdt))
    return np.array([dmdt, dxdt, dydt, dvxdt, dvydt])

def runge_kutta(initial_mass, v_exhaust, dmdt, drag_coefficient):
    r = [initial_mass, x_initial, y_initial, vx_initial, vy_initial]
    r_points = np.zeros((len(t),5))

    for i in range(len(t)):
        r_points[i] = r
        k1 = h*rocket(r, v_exhaust=v_exhaust, dmdt=dmdt, drag_coefficient=drag_coefficient)
        k2 = h*rocket(r+0.5*k1, v_exhaust=v_exhaust, dmdt=dmdt, drag_coefficient=drag_coefficient)
        r = r + k2
    return r_points

run1_model_rocket = runge_kutta(initial_mass_rocket, v_exhaust_rocket, dmdt_rocket, drag_coefficient_rocket)

plt.plot(t, run1_model_rocket[:,0])
#plt.ylim(bottom=0)
#plt.plot(t,v)
plt.show()

#need to make runga a function, add the mass argument just like for the lab exercise. Maybe also would be good to add thrust, gravity and drag as arguments of the f(x) function