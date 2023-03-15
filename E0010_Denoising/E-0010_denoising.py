import cv2

# Load the grayscale medical image with Gaussian noise
image = cv2.imread('./data/e-0010_1.png', cv2.IMREAD_GRAYSCALE)

# Apply non-local means denoising algorithm
denoised_image = cv2.fastNlMeansDenoising(image, None, 10, 7, 21)

# Save the denoised image
cv2.imwrite('./data/e-0010_denoised_1.png', denoised_image)
