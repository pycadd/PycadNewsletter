from monai.transforms import Orientation
import nibabel as nib


orientation_changer = Orientation(axcodes='RAS') # LAS, LPS, RAI, LPI, RPS,...
image = nib.load('data/patient.nii.gz').get_fdata()
oriented_image = orientation_changer(image)