import cv2

# Load the grayscale medical image with Gaussian noise
image = cv2.imread('./E0010_Denoising/data/noisy_image.png', cv2.IMREAD_GRAYSCALE)

# Apply non-local means denoising algorithm
denoised_image = cv2.fastNlMeansDenoising(image, None, 10, 7, 21)

# Save the denoised image
cv2.imwrite('./E0010_Denoising/data/denoised_image.png', denoised_image)
