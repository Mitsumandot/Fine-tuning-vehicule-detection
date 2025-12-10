import torch
from ultralytics import YOLO

print(torch.cuda.is_available())

model = YOLO("yolov8n.pt")

model.train(
    data=r"C:\Users\ROG STRIX G17\Desktop\AIFINAL\vehicles-nighttime\dataset\data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)