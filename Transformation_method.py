import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(12345) #creates the generator
random_decays_1000 = rng.random(size = 1000) # random times of decays of 1000 atoms
Tau = 3.53 * 60
m = 1 / Tau
x = ( - 1 / m ) * np.log(1 - random_decays_1000)
time_of_decays = np.sort(x)
plt.hist(time_of_decays)
plt.show()
