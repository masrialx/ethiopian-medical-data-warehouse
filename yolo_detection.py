import torch
import cv2
import os
from pathlib import Path

# Load YOLO model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

# Input and output paths
input_folder = "images/"  # Folder with images
output_folder = "detections/"

os.makedirs(output_folder, exist_ok=True)

# Process images
for image_path in Path(input_folder).glob("*.jpg"):
    img = cv2.imread(str(image_path))
    results = model(img)  # Run YOLOv5

    # Save detection results
    results.save(output_folder)
    print(f"Processed {image_path}")
