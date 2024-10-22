""" When we have a function that does not behave particularly nice, the integral done by random sampling method will no be accurate, and every single run will give a different value. This is because we're not sampling correctly, since the sampling is random in the integration variable axis. To avoid this, we use a transformation to sample a uniform distribution, into a weighted sampling, where we consider the "shape" of the function. This should provide an accurate integration with consistent results even if we run the program multiple times."""


#we want to solve the intergral (0 to 1) of (x**(-1/2))/(exp(x)+1))
from numpy import sqrt, exp
from random import random

N = 10**6
w_norm = 2
def transformation(x):
    return sqrt(x)
def gfunc(x):
    return 1/(exp(x)+1)

#generate uniformly distributed numbers
sumg = 0
for i in range(N):
    z = random()
    x = z**2
    sumg += gfunc(x)

I = (1/N)*sumg*w_norm
print(I)

