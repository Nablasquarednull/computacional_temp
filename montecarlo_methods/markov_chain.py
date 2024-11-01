# Let's say we have a chain of particles, each with a transition probability. i.e, the matrix T_{i,j} determines wether a particular state changes energy level.
#Then, we can prove that the corresponging eigenvector of the leading eigenvalue of the matrix T_{i,j} is in fact a boltzmann distribution, thus...
#if we apply the limit t -> oo to the expression, we are thus led to the conclusion that lim t --> 00 p(t)/lmbda_1 = sum_i C_k (lambda_k/lamda_i)^+ V_k

#IDEAL GAS SIMULATION USING THE METROPOLIS ALGORITHM
from random import random, randrange
from numpy import pi
from matplotlib.python import plot, scatter, show
N = 1000
steps = 250000
beta = 1/10

# CHOOSE INITIAL STATE:
n_x, n_y, n_z = 1,1,1
E = N* (3/2) * pi**2

def main():
    for k in range(steps):
        i = randrange(N)
        j = randrange(3)





