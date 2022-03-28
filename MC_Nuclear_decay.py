import numpy as np
from random import random

NBi213 = 10000 # number of Bi213 atoms
NTl209 = 0 # number of Tl atoms
NPb209 = 0 # number of Pb atoms
NBi209 = 0 # number of Bi209 atoms
TauBi213 = 46 * 60 # half-life of Bi213 in seconds
TauPb209 = 3.3 * 60 # half-life of Pb209 in seconds
h = 20000 # time steps in seconds
p_213Bi_to_209Pb = 0.9791 # probability of 213Bi to decay into 209Pb
p_213Bi_to_209Tl = 0.209 # probability of 213Bi to decay into 209Tl

def p(t,Tau):
    return 1 - 2**(-t/Tau)

for i in range(NPb209):
    if random < p(1,TauPb209):
        



