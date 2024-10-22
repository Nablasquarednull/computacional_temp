#Ricardo Rodriguez Pineda 169048
#Jose Emilio Pacheco Cuan 172211
#Andrés Alvarez Rodriguez 170060
import numpy as np
import matplotlib.pyplot as plt
def gaussian_blur(x,y,sigma = 25):
    return np.exp(-(x**2 + y**2) / (2 * sigma**2))


#-------create and plot array from file 'blur.txt'----#
blur_array = np.loadtxt('blur.txt')
plt.imshow(blur_array, cmap='gray')
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
plt.imshow(gaussian_filter, cmap='gray')
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
plt.imshow(unblured_array, cmap='gray')
plt.show()
#------EXTRA: NOW WE PLOT ALL THREE TOGETHER IN A NICER FORMAT-----#
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot the blurred image
axs[0].imshow(blur_array, cmap='gray')
axs[0].set_title("Blurred Image")
axs[0].axis('off')

# Plot the Gaussian filter
axs[1].imshow(gaussian_filter, cmap='gray')
axs[1].set_title("Gaussian Filter")
axs[1].axis('off')

# Plot the unblurred image
axs[2].imshow(unblured_array, cmap='gray')
axs[2].set_title("Unblurred Image")
axs[2].axis('off')

# Adjust layout to ensure titles fit properly
plt.tight_layout()
plt.show()

"""PART D:
The limit to completely deblur an image depends on the coefficients of the DFT of the smearing distrbution. Since these coeffs might be zero, we then have to circumvent the issue somehow, either by introducing noise (as we did in this code with the "epsilon" variable, or by leaving the original coeff untouched (which in the end is also noise). That's why we cannot perfectly unblur an image."""
