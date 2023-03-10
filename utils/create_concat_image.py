import json 
import cv2
import numpy as np
import os
import time

#create a fresque of all images

path = "../US_data/Autres"
file = open("../data.json")
data_total = json.load(file)
images_data = data_total["images"]

counter = 0
current_image = np.empty((1024, 0, 3), dtype=np.uint8)
for image_data in images_data:
    img_name = image_data["name"]
    img_path = os.path.join(path, img_name)
 
    img = cv2.imread(img_path, 1)
    img = cv2.resize(img, dsize=(1024, 1024), interpolation=cv2.INTER_CUBIC)

    current_image = np.concatenate((current_image, img), axis=1)

    counter +=1

cv2.imwrite("../final_image.png",  current_image)