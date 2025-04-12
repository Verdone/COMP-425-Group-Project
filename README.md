# About

License plate detection and recognition remain challenging due to their accuracy being impacted by diverse lighting conditions, obstructions, and regional plate variations. Addressing these issues has direct benefits towards plate detection's applications in traffic management, parking detection, and even for charging tolls when crossing through points of interest.

We seek to tackle the ongoing challenge of detecting license plates by implementing a two-step pipeline;
First, a YOLOv9 model is used to find and isolate license plates from images provided from custom datasets made of images that contain license plates from several regions.
Second, an EasyOCR model is used to read these license plates by employing an optimized character recognition algorithm.

Our paper discusses the detailed process of developing and implementing these models, followed by a discussion of the results and inferred findings from
training and testing this two-phase algorithm on the aforementioned datasets.

## Team Members

| Name             | Student ID | Email                      | Program                     |
| ---------------- | ---------- | -------------------------- | --------------------------- |
| Philippe Lizotte | 40261140   | p_lizot@live.concordia.ca  | Year 3 COMP (Undergraduate) |
| Marmik Patel     | 40201462   | p_marmik@live.concordia.ca | Year 3 COMP (Undergraduate) |
| Phuc Thien Tran  | 40017354   | phucthientran@gmail.com    | Year 3 COMP (Undergraduate) |
| Giuliano Verdone | 40252190   | g_verdon@live.concordia.ca | Year 3 SOEN (Undergraduate) |

## Model weights

For the data on model weights, please see the Google Drive link [available here](https://drive.google.com/file/d/103jRrNEmkUrTI-o3bK-xRuL1YJW_rBjK/view?usp=sharing​).

## YOLOv9-c model paired with EasyOCR

To view the source code for the YOLO OCR model, see the Google Drive link [available here](https://drive.google.com/file/d/1-U6rhLxYVgWVjGZ3MGcMZ3wv8I9R4YrU/view?usp=drive_link).

## Research Paper

The final draft of this project's report will be uploaded to the repostiory. The draft is currently under review by the project's lab demonstrator.

## Running the Code

Before running the code, make sure to:

1. Organize your dataset as follows:

   ```
   ├── data/
   │   ├── images/
   │   └── labels/
   ```

2. Update the paths in your training and inference scripts to point to your dataset location. Don't forget to configure the .YAML file as well.

3. Verify that the label files are in the correct YOLO format.

If you're using your own GPU, make sure you have the correct dependencies installed on your machine (e.g. CUDA for NVIDIA.)

---

## Running the Model

Once paths are correctly set up and pytorch is installed, run the following train, detection, and validation scripts.

# Acknowledgement

The authors wish to acknowledge Dr. Yaser Esmaeili Salehani and Zahra Ebrahimi from Concordia University’s Department of Computer Science and Software Engineering (CSSE) for their guidance throughout this research project. It was conducted as a part of coursework from COMP 425/6341 - Computer Vision, for the Winter 2025 semester.
