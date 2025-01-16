import numpy as np

import matplotlib.pyplot as plt
# Define parameter L
k_values = [0,1,2]
L = 2 * np.pi
x = np.linspace(-L, L, 1000)

# Plot Psi+ for k = 1, 2, 3 from -L to L
plt.figure(figsize=(10, 5))
for k in k_values:
    plt.plot(x, np.cos(k * x), label=fr'$\Psi_+(x) = \cos({k}x)$')
plt.title(f'Wavefunction $\Psi_+$ ')
plt.xlabel('x')
plt.ylabel(r'$\Psi_+$')
plt.axhline(0, color='black', lw=0.8, linestyle='--')
plt.grid(True)
plt.legend()
plt.show()

# Plot Psi- for k = 1, 2, 3 from -L to L
plt.figure(figsize=(10, 5))
for k in k_values:
    plt.plot(x, np.sin(k * x), label=fr'$\Psi_-(x) = \sin({k}x)$')
plt.title(f'Wavefunction $\Psi_-$ ')
plt.xlabel('x')
plt.ylabel(r'$\Psi_-$')
plt.axhline(0, color='black', lw=0.8, linestyle='--')
plt.grid(True)
plt.legend()
plt.show()

