#Ising array simulation
# Emilio pacheco cuan
#Ricardo rodriguez Pineda
#Andrés Alvarez rodriguez
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
def random_markov(n): #crea un arreglo n x n 2-dimensional de spines con orientación aleatoria
    M = ones([n,n],int)
    for i in range(n):
        for j in range(n):
            x = random()
            if x <0.5:
                M[i,j] = -1
    return M
#----------------------------------
def energy_cal(markov_chain): #calcula el nivel de energía para un arreglo "markov_chain"
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
    return magnetization
#----------------------------------
"""def markov_evolution(markov_chain):
    dim = markov_chain.shape
    row = dim[0]
    col = dim[1]
    i = randrange(row)
    j = randrange(col)
    markov_chain_copy = copy(markov_chain)
    spin = markov_chain_copy[i,j]
    if spin == 1:
        spin = -1
    elif spin == -1:
        spin == 1
    E = energy_cal(markov_chain_copy)
    if random() < exp(-beta * E): #we accept the chain and return the new chain
        return markov_chain_copy
    else:
        return markov_chain #we reject the change and return the original chain"""
#------------------------------------
def markov_evolution(markov_chain):
    dim = markov_chain.shape
    row = dim[0]
    col = dim[1]
    i = randrange(row)
    j = randrange(col)
    spin = markov_chain[i,j]
    
    # Calculate the energy difference due to the spin flip
    delta_E = 2 * spin * (markov_chain[(i+1)%row, j] + markov_chain[(i-1)%row, j] + 
                           markov_chain[i, (j+1)%col] + markov_chain[i, (j-1)%col])

    if random() < np.exp(-beta * delta_E):  # Accept the spin flip
        markov_chain[i, j] *= -1
    
    return markov_chain
#------------------------------------    
def main_for_windows():
    markov_chain = random_markov(20)
    for i in range(steps):
        magnetization.append(magnetization_cal(markov_chain))
        markov_chain = markov_evolution(markov_chain)
    plot(magnetization)
    show()
#------------------------------------
def main_for_linux():
    markov_chain = random_markov(20)

    for i in range(steps):
        # Move the cursor to the top-left corner
        print("\033[H\033[J")

        # Print the updated matrix with aligned columns
        for row in markov_chain:
            for spin in row:
                print(f"{spin:2d}", end=" ")  # Print each spin with a fixed width of 2 characters
            print()  # Move to the next line

        # Update the magnetization
        magnetization.append(magnetization_cal(markov_chain))

        # Evolve the Markov chain
        markov_chain = markov_evolution(markov_chain)

        # Introduce a delay to control the update rate
        sleep(0.01)

    # Print the final magnetization plot
    plot(magnetization)
    show()
#main_for_windows()
main_for_linux()





