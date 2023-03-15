import numpy as np
from skimage import io, metrics

# Load the original noisy image and the denoised image
noisy_image = io.imread('./data/e-0010.png', as_gray=True)
denoised_image = io.imread('./data/e-0010_denoised.png', as_gray=True)

# Calculate PSNR and SSIM
psnr = metrics.peak_signal_noise_ratio(noisy_image, denoised_image)
ssim = metrics.structural_similarity(noisy_image, denoised_image)

print('PSNR:', psnr)
print('SSIM:', ssim)
