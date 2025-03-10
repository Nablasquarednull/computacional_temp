#Andres Alvarez rodriguez
from random import random,randrange
from matplotlib.pyplot import plot, show, scatter
from numpy import fft,empty, sort, flip, arange, loadtxt, savetxt, sqrt, log, cos, sin, pi,empty_like,zeros,where
#PARTE_1------------------------
rate = 44100 #samples/second
#---------load of text files-----------
piano = loadtxt('piano.txt')
trumpet = loadtxt('trumpet.txt')
#---------plotting the files-----------
plot(piano,color = 'green')
show()
plot(trumpet, color = 'orange')
show()
#---------calcultating the fourier coefficients-----------
piano_coeffs = fft.rfft(piano)
trumpet_coeffs = fft.rfft(trumpet)
#---------Making the arrays with only 10,000 coefficients and filling them-----------
magnitude_piano_coeffs = zeros(10000,float) 
magnitude_trumpet_coeffs = zeros(10000,float) 
for i in range(10000):
    magnitude_piano_coeffs[i] = abs(piano_coeffs[i]) 
    magnitude_trumpet_coeffs[i] = abs(trumpet_coeffs[i]) 
#---------Plotting the arrays with only 10,000 coefficients-----------
plot(magnitude_piano_coeffs,color = 'green')
show()
plot(magnitude_trumpet_coeffs,color = 'orange')
show()
#---------finding the coefficient with greatest contribution, and finding the respective frecuency-----------
max_coeff_piano = max(magnitude_piano_coeffs)
max_coeff_trumpet = max(magnitude_trumpet_coeffs)
max_k_piano = where (magnitude_piano_coeffs == max_coeff_piano)
max_k_trumpet = where (magnitude_trumpet_coeffs == max_coeff_trumpet)
print("The corresponding frecuency maximum coeffs of the piano and trumpet are : ", max_k_piano[0], " and ", max_k_trumpet[0], "that means they both are playing the note: re")




#PARTE_2-----------------------
#---------defining our arrays to hold our random numbers
points = 1000
x_array = empty(points,float)
y_array = empty(points,float)
#----------defining our transformation function--------------
def gaussian_random(z,sigma):
    return (sqrt(-2*sigma**2*log(1-z)))
#-----------coordinate changes----------
def polar_to_x(r,theta):
    return r*cos(theta)
def polar_to_y(r,theta):
    return r*sin(theta)
#-----------for loop to fill the arrays and plotting--------------
for i in range(points):
    z = random()
    theta = random()*2*pi
    r_x = gaussian_random(z,30)
    r_y = gaussian_random(z,10)
    x_array[i] = polar_to_y(r_x,theta)
    y_array[i] = polar_to_x(r_y,theta)
scatter(x_array,y_array,color = 'purple')
show()
