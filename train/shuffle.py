import random
import shutil
import cv2 as cv

number_of_samples = 10913

x = range(number_of_samples)
x = list(x)
random.shuffle(x)
print(len(x))

train_size = 8729

for i in range(train_size):
    img_number = x[i]
    img_path = f"data/img_{img_number}.jpg"
    img = cv.imread(img_path)
    if img is None:
        img_path = f"data/img_0{img_number}.jpg"
        img = cv.imread(img_path)
        img_number = f"0{img_number}"
        if img is None:
            continue
    
    label_path = f"datalabel/img_{img_number}.txt"

    img_destination = f"dataset/images/train/img_{img_number}.jpg"

    label_destination = f"dataset/labels/train/img_{img_number}.txt"

    shutil.move(img_path, img_destination)

    shutil.move(label_path, label_destination)

