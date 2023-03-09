import cv2

img_path = "../final_image.png"
data_dir_path = "../data/"

img = cv2.imread(img_path, 1)
total_sub_image = img.shape[1]//1024

for i in range(total_sub_image):
    img_generated = img[:,i*1024:(i+1)*1024]
    cv2.imwrite("../data/"+str(i)+".png", img_generated)

# make the last
img_generated = img[:,(total_sub_image)*1024:img.shape[1]]
cv2.imwrite("../data/png/"+str(total_sub_image)+".png", img_generated)

