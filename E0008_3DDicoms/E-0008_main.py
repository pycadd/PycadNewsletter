import pydicom

dicom_file = pydicom.dcmread('path/to/dicom')
dicom_array = dicom_file.pixel_array
number_of_frames = dicom_file.NumberOfFrames

print('Shape:', dicom_array.shape)
print('Number of frames:', number_of_frames)