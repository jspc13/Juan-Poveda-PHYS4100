import matplotlib.pyplot as plt
import numpy as np

figure,ax=plt.subplots(1,3, figsize = (6,3))

thetta = np.linspace(0, 6.2)

x = 2 * np.cos(thetta) + np.cos(2 * thetta)

y = 2 * np.sin(thetta) - np.sin(2 * thetta)

ax[0].plot(x, y)

thetta1 = np.linspace(0, 31.4, 1000)

r = thetta1**2

x1 = r * np.cos(thetta1)

y1 = r * np.sin(thetta1)

ax[1].plot(x1,y1)

thetta2 = np.linspace(0, 75.4, 1000)

r1 = np.exp(np.cos(thetta2)) - 2 * np.cos(4 * thetta2) + (np.sin(thetta2 / 12))**5

x2 = r1 * np.cos(thetta2)

y2 = r1 * np.sin(thetta2)

ax[2].plot(y2,x2)

plt.show()
