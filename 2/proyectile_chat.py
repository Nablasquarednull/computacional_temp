#Paola blumenkron guerrero
#Andrés Alvarez Rodriguez
from numpy import cos, sin, sqrt, radians, linspace, arange
import matplotlib.pyplot as plt
#Algorithm: set up initial constraints (x_0,Y_o) and (V_x0,V_y0), loop for each t_i value
#Task 1: Implement the algorithm with air resistance (and without) and plot
     # on the same graph
     #Initial Constraints: initial position: (0,0), V_0 = 700 m/s, theta = 45º
#NOTE: we must calculate the position where the trajectory stops to avoid overcalculating negative trajectory.

#------GIVEN CONSTRAINTS----
V_0 = 700  # m/s
theta = 45  # º
x_0 = 0  # m
y_0 = 0  # m
res_const = 4e-5  # 1/m
g = 9.81  # m/s²
delta_t = 0.1
steps = 1100

# Initial velocities
v_x = V_0 * cos(radians(theta))
v_y = V_0 * sin(radians(theta))

# Arrays to store the trajectory
x_array = []
y_array = []
x_res_array = []
y_res_array = []

#--------------------------------
def euler_method(x_0, y_0, v_x, v_y):
    x_n = x_0 + v_x * delta_t
    y_n = y_0 + v_y * delta_t
    v_y = v_y - g * delta_t
    return x_n, v_x, y_n, v_y

def euler_method_resistance(x_0, y_0, v_x, v_y):
    v = sqrt(v_x**2 + v_y**2)
    x_n = x_0 + v_x * delta_t
    v_x = v_x - res_const * v * v_x * delta_t
    y_n = y_0 + v_y * delta_t
    v_y = v_y - (g + res_const * v * v_y) * delta_t
    return x_n, v_x, y_n, v_y

def iterate(x_0, y_0, v_x, v_y, x_array, y_array, method, steps):
    for _ in range(steps):
        x_array.append(x_0)
        y_array.append(y_0)
        x_0, v_x, y_0, v_y = method(x_0, y_0, v_x, v_y)
        if y_0 < 0:  # Stop when trajectory reaches the ground
            break
    return x_array, y_array

# Compute trajectories
x_array, y_array = iterate(x_0, y_0, v_x, v_y, x_array, y_array, euler_method, steps)

# Reinitialize velocities for resistance
v_x_res = V_0 * cos(radians(theta))
v_y_res = V_0 * sin(radians(theta))
x_res_array, y_res_array = iterate(x_0, y_0, v_x_res, v_y_res, x_res_array, y_res_array, euler_method_resistance, steps)

# Convert distances from meters to kilometers
x_array_km = [x / 1000 for x in x_array]
y_array_km = [y / 1000 for y in y_array]
x_res_array_km = [x / 1000 for x in x_res_array]
y_res_array_km = [y / 1000 for y in y_res_array]

# Plot results
plt.plot(x_array_km, y_array_km, label="Without Air Resistance")
plt.plot(x_res_array_km, y_res_array_km, label="With Air Resistance")
plt.xlabel("Horizontal Distance (km)")
plt.ylabel("Vertical Distance (km)")
plt.title("Projectile Motion with and without Air Resistance (in km)")
plt.legend()
plt.grid()
plt.show()

#TASK 2: implement verlets algorith to produce a y-t plot and a E-t plot.
#---INITIAL CONSTRAINTS---
omega = 1
mass = 1
V_0  = 0 # m/s
y_0 = 0.2
t_0 = 0
t_final = 100
delta_t = 0.01 # s (sugerida por la Dra. milagros)
y_1 = y_0 + V_0 * delta_t
steps = int

#------arrays to store energy,position, and time--------
energy_array = []
y_array = []
v_array = []
t_array = arange(t_0,t_final,delta_t)
#---------------------------------------------------
y_array.append(y_0)
y_array.append(y_1)
v_array.append(0)
#--------------------------------------------------
def verlet_method(y_0,y_1,delta_t,omega,mass,v):
    y_2  = 2 * y_1 - y_0 - omega**2 * y_1 * delta_t**2
    v_1 = (y_2 - y_0)/(2*delta_t)
    return y_2,v_1

def energy_calc(v,omega,y):
    return (1/2) * v**2 + (1/2) * omega**2 * y**2
for i in range(1,len(t_array)):
    y_n,v_m = verlet_method(y_array[i-1],y_array[i],delta_t,omega,mass,v_array[i-1])
    v_array.append(v_m)
    y_array.append(y_n)
del y_array[-1]
plt.plot(t_array, y_array,color = 'purple')
plt.xlabel("Time (s)")
plt.ylabel("position (m)")
plt.title("Unidimiensional position of harmonic oscillator")
plt.grid()
plt.show()
for i in range(len(v_array)):
    energy_array.append(energy_calc(v_array[i],omega,y_array[i]))
plt.plot(t_array, energy_array)
plt.xlabel("Time (s)")
plt.ylabel("Energy (en no se qué unidades)")
plt.title("Energy of the harmonic oscillator")
plt.grid()
plt.show()
print(energy_array[0:10])



