from os.path import dirname, join as pjoin
import scipy.io as sio
import cv2

#convert .mat image to .png image

mat_fname = '../US_data/humankidney/data_simu3.mat'
mat_contents = sio.loadmat(mat_fname)

array = mat_contents["refl"]
cv2.imwrite("2.png", array)