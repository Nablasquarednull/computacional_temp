from numpy import arange
import matplotlib.pyplot as plt

# --- INITIAL CONSTRAINTS ---
omega = 1
V_0 = 0  # m/s
y_0 = 0.2
t_0 = 0
t_final = 100
delta_t = 0.01  # s
steps = int((t_final - t_0) / delta_t)

# ------ Arrays to store energy, position, and time --------
energy_array = []
y_array = []
t_array = arange(t_0, t_final, delta_t)

# ---------------------------------------------------
y_array.append(y_0)
y_1 = y_0 + V_0 * delta_t - 0.5 * omega**2 * y_0 * delta_t**2  # Initialize y_1
y_array.append(y_1)

# --------------------------------------------------
def verlet_method(y_0, y_1, delta_t, omega):
    """Update the position using Verlet integration."""
    y_2 = 2 * y_1 - y_0 - omega**2 * y_1 * delta_t**2
    return y_2

def energy_calc(y_array, delta_t, omega):
    """Calculate energy using positions and velocities."""
    energy = []
    for i in range(1, len(y_array) - 1):
        v = (y_array[i + 1] - y_array[i - 1]) / (2 * delta_t)  # Central difference velocity
        e = 0.5 * v**2 + 0.5 * omega**2 * y_array[i]**2  # Total energy
        energy.append(e)
    return energy

# Verlet integration loop
for i in range(1, len(t_array) - 1):
    y_n = verlet_method(y_array[i - 1], y_array[i], delta_t, omega)
    y_array.append(y_n)

# Calculate energy
energy_array = energy_calc(y_array, delta_t, omega)

# Plot position vs. time
plt.figure(figsize=(10, 5))
plt.plot(t_array, y_array[:len(t_array)], color="purple")  # Match lengths
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Unidimensional Position of Harmonic Oscillator")
plt.grid()
plt.show()

# Plot energy vs. time
plt.figure(figsize=(10, 5))
plt.plot(t_array[1:-1], energy_array, color="red")  # Match lengths
plt.xlabel("Time (s)")
plt.ylabel("Energy (arbitrary units)")
plt.title("Energy of the Harmonic Oscillator")
plt.grid()
plt.show()

