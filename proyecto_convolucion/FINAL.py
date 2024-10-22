import numpy as np
import matplotlib.pyplot as plt

def gaussian_blur(x, y, sigma=25):
    return np.exp(-(x**2 + y**2) / (2 * sigma**2))

# Load the blurred image from file
blur_array = np.loadtxt('blur.txt')

# Create the Gaussian filter (without centering it in the image)
height, width = blur_array.shape
x, y = np.meshgrid(np.arange(0, width), np.arange(0, height))
x = np.minimum(x, width - x)  # Symmetry for Gaussian filter
y = np.minimum(y, height - y)  # Symmetry for Gaussian filter
gaussian_filter = gaussian_blur(x, y)

# Transform both arrays to Fourier domain
blur_array_transformed = np.fft.fft2(blur_array)
gaussian_filter_transformed = np.fft.fft2(gaussian_filter, s=blur_array.shape)

# Avoid division by zero or small numbers by adding a small epsilon
epsilon = 1e-3
unblured_coeffs = blur_array_transformed / (gaussian_filter_transformed + epsilon)

# Inverse Fourier transform to obtain the unblurred image
unblured_array = np.fft.ifft2(unblured_coeffs).real

# Create subplots for better formatting
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

