import os
import skimage
from skimage.transform import resize

import numpy as np
import matplotlib.pyplot as plt
import random 

path = "../data/custom_train_data/process"
path_save_test = "../data/custom_train_data/speckle_test"
names = os.listdir(path)

count = 0
percent = 0.1

for name in names :

    if count > 1 : 
        break

    path_img = os.path.join(path, name)
    path_save_img = os.path.join(path_save_test, name)

    img = skimage.io.imread(path_img)
    img = resize(img, (1024, 1024), anti_aliasing=True)
    noise_img = skimage.util.random_noise(img, mode='speckle', var=0.1)

    plt.imsave("./test.png", noise_img, cmap='gray')

    print(str(count)+"/"+str(len(names)))
    count+=1
