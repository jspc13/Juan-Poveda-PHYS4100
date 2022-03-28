import numpy as np

B = 0.01

for n in range(11):
    E = (n + 0.5)
    e = E * np.exp(-B * E)
    Z = np.exp(-B * E)
    avE = e / Z

    print("When n is", n, "Z is ", Z, "and the value of average energy is:", avE)

