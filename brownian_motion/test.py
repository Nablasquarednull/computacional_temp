from random import random
from numpy import savetxt
def onedim_walk(N,initial_pos,lower_lim,upper_lim):
    pos_list = [initial_pos]
    current_pos = initial_pos
    for i in range(N):
        if current_pos == lower_lim:
            current_pos += 1
        elif current_pos == upper_lim:
            current_pos -= 1
        else:
            x = 2 * random()
            if x <= 1:
                current_pos -= 1
            else:
                current_pos += 1
        pos_list.append(current_pos)
    return pos_list
a = (onedim_walk(100,0,-20,20))
savetxt("prueba.txt",a)
