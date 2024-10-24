#Radioactive decay using nonuniform distribution
from numpy import log, empty,sort,flip,arange
from random import random
from matplotlib.pyplot import plot,show
#-----------------------------------------#
#theoretical equation of decay
tmax = 1000
dt = 1
time = arange(0,tmax,dt)
N0 = 1000
tau = 60*60
mu = log(2)/tau
Ntheo = N0 * 2 **(-time/tau)
#uniformly distributed random numbers
z = empty(N0, float)
for i in range(N0):
    z[i] = random()
#nonuniformly distriuted random numbers
t = -(1/mu)*log(1-z)
plot(flip(sort(t)),time)
plot(Ntheo,time)
show()
