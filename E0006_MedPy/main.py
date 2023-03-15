from medpy.io import load
import matplotlib.pyplot as plt

# Load the dicom file using MedPy
image_data, image_header = load('path/to/file.dcm')

# Normalize the image data to 0-1 range
image_array = (image_data - image_data.min()) / (image_data.max() - image_data.min())

# Display the image using matplotlib
plt.imshow(image_array, cmap='gray')
plt.show()