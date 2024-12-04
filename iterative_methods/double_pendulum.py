from numpy import empty, sin, max, pi
from matplotlib.pyplot import plot, show, xlabel, ylabel, xlim, ylim, legend, yscale,savefig
final_time = 200
initial_time = 0
delta_t = 0.04
L = 9.81
g = 9.81
q = 0.5
F_D = 0.5
omega_D = 2/3
# number of steps
steps = int((final_time - initial_time)/delta_t)
# initial conditions:
theta_0 = 0.2 # ~ 1 degrees
omega_0 = 0
theta_1 = 0.2
omega_1 = 0
#------------------------
theta = empty(steps, float)
theta_a = empty(steps, float)
omega = empty(steps, float)
omega_a = empty(steps, float)
time = empty(steps, float)
#--------------------------
omega[0] = omega_0
omega_a[0] = omega_1
time[0] = initial_time
theta[0] = theta_0
theta_a[0] = theta_1
for i in range(steps-1):
    time[i+1] = time[i] + delta_t
    omega[i+1] = omega[i] - ((g/L)*sin(theta[i]) +q*omega[i] + F_D*sin(omega_D*time[i]))*delta_t
    theta[i+1] = theta[i] + omega[i+1] * delta_t
    if theta[i+1] < -pi:
        theta[i+1] = theta[i+1] + 2*pi
    if theta[i+1] > pi:
        theta[i+1] = theta[i+1] - 2*pi
for i in range(steps-1):
    time[i+1] = time[i] + delta_t
    omega_a[i+1] = omega_a[i] - ((g/L)*sin(theta[i]) +q*omega_a[i] + F_D*sin(omega_D*time[i]))*delta_t
    theta_a[i+1] = theta_a[i] + omega_a[i+1] * delta_t
    if theta_a[i+1] < -pi:
        theta_a[i+1] = theta_a[i+1] + 2*pi
    if theta_a[i+1] > pi:
        theta_a[i+1] = theta_a[i+1] - 2*pi
plot(theta, omega,label='$F_D$ = ' +str(F_D))
plot(theta_a,omega_a,label='$F_D$ = ' +str(F_D))

#yscale('log')
#xlabel('Time (s)')
ylabel(r'$\omega$ (rad)')
xlabel(r'$\theta$ (rad)')
#xlim(initial_time,final_time)
savefig("test.jpg")
#ylim(-max(theta_0)*1.5,max(theta_0)*1.5)
legend()
show()
