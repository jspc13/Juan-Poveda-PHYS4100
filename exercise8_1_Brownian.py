import numpy as np

rng = np.random.default_rng(12345)
L = 101
x = np.arange(0,L,1)
y = np.arange(0,L,1)
particle_x_value = 50
particle_y_value = 50
#move_up = particle_y_value + 1
#move_down = particle_y_value - 1
#move_right = particle_x_value + 1
#move_left = particle_x_value - 1
#random_direction = rng.choice(4) 
position = np.arange(0,L,1)
position_x = position[50,50]
position_y = position[50,50]
for i in range(100):
    random_direction = rng.choice(4)
    if random_direction == 0:
        position_y = position_y + 1
    if random_direction == 1:
        position_y = position_y - 1
    if random_direction == 2:
        position_x = position_x + 1
    if random_direction == 3:
        position_x = position_x - 1

