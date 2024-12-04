#neural network as memory
#modeled by Ising model
#implemented using MC method

from numpy import ones, empty, reshape, copy
from matplotlib.pyplot import imshow, plot, show, gray
from random import random, randrange
N = 10
# Letter A
sA = ones((N,N), int)*(-1)
sA[0,4:6] = 1
sA[1,3:7] = 1
sA[2,2],sA[2,3],sA[2,6],sA[2,7] = 1,1,1,1
sA[3,1],sA[3,2],sA[3,7],sA[3,8] = 1,1,1,1
sA[4,1:9] = 1
sA[5,0:10] = 1
sA[6,0],sA[6,1],sA[6,2] = 1,1,1
sA[6,7],sA[6,8],sA[6,9] = 1,1,1
sA[7,0],sA[7,1],sA[7,8],sA[7,9] = 1,1,1,1
sA[8,0],sA[8,1],sA[8,8],sA[8,9] = 1,1,1,1
sA[9,0],sA[9,1],sA[9,8],sA[9,9] = 1,1,1,1

# Letter C
sC = ones((N,N), int)*(-1)
sC[1,8],sC[1,9]= 1,1
sC[1,5],sC[1,6],sC[1,7] = 1,1,1
sC[1,2],sC[1,3],sC[1,4] = 1,1,1
sC[2,1],sC[2,2] = 1,1
sC[3,0],sC[3,1] = 1,1
sC[4,0],sC[4,1] = 1,1
sC[5,0],sC[5,1] = 1,1
sC[6,0],sC[6,1] = 1,1
sC[7,1],sC[7,2] = 1,1
sC[8,2],sC[8,3],sC[8,4] = 1,1,1
sC[8,5],sC[8,6],sC[8,7] = 1,1,1
sC[8,8],sC[8,9] = 1,1

# Letter B
sB = ones((N,N), int)*(-1)
sB[0,2:8] = 1
sB[1,1],sB[1,8] = 1,1
sB[2,1],sB[2,8] = 1,1
sB[3,1],sB[3,8] = 1,1
sB[4,1:8] = 1
sB[5,1:8] = 1
sB[6,1],sB[6,8] = 1,1
sB[7,1],sB[7,8] = 1,1
sB[8,1],sB[8,8] = 1,1
sB[9,2:8] = 1

# different style for A
s_array = ones((N,N), int)*(-1)
s_array[0,4:7] = 1
s_array[1,3], s_array[1,7] = 1,1
s_array[2,3], s_array[2,7] = 1,1
s_array[3,2], s_array[3,8] = 1,1
s_array[4,1], s_array[4,8] = 1,1
s_array[5,0], s_array[5,9] = 1,1
s_array[6,0], s_array[6,9] = 1,1
s_array[7,0], s_array[7,9] = 1,1
s_array[8,0], s_array[8,9] = 1,1
s_array[9,0], s_array[9,9] = 1,1

# letter V
s_array[9,4:6] = 1
s_array[8,3], s_array[8,7] = 1,1
s_array[7,3], s_array[7,7] = 1,1
s_array[6,1], s_array[6,8] = 1,1
s_array[5,1], s_array[5,8] = 1,1
s_array[4,0], s_array[4,9] = 1,1
s_array[3,0], s_array[3,9] = 1,1
s_array[2,0], s_array[2,9] = 1,1
s_array[1,0], s_array[1,9] = 1,1
s_array[0,0], s_array[0,9] = 1,1

#calculate the energy
def calc_energy(Jmatrix,array):
    E = 0
    for i in range(N*N):
        for j in range(i+1,N*N):
            E += (-1)*array[0,i]*Jmatrix[i,j]*array[0,j]
    return E

imshow(sA)
gray()
show()
# we need to create Jij
#reshape sA
sA_array = reshape(sA,(1,N*N))
Jmatrix = empty((N*N,N*N),float)
for i in range(N*N-1):
    for j in range(N*N):
        Jmatrix[i,j] = sA[0,i]*sA[0,j]
print(calc_energy(Jmatrix,sA_array))

#changing 20% letter A pattern
s_array =  copy(sA_array)
t = 0
while t < 20:
    i = randrange(N*N)
    s_array[0,i] *= (-1)
    t += 1
imshow(reshape(s_array,(N,N)))






