import numpy as np

L = 20 # depth in meters
Diffusivity = 0.1 # thermal diffusivity of the Earth
N = 100 # divisions in the grid
h = 1 # time step in days
a = L/N

initial_temperature = 10
Temperature = np.zeros(N) * 10

def temperature_boundary_of_surface(t): # surface x = 0
    A = 10
    B = 12
    tau = 365
    return A + B * np.sin((2*np.pi*t)/tau)

time_end = 365*10 # in years
time_initial = 0
c = h*Diffusivity/(a*a)
Temperature_h = np.zeros(N)

while time_initial < time_end:
    for i in range (1,N):
        Temperature_h[i] = Temperature[i] + c*(Temperature[i+1]+Temperature[i-1]-2 * Temperature[i])
        

