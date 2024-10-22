#Ricardo Rodriguez Pineda 169048
#Jose Emilio Pacheco Cuan 172211
#Andrés Alvarez Rodriguez 170060
import numpy as np
import matplotlib.pyplot as plt
def gaussian_blur(x,y):
    return np.exp(-(x**2 + y**2)/(2*25**2))


#-------create and plot array from file 'blur.txt'----#
blur_array = np.loadtxt('blur.txt')
plt.imshow(blur_array)
plt.show()
#------create and plot array from gaussian_blur------#
gaussian_filter = np.empty_like(blur_array,dtype = float)
width = len(blur_array[0])
height = len(blur_array)
n = width//2
m = height//2
for i in range(-n,n):
    for j in range(-m,m):
        gaussian_filter[i,j] = gaussian_blur(i,j)
plt.imshow(gaussian_filter)
plt.show()
#------------transform both arrays to get fourier coeffs for each array----------#
blur_array_transformed = np.fft.rfft2(blur_array)
gaussian_filter_transformed = np.fft.rfft2(gaussian_filter)
#--------divide coefficients to get the coeffs of the unblured image------------#
unblured_coeffs = np.empty_like(blur_array_transformed)
for i in range(-n,n):
    for j in range(-m,m):
        unblured_coeffs[i,j] = blur_array_transformed[i,j]/((width*height)*gaussian_filter_transformed[i,j])

#------inverse fourier transform to get array of unblured image---#
unblured_array = np.fft.irfft2(unblured_coeffs)
#------plot of unblured_array-------#
plt.imshow(unblured_array)
plt.show()
