#Algorithm: set up initial constraints (x_0,Y_o) and (V_x0,V_y0)
            #For loop for each t_i value
#Task: Implement the algorithm with air resistance (and without) and plot
     # on the same graph
     #Initial Constraints: initial position: (0,0), V_0 = 700 m/s, theta = 45º
#NOTE: we must calculate the position where the trajectory stops to avoid overcalculating negative trajectory.
from numpy import cos, sin, empty
import matplotlib.pyplot as plt
#------GIVEN CONSTRAINTS----
V_0 = 700 # m/s
theta = 45 #º
x_0 = 0 #m
y_0 = 0#m
res_const = 4e-5 # 1/m
g = 9.81 # m/s² 
#-------------------------
v_x = V_0 * cos(theta)
v_y = V_0 * sin(theta)
delta_t = 0.1
steps = 100
#-------------------------
x_array = []
y_array = []
x_res_array = [] 
y_res_array = []
#--------------------------------
def euler_method(x_0,y_0,v_x,v_y):
    x_n = x_0 + v_x * delta_t
    v_x = v_x
    y_n = y_0 + v_y * delta_t
    v_y = v_y - g * delta_t
    return (x_n,v_x,y_n,v_y)
#-----------------------------------------
def euler_method_resistance(x_0,y_0,v_x,v_y):
    v = sqrt(v_x**2 + v_y**2)
    x_n = x_0 + v_x * delta_t
    v_x = v_x - res_const * v * v_x * delta_t
    y_n = y_0 + v_y * delta_t
    v_y = v_y - (g + res_const * v * v_y ) * delta_t
    return (x_n,v_x,y_n,v_y)
#..........................................
def iterate(x_0,y_0,v_x,v_y,x_array,y_array,method,steps):
    for i in range(steps):
        x_array.append(x_0)
        y_array.append(y_0)
        x_0,v_x,y_n,v_y = method(x_0,y_0,v_x,v_y)
        if y_n < 0:
            break
    return x_array,y_array
#-------------------------------------------
x_array,y_array = iterate(x_0,y_0,v_x,v_y,x_array,y_array,euler_method,steps)
plt.plot(x_array,y_array)
plt.show()

    

