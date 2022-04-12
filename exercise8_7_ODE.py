import numpy as np

#def acceleration():
    #acceleration_along_x = ((-1 * np.pi * r**2 * rho * C * Vx) / (2 * m)) * np.sqrt(Vx**2 + Vy**2)
    #acceleration_along_y = - g - (((-1 * np.pi * r**2 * rho * C * Vy) / (2 * m)) * np.sqrt(Vx**2 + Vy**2))
    #return 

h = 3 # in seconds
t_array = np.arange(0,100,h)
#define initial conditons
mass = 1
radius = 0.08 
angle_thetta = 30 # angle wrt to the horizontal
Velocity_ball = 100
density_air = 1.22 # density of air
coefficient_of_drag = 0.47 # coefficient of drag for a sphere
gravity = 9.8
x_initial = 0
y_initial = 0
Vx_initial = Velocity_ball * np.cos(angle_thetta)
Vy_initial = Velocity_ball * np.sin(angle_thetta)

def f(x_initial,y_initial,Vx_initial,Vy_initial):
    return ((-1 * np.pi * radius**2 * density_air * coefficient_of_drag * Vx_initial) / (2 * mass)) * np.sqrt(Vx_initial**2 + Vy_initial**2)

x = np.zeros(len(t_array)+1)
y = np.zeros(len(t_array)+1)
Vx = np.zeros(len(t_array)+1)
Vy = np.zeros(len(t_array)+1)
for i,t in enumerate(t_array):
    x[i+1] = x[i] + h * 


