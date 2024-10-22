#Mean value method for calculating integrals
from random import random
from numpy import empty, pi
N = 1000
V = 4

def func(x,y):
    if (pow(x,2) + pow(y,2)) <= 1:
        return 1
    else:
        return 0
f = empty(N,float)
for i in range(N):
    x = -1 + random()*2
    y = -1 + random()*2
    f[i] = func(x,y)
I = (V/N)*sum(f)
print(I, pi)
