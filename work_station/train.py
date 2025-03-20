from ultralytics import YOLO
import torch
import os



model = YOLO("yolov9c.pt")
#torch.cuda.empty_cache()

# dir = os.getcwd()
# data_path=os.path.join(dir,"container_2","data.yaml")
data_path=r".\425\container_2\data.yaml"

data_path
train_results=model.train(
    data=data_path,
    epochs=50,
    device=0,
    batch=-1,
    save_period=4,
    resume=True
)
print("Complete",train_results)
