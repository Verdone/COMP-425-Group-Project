from ultralytics import YOLO

# Load a model
model = YOLO("yolov9c.pt")  # pretrained YOLO model

# Run batched inference on a list of images
result = model([r"C:\Users\MV\Downloads\425\container_2\valid\images\00b6f96c840767fa_jpg.rf.d4ce4a053ac575abc9cf11c4092a3a97.jpg"])  # return a list of Results objects


result=result[0]
boxes = result.boxes  # Boxes object for bounding box outputs
masks = result.masks  # Masks object for segmentation masks outputs
keypoints = result.keypoints  # Keypoints object for pose outputs
probs = result.probs  # Probs object for classification outputs
obb = result.obb  # Oriented boxes object for OBB outputs
result.show()  # display to screen
result.save(filename="result.jpg")  # save to disk