import json 
import cv2
import numpy as np
import os
import time

# Concatenate same image while size is under 1024/1024
# We do that because the neural network test need square image

path = "../US_data/Autres"
file = open("../data.json")
data_total = json.load(file)
images_data = data_total["images"]

for image_data in images_data:
    img_name = image_data["name"]
    img_path = os.path.join(path, img_name)
 
    img = cv2.imread(img_path, 1)
 
    while img.shape[1] < 1024:
        img = np.concatenate((img, img), axis=1)

    cv2.imwrite("../data/png_2/"+img_name,  img[:1024,:1024])