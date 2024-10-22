#this program uses montecarlo integration to aproximate an integral.
from random import random
from numpy import empty,sin
def func(x):
    return (sin(1/(x*(2-x))))**2
N = 1000
width = 2
height = 1
A = width * height
k = 0
for i in range(N):
    x = random()*width
    y = random()*height
    yf = func(x)
    if y < yf:
        k += 1
I = k *A/N
print(I)
