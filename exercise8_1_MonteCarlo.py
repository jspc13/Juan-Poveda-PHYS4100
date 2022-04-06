import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rng = np.random.default_rng(12345)
L = 101 #lattice
N = 1000 #steps
x = np.arange(0,L,1)
y = np.arange(0,L,1)
position_x = 50
position_y = 50
new_position_x = np.zeros(N)
new_position_y = np.zeros(N)
for i in range(N):
    random_direction = rng.choice(4)
    if random_direction == 0 and position_y < 100:
        position_y = position_y + 1
    if random_direction == 1 and position_y < 100:
        position_y = position_y - 1
    if random_direction == 2 and position_x < 100:
        position_x = position_x + 1
    if random_direction == 3 and position_x < 100:
        position_x = position_x - 1
    new_position_x[i] = position_x
    new_position_y[i] = position_y
#plt.scatter(new_position_x, new_position_y)
#plt.show()
fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(0,100), ylim=(0,100))
particle = plt.Circle((50,50), radius=0.01)

def init():
    particle.center = (50,50)
    ax.add_patch(particle)
    return particle,

def animate(i):
    x = new_position_x[i]
    y = new_position_y[i]
    particle.center = (x,y)
    return particle,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)
writergif = animation.PillowWriter(fps=30)
anim.save('particle_moving.gif', writer=writergif)

#to do:
#animation not working