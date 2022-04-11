import numpy as np

#def acceleration_along_x(r, rho, C, m, Vx, Vy):
    #return ((-1 * np.pi * r**2 * rho * C * Vx) / (2 * m)) * np.sqrt(Vx**2 + Vy**2)

#def acceleration_along_y(g, r, rho, C, m, Vx, Vy):
    #return - g - (((-1 * np.pi * r**2 * rho * C * Vy) / (2 * m)) * np.sqrt(Vx**2 + Vy**2))

def acceleration():
    m = 1
    r = 0.08
    thetta = 30
    V = 100
    rho = 1.22
    C = 0.47
    g = 9.8
    Vx = V * np.cos(thetta)
    Vy = V * np.sin(thetta)

    acceleration_along_x = ((-1 * np.pi * r**2 * rho * C * Vx) / (2 * m)) * np.sqrt(Vx**2 + Vy**2)
    acceleration_along_y = - g - (((-1 * np.pi * r**2 * rho * C * Vy) / (2 * m)) * np.sqrt(Vx**2 + Vy**2))

    

    
