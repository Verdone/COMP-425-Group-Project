from ultralytics import YOLO

# Load a model
model = YOLO("yolov9c.pt")

# Customize validation settings
validation_results = model.val(
    data=r'.\425\container_2\data.yaml', 
    imgsz=640, batch=16, conf=0.25, iou=0.6, device="0",
    save_dir="./")
