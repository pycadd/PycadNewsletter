import itk

# Load an image
input_image = itk.imread("input_image.nii.gz") # or input_image.nii

# Apply a filter
smoothed_image = itk.median_image_filter(input_image, redius=2) # More you incread the `redius` more the image will be smooth

#Save the result
itk.imwrite(smoothed_image, "output_image.nii.gz") # or output_image.nii