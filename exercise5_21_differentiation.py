import numpy as np
import scipy.constants as cons
import matplotlib.pyplot as plt

a,b = 0,100
x = np.arange(a,b,1)
y = np.arange(a,b,1)
ygrid,xgrid = np.meshgrid(x,y)
charge1 = 1
charge2 = -1
xcharge1 = xgrid[45,50]
ycharge1 = ygrid[45,50]
xcharge2 = xgrid[55,50] 
ycharge2 = ygrid[55,50]
potential = np.zeros([b,b])
for i in range(b):
    for j in range(b):
        rcharge1 = (np.sqrt((xcharge1 - xgrid[i,j])**2 + (ycharge1 - ygrid[i,j])**2)) / 100
        rcharge2 = (np.sqrt((xcharge2 - xgrid[i,j])**2 + (ycharge2 - ygrid[i,j])**2)) / 100
        potential1 = charge1 / (4 * cons.pi * cons.epsilon_0 * rcharge1)
        potential2 = charge2 / (4 * cons.pi * cons.epsilon_0 * rcharge2)
        potential[i,j] = potential1 + potential2
#plt.contour(xgrid,ygrid,potential, levels = [-11e10,-3e10, -1e8, -1e5, 0, 1e5, 1e8, 3e10, 11e10])
#plt.show()

#calculating the partials
h = 2 # number of steps, in this case is 1, since we have h/2, then h must be 2
partial_wrt_x = np.zeros([b,b])
partial_wrt_y = np.zeros([b,b])
for i in range(1, b-1):
    for k in range(1, b-1):
        partial_wrt_x[i,k] = (potential[i+1,k] - potential[i-1,k]) / h
        partial_wrt_y[i,k] = (potential[i,k+1]) - potential[i,k-1] / h
plt.quiver(xgrid[0:b:5,0:b:5], ygrid[0:b:5,0:b:5], partial_wrt_x[0:b:5,0:b:5], partial_wrt_y[0:b:5,0:b:5])
plt.show()

# to do:
# need to improve the graph, maybe try a different method to plot