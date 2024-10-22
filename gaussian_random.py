from random import random
from numpy import arange,sqrt,log,pi,empty,where,size
z = 79
e = 1.602e-19
E = 7.7e6 * e #eV
a_0 = 5.29e-11
sigma = a_0/100
epsilon0 = 8.65e-12
b_max = (z*e**2)/(2*pi*epsilon0*E)

N = 1000000
#create uniformly random distributed numbers
z = empty(N,float)
for i in range(N):
    z[i] = random()

#produce gaussian random numbers
r = sqrt(-2*sigma**2*log(1-z))
random_array = where(r < b_max)
print(" The number of atoms that bouced back were: ", size(random_array))
