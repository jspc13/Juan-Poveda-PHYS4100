import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("x", help="enter distance x in light years", type=float)
parser.add_argument("v", help="enter speed v as a fraction of c", type=float)
args = parser.parse_args()
x = args.x
v = args.v
tearth = x / v
print("The time in years that the spaceship takes to reach its destination in the rest frame of an observer on Earth is", tearth)
gamma = math.sqrt(1-(v**2))
tship = tearth / gamma
print("The time in years that the spaceship takes to reach its destination as perceived by a passenger on board the ship is,", tship)



