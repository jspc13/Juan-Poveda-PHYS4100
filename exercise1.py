import math

import sys

print("This program calculates the time it takes a ball to hit the ground")

g = 9.8

if len(sys.argv)!=2:
    h = float(input("Enter the height of the tower in meters = "))
else:
    h = float(sys.argv[1])
    
t = math.sqrt(2*h / g)

print("The time it takes the ball to hit the ground, when dropped by a height of", h, "m is = ", t)    