import json 
import numpy as np
import os
import time
from cmath import log10, sqrt

import cv2

import skimage
from skimage.transform import resize
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import mean_squared_error as mse
from skimage.color import gray2rgb
from skimage import img_as_ubyte

save_path = "../data/results/test/GAN"
path = os.path.join(save_path,"results")
path_noise = "../data/custom_train_data/speckle_test"
path_base ="../data/custom_train_data/process"
images_names = os.listdir(path_noise)

# Text settings
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 100)
fontScale = 2
color = (255, 0, 0)
thickness = 5

moy_psnr_noise = 0
moy_mse_noise = 0
moy_psnr_denoise = 0
moy_mse_denoise = 0

for img_name in images_names:
    img_path = os.path.join(path, img_name)
    img_noise_path = os.path.join(path_noise, img_name)
    img_base_path = os.path.join(path_base, img_name)

    img = skimage.io.imread(img_path)
    img = resize(img, (1024, 1024), anti_aliasing=True)

    if len(img.shape) == 2:
        img = gray2rgb(img)

    img_base = skimage.io.imread(img_base_path)    
    img_base =  resize(img_base, (1024, 1024), anti_aliasing=True)

    img_noise = skimage.io.imread(img_noise_path)    
    img_noise =  resize(img_noise, (1024, 1024), anti_aliasing=True)
    img_noise = img_noise[:,:,:3]

    psnr_noise = psnr(img_base, img_noise)
    psnr_denoise = psnr(img_base, img)

    mse_noise = mse(img_base, img_noise)
    mse_denoise = mse(img_base, img)

    moy_psnr_noise += psnr_noise
    moy_mse_noise += mse_noise
    moy_psnr_denoise+= psnr_denoise
    moy_mse_denoise+=mse_denoise

    # convert image skimage to cv
    img_base = img_as_ubyte(img_base)
    img_noise = img_as_ubyte(img_noise)
    img = img_as_ubyte(img)

    # write data to image
    text_noise = "PSNR : "+str(int(psnr_noise))+" MSE : "+"{:.4f}".format(mse_noise)
    text_denoise = "PSNR : "+str(int(psnr_denoise))+" MSE : "+"{:.4f}".format(mse_denoise)
    cv2.putText(img_noise, text_noise, org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.putText(img, text_denoise, org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)

    compare_image = np.concatenate((img_base, img_noise, img), axis =1)

   
    cv2.imwrite(os.path.join(os.path.join(save_path,"final"), img_name), img)
    cv2.imwrite(os.path.join(os.path.join(save_path,"compare"), img_name), compare_image)

s = len(images_names)
print("moy_psnr_denoise",str(moy_psnr_denoise/s))
print("moy_mse_denoise",str(moy_mse_denoise/s))