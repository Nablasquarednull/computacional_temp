""" The radioisotope 208 T l (thallium 208) decays to stable 208 P b (lead 208) with a half-life of 3.053 minutes. Suppose we start with a sample of 1000 thallium atoms. Simulate the decay of these atoms over time, mimicking the randomness of that decay using random numbers."""
#PROFESOR NOTE: SIMULATE 100 SECONDS
#RICARDO RODRIGUEZ PINEDA 169048
#EMILIO PACHECO CUAN 172211
#ANDRES ALVAREZ RODRIGUEZ 170060
from random import seed, random, randrange
import numpy as np
import matplotlib.pyplot as plt
thalium_count = 1000
seconds = 1000
half_life = 3.053*60





def decay(t, half_life, thalium_count):
    return (thalium_count*np.exp(-t/half-life))

def main(atom_count,half_life,second_count,delta_t):
    thelist = range(0,1001)
    thalium = [atom_count]
    lead = [0]
    for i in range(second_count):
        decay = 0 
        for N in range(atom_count):
            p = 1 - np.exp(-delta_t/half_life)
            if random() < p:
                decay += 1
        atom_count -= decay
        thalium.append(atom_count)
        lead.append(1000 - atom_count)
    plt.plot(thelist,thalium,lead)
    plt.show()
main(thalium_count,half_life,seconds,1)


