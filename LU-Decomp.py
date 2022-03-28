import numpy as np

a = np.array(([4,-1,-1,-1], [-1,3,0,-1], [-1,0,3,-1], [-1,-1,-1,4]), dtype = float)
v = np.array((5,0,5,0), dtype = float)
print(np.linalg.solve(a,v))