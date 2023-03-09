import cv2
import os
import numpy as np 

path_base = "../data/personal_data/base"
path_speckle = "../data/personal_data/speckle"
images_path = os.listdir(path_base)

for image_path in images_path:
    img = cv2.imread(os.path.join(path_base, image_path),0)
    gauss = np.random.normal(0,1,img.size)
    gauss = gauss.reshape(img.shape[0],img.shape[1]).astype('uint8')
    noise = img + img * gauss

    

    cv2.imwrite(os.path.join(path_speckle, image_path), noise[:600, :600])