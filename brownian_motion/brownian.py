from vpython import *
canvas(width=600, height=600, background=color.black)

particle = sphere(pos=vec(0,0,0), radius=0.3, color=color.yellow, make_trail = True)
velocity = vec(0.5, 0.5, 0)
dt = 1
N = 1000000
count = 0
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
x_axis = onedim_walk(N,0,-50,50)
y_axis = onedim_walk(N,0,-50,50)

    
while count < N:
    rate(30)
    displacement = vec(x_axis[count],y_axis[count],0)
    particle.pos = displacement
    count += 1
