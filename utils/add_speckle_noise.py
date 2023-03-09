import cv2
import os
import numpy as np 
import matplotlib.pyplot as plt

path_base = "../data/personal_data/base"
path_speckle = "../data/personal_data/speckle"
images_path = os.listdir(path_base)

for image_path in images_path:
    img = cv2.imread(os.path.join(path_base, image_path),0)

    # gauss = np.random.normal(0,1,img.size)
    # gauss = gauss.reshape(img.shape[0],img.shape[1],3).astype('uint8')
    # noise = img + img * gauss
    
    plt.imsave(os.path.join(path_speckle, image_path), img, cmap=plt.cm.copper)