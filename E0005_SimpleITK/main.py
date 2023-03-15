import SimpleITK as sitk
import matplotlib.pyplot as plt

# Load the image using SimpleITK
image = sitk.ReadImage('path/to/file.dcm')

# Get the image array data
image_array = sitk.GetArrayFromImage(image)

# Normalize the image data to 0-1 range
image_array = (image_array - image_array.min()) / (image_array.max() - image_array.min())

# Display the image using matplotlib
plt.imshow(image_array[0], cmap='gray')
plt.show()