""" FOURIER SERIES IMPLEMENTATION IN PYTHON"""
import numpy as np
import matplotlib.pyplot as plt
#---------------------------------
def func_to_int(x):
    if x == L:
        x = 0
    return (-x**3 + np.sin(x))*(np.exp(-1j*2*np.pi*k*x/L))
#------------------------------------------------
def append_y(x_list):
  y_list = []
  for x in x_list:
    y_list.append(func(x))
  return y_list
y_list = append_y(x_list)
#----------------------------------------
def trap_rule(N,a,b):
    h = (b-a)/N
    sumf = 0.
    for n in range (1,N):
        sumf += func_to_int(a+n*h)
    return h/L * (sumf + 0.5*func_to_int(a) + 0.5*func_to_int(b))
#--------------------------------------
#DFT (discrete fourier transform)

N= 100
L = 2
k = 1
x_list =[]
print(k, trap_rule(N,0,L))
