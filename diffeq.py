import numpy as np
import math
from matplotlib.pyplot import plot, show, scatter
def func(x,t):
    return -x**3+np.sin(t)
x0 = 0
t0 = 0
N= 1000
t_min = 0
t_max = 10
h = (t_max - t_min)/N
def eulers_method(t0,x0, func):
    x = x0
    t = t0
    x_list=[]
    t_list=[]
    for i in np.arange(0,N,h):
       t_list.append(t0)
       x_list.append(x0)
       x = x0+ h*func(x0,t0)
       x0 = x
       t0 = i
    return(x_list,t_list)
def runge_kutta(t0,x0,func,h):
    for i in np.arange(0,N,h):
        k_1 = h*func(x0,t0)
        k_2 = h*func(x0 + h,t0 + h)
    pass
def main():
    plot(t_list,x_list)
    show()
    return 0
main()    


