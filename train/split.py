import cv2 as cv
import os
class_id = 2 


with open('gt10913.txt', "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        parts = line.split()

        img_number = int(parts[0])
        img_path = f"data/img_{img_number}.jpg"
        img = cv.imread(img_path)
        if img is None:
            img_path = f"data/img_0{img_number}.jpg"
            img = cv.imread(img_path)
            img_number = f"0{img_number}"
            if img is None:
                print(img_number)
                continue
        
        height, width = img.shape[:2]

        vehicule_count = int(parts[1])

        boxes = parts[2:]

        yolo_lines = []

        for i in range(0, len(boxes), 4):
            
            box = boxes[i:i+4]
            box = [int(i) for i in box]

            x, y, w, h = box

            x_center = (x + w/2)/width
            y_center = (y + h/2)/height

            w = w / width
            h = h / height

            yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")

        with open(os.path.join("dataset/labels/train", f"{img_number}.txt"), "w") as out:
            out.write("\n".join(yolo_lines))





        

