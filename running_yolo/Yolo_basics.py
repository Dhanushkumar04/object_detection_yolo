from ultralytics import YOLO
import cv2

model = YOLO('../yoloweights/yolov8n.pt')
results= model("images/bikes.jpeg",show=True)
cv2.waitKey(0)