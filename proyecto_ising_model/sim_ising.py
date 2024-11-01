# Ideal gas simulation using the Metropolis algorithm
# We want to determine the total energy of the gas
from os import system
from time import sleep
from random import random, randrange
from numpy import ones, exp, pi, shape, zeros, copy
import numpy as np
from matplotlib.pyplot import plot, xlabel, ylabel, show, imshow
#------------------------------------
beta = 1
steps = 1000
magnetization = []
#------------------------------------
def random_markov(n):
    M = ones([n,n],int)
    for i in range(n):
        for j in range(n):
            x = random()
            if x <0.5:
                M[i,j] = -1
    return M
#----------------------------------
def energy_cal(markov_chain):
    dim = markov_chain.shape
    interaction_mat1 = zeros((dim[0],dim[1]-1),int)
    interaction_mat2 = zeros((dim[0]-1,dim[1]),int)
    for i in range(dim[0]):
        for j in range(dim[1]-1):
            if markov_chain[i,j] == markov_chain[i,j+1]:
                interaction_mat1[i,j] = -1
            else:
                interaction_mat1[i,j] = 1
    for i in range(dim[0]-1):
        for j in range(dim[1]):
            if markov_chain[i,j] == markov_chain[i+1,j]:
                interaction_mat2[i,j] = -1
            else:
                interaction_mat2[i,j] = 1
    energy_level = np.sum(interaction_mat1) + np.sum(interaction_mat2)
    return energy_level
#-----------------------------------
def magnetization_cal(markov_chain):
    magnetization = np.sum(markov_chain)
#----------------------------------
def markov_evolution(markov_chain):
    i = randrange(N)
    j = randrange(N)
    markov_chain_copy = copy(markov_chain)
    spin = markov_chain_copy[i,j]
    if spin == 1:
        spin = -1
    else:
        spin == 1
    E = energy_cal(markov_chain_copy)
    if random() < exp(-beta*E): #we accept the chain
        return markov_chain_copy
    else:
        return markov_chain #we reject the change
#------------------------------------    
def main_for_linux():
    for i in range(steps):
        system('clear')
        markov_chain = random_markov(20)
        print(markov_chain)
        magnetization.append(magnetization_cal(markov_chain))






