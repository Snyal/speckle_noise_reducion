import json 
import cv2
import numpy as np
import os

save_path = "../data/results/DPIR"
path = os.path.join(save_path,"results")
path_base = "../US_data/Autres"
file = open("../data.json")
data_total = json.load(file)
images_data = data_total["images"]

for image_data in images_data:
    img_name = image_data["name"]
    img_path = os.path.join(path, img_name)
    img_base_path = os.path.join(path_base, img_name)
    img_size = image_data["size"]

    img = cv2.imread(img_path, 1)
    img = cv2.resize(img, dsize=(1024, 1024), interpolation=cv2.INTER_CUBIC)

    print(img.shape)
    img_base = cv2.imread(img_base_path, 1)
    
    new_image = img[:img_size[0], :img_size[1]]
    compare_image = np.concatenate((img_base, new_image), axis =1)

    cv2.imwrite(os.path.join(os.path.join(save_path,"final"), img_name), new_image)
    cv2.imwrite(os.path.join(os.path.join(save_path,"compare"), img_name), compare_image)
