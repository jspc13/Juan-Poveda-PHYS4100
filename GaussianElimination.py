import numpy as np

v = np.array((5,0,5,0), dtype = float)
a = np.array(([4,-1,-1,-1], [-1,3,0,-1], [-1,0,3,-1], [-1,-1,-1,4]), dtype = float)
#first line
v[0] = v[0]/a[0][0]
a[0] = a[0]/a[0][0]
#second line
v[1] = v[1] - (v[0]*a[1,0])
a[1] = a[1] - (a[0]*a[1,0])
#third line
v[2] = v[2] - ()
a[2] = a[2] - (a[2,0]*a[0])

print(v)
print(a)