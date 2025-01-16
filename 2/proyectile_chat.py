#Paola blumenkron guerrero
#Andrés Alvarez Rodriguez
from numpy import cos, sin, sqrt, radians
import matplotlib.pyplot as plt
#Algorithm: set up initial constraints (x_0,Y_o) and (V_x0,V_y0)
            #For loop for each t_i value
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

#TASK 2: 
