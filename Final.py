import numpy as np
import matplotlib.pyplot as plt

#Define Constants
initial_mass_model_rocket = 0.9 # in kg
dmdt_model_rocket = -0.02 #mass burn rate in Kg/s
v_exhaust_model_rocket = -18000
thrust_model_rocket = 15 # in N
drag_coefficient_model_rocket = 0.09
initial_angle = np.radians(30)
deltaV_model_rocket = 1/initial_mass_model_rocket * v_exhaust_model_rocket * dmdt_model_rocket * 1e-8
vx_initial_model_rocket = deltaV_model_rocket * np.cos(initial_angle)
vy_initial_model_rocket = deltaV_model_rocket * np.sin(initial_angle)
initial_mass_rocket = 2030000 # in Kg
dmdt_rocket = -4989.5 # mass burn rate Kg/s
v_exhaust_rocket = -5142 # velocity of exhaust in m/s
drag_coefficient_rocket = 0.9
gravity = 9.8
gravitational_constant = 6.67e-11 # Newton's Gravitational Constant
mass_earth = 5.972e24
radius_earth = 6.37e6
distance_from_radius = 2e6 # distance covered by the rocket outside of the Earth, in meters
deltaV_rocket = 1/initial_mass_rocket * v_exhaust_rocket * dmdt_rocket * 1
vx_initial_rocket = deltaV_rocket * np.cos(initial_angle)
vy_initial_rocket = deltaV_rocket * np.sin(initial_angle)
x_initial = 0
y_initial = 0
h_rocket = 0.1
t_rocket = np.arange(0,200,h_rocket)
h_model_rocket = 0.0001
t_model_rocket = np.arange(0,5,h_model_rocket)
v_0 = 0 

#print(vx_initial_model_rocket, vy_initial_model_rocket)
#g = gravitational_constant*((mass*mass_earth)/(radius_earth+distance_from_radius)**2)

def rocket(r, v_exhaust, dmdt, drag_coefficient):
    mass = r[0]
    dxdt = r[3]
    dydt = r[4]
    dvxdt = (1 / mass) * ((r[3]/np.sqrt(r[3]**2 + r[4]**2) * v_exhaust * (dmdt)) - (drag_coefficient*r[3]*np.sqrt(r[3]**2 + r[4]**2)) - (r[3]*dmdt))
    dvydt = (1 / mass) * ((r[4]/np.sqrt(r[3]**2 + r[4]**2) * v_exhaust * (dmdt)) - (gravity) - (drag_coefficient*r[4]*np.sqrt(r[3]**2 + r[4]**2)) - (r[4]*dmdt))
    return np.array([dmdt, dxdt, dydt, dvxdt, dvydt])

def runge_kutta(initial_mass, vx_initial, vy_initial, t, h, v_exhaust, dmdt, drag_coefficient):
    r = [initial_mass, x_initial, y_initial, vx_initial, vy_initial]
    r_points = np.zeros((len(t),5))

    for i in range(len(t)):
        r_points[i] = r
        k1 = h*rocket(r, v_exhaust=v_exhaust, dmdt=dmdt, drag_coefficient=drag_coefficient)
        k2 = h*rocket(r+0.5*k1, v_exhaust=v_exhaust, dmdt=dmdt, drag_coefficient=drag_coefficient)
        r = r + k2
    return r_points

run1 = runge_kutta(initial_mass_model_rocket, vx_initial_model_rocket, vy_initial_model_rocket, t_model_rocket, h_model_rocket, v_exhaust_model_rocket, dmdt_model_rocket, drag_coefficient_model_rocket)
run2 = runge_kutta(initial_mass_rocket, vx_initial_rocket, vy_initial_rocket, t_rocket, h_rocket, v_exhaust_rocket, dmdt_rocket, drag_coefficient_rocket)
V_model_rocket = np.sqrt(run1[:,3]**2 + run1[:,4]**2)
V_rocket = np.sqrt(run2[:,3]**2 + run2[:,4]**2)

figure,ax=plt.subplots(2,4, figsize = (16,6))
#plot graphs for the model rocket
ax[0,0].plot(t_model_rocket, run1[:,0])
ax[0,0].set_xlabel('Time (s)')
ax[0,0].set_ylabel('Mass (kg)')
ax[0,0].set_title('Mass vs Time Model Rocket')
ax[0,1].plot(t_model_rocket, run1[:,1])
ax[0,1].set_xlabel('Time (s)')
ax[0,1].set_ylabel('X (m)')
ax[0,1].set_title('Position X vs Time Model Rocket')
ax[0,2].plot(t_model_rocket, run1[:,2]) # y vs time
ax[0,2].set_ylim(0,20)
ax[0,2].set_xlabel('Time (s)')
ax[0,2].set_ylabel('Y (m)')
ax[0,2].set_title('Position Y vs Time Model Rocket')
ax[0,3].plot(t_model_rocket, V_model_rocket) # V vs time
ax[0,3].set_xlabel('Time (s)')
ax[0,3].set_ylabel('V (m/s)')
ax[0,3].set_title('Velocity vs Time Model Rocket')
#rocket
ax[1,0].plot(t_rocket, run2[:,0]) # mass vs time
ax[1,0].set_xlabel('Time (t)')
ax[1,0].set_ylabel('Mass (kg)')
ax[1,0].set_title('Mass vs Time Rocket')
ax[1,1].plot(t_rocket, run2[:,1]) # x vs time
ax[1,1].set_xlabel('Time (s)')
ax[1,1].set_ylabel('X (m)')
ax[1,1].set_title('Position X vs Time Rocket')
ax[1,2].plot(t_rocket, run2[:,2]) # y vs time
#ax[1,2].set_ylim(0,20)
ax[1,2].set_xlabel('Time (s)')
ax[1,2].set_ylabel('Y (m)')
ax[1,2].set_title('Position Y vs Time Rocket')
ax[1,3].plot(t_rocket, V_rocket) # V vs time
ax[1,3].set_xlabel('Time (s)')
ax[1,3].set_ylabel('V (m/s)')
ax[1,3].set_title('Velocity vs Time Rocket')
plt.subplots_adjust(wspace=0.5, hspace=0.5) #adjust width and height between plots
#plt.show()

