#Emmanuel Ivan montiel paredes 
#Paola Blumenkron Guerrero 
#Juan Carlos usagiaba orozco
import numpy as np
import matplotlib.pyplot as plt


#-------crear arreglos y plotear----#
blur_array = np.loadtxt('blur.txt')
plt.imshow(blur_array)
plt.show()


def gauss(x,y):
    return np.exp(-(x**2 + y**2) / (2 * 25**2))

#------crear los arreglos de largo y ancho y plotear el filtro gaussiano------#
gaussian_filter = np.empty_like(blur_array,dtype = float)
width = len(blur_array[0])
height = len(blur_array)
n = width//2
m = height//2
for i in range(-n,n):
    for j in range(-m,m):
        gaussian_filter[i,j] = gauss(i,j)
plt.imshow(gaussian_filter)
plt.show()
#------------transform both arrays to get fourier coeffs for each array----------#
blur_array_transformed = np.fft.rfft2(blur_array)
gaussian_filter_transformed = np.fft.rfft2(gaussian_filter)
#--------divide coefficients to get the coeffs of the unblured image| TRICK: ADD A SMALL EPSILON TO AVOID DIVIDING BY 0------------#
epsilon = 1e-3
unblured_coeffs = blur_array_transformed / (gaussian_filter_transformed + epsilon) #IMPORTANT NOTE! NUMPY CAN DO ARRAY DIVISION WITHOUT HAVING TO DO THEM ONE BY ONE!
#------inverse fourier transform to get array of unblured image---#
unblured_array = np.fft.irfft2(unblured_coeffs)
#------plot of unblured_array-------#
plt.imshow(unblured_array)
plt.show()
"""PART D:
The limit to completely deblur an image depends on the coefficients of the DFT of the smearing distrbution. Since these coeffs might be zero, we then have to circumvent the issue somehow, either by introducing noise (as we did in this code with the "epsilon" variable, or by leaving the original coeff untouched (which in the end is also noise). That's why we cannot perfectly unblur an image."""
