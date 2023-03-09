import os
import cv2
import json
import numpy as np


# We create a json file how save all images datas
# We do that to keep the base shape image, so we can recover the base image from concatenate one

path = "../US_data/Autres"

data_total = {"images" :[], "total_size":0}

total_size = 0
images = os.listdir(path)
images.sort()

for image in images:
    img_path = os.path.join(path, image)
    img = cv2.imread(img_path,1)

    if(img.shape[0] == 2048):
        img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)), interpolation = cv2.INTER_LINEAR)
        cv2.imwrite(img_path, img)

    data = {"name":image, "size":img.shape}
    data_total["images"].append(data)
    total_size += 1024

data_total["total_size"] = total_size

with open('../data.json', 'w') as fp:
    json.dump(data_total, fp)


