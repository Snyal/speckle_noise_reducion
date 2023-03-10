import cv2
import os
import numpy as np 
import matplotlib.pyplot as plt
import skimage

path_base = "../data/personal_data/color"
path_speckle = "../data/personal_data/speckle"
images_path = os.listdir(path_base)

for image_path in images_path:
    img = cv2.imread(os.path.join(path_base, image_path),0)
    img = skimage.util.random_noise(img, mode='speckle', var=.1)

    
    plt.imsave(os.path.join(path_speckle, image_path), img[:300,:300], cmap=plt.cm.copper)