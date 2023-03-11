import os
import skimage
from skimage.transform import resize

import numpy as np
import matplotlib.pyplot as plt
import random 

path = "../data/custom_train_data/process"
path_save_train = "../data/custom_train_data/train"
path_save_test = "../data/custom_train_data/test"
names = os.listdir(path)

count = 0
percent = 0.1

for name in names :
    path_img = os.path.join(path, name)
    
    path_save_img = os.path.join(path_save_test, name)

    if(random.random() > percent):
       path_save_img = os.path.join(path_save_train, name)

    img = skimage.io.imread(path_img)
    img = resize(img, (1024, 1024), anti_aliasing=True)
    
    noise_img = skimage.util.random_noise(img, mode='speckle', var=0.02)
    save_img = np.concatenate((noise_img, img), axis=1)
    plt.imsave(path_save_img, save_img, cmap='gray')


    print(str(count)+"/"+str(len(names)))
    count+=1

