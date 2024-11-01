# Ideal gas simulation using the Metropolis algorithm
# We want to determine the total energy of the gas

from random import random, randrange
from numpy import ones, exp, pi
from matplotlib.pyplot import plot, xlabel, ylabel, show, imshow

N = 1000
steps = 250000
beta = 1/10

# choose the initial state with
# nx = 1, ny = 1, nz = 1
# M[Nx3] is the matrix that keeps track of the system
# of N particles and 3 quantum numbers: nx, ny and nz
M = ones([N,3],int)
# initial total energy (for all the particles)
E = 3 * pi**2 * N/ 2

# create variable to keep track of the total energy
# which is our variable of interest
total_E = []

for k in range(steps):
    # choose the particle whose state is going to change
    i = randrange(N)
    # choose if the change will be done on nx, or ny or nz
    j = randrange(3)
    # choose with 50% probability that the change will be up or down
    if random()<0.5:
        dn = 1
        dE = (2*M[i,j]+1)*pi*pi/2
    else:
        dn = -1
        dE = (-2*M[i,j]+1)*pi*pi/2
    # Decide whether to accept the move
    # Check first that if nx or ny or nz = 1, a decrement cannot happen
    if M[i,j]>1 or dn==1:
        if random() < exp(-beta*dE):
            # we accept the move
            M[i,j] += dn
            E += dE

    total_E.append(E)

# Make the graph
plot(total_E)
xlabel('Steps')
ylabel('Total energy')
show()
