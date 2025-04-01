import os
import shutil
import random

# --- Configuration ---
# Path to your single folder containing both images and labels
input_folder = r"C:\Users\MV\Downloads\425\cenparmi_ocr_dataset\NY\test"

# Path to the output directory where the new folders will be created
output_base = r'C:\Users\MV\Downloads\425\ocr_container_colored'

# Split ratios (train, val, test). Must sum to 1.0
train_ratio = 0.0
val_ratio   = 0.5
test_ratio  = 0.5

# List of image extensions you expect to handle
image_extensions = [".jpg", ".jpeg", ".png"]  

# Make results reproducible (optional)
random.seed(42)

# --- Create the necessary output folders ---
train_images_dir = os.path.join(output_base, "train", "images")
train_labels_dir = os.path.join(output_base, "train", "labels")

val_images_dir   = os.path.join(output_base, "val",   "images")
val_labels_dir   = os.path.join(output_base, "val",   "labels")

test_images_dir  = os.path.join(output_base, "test",  "images")
test_labels_dir  = os.path.join(output_base, "test",  "labels")

os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir,   exist_ok=True)
os.makedirs(val_labels_dir,   exist_ok=True)
os.makedirs(test_images_dir,  exist_ok=True)
os.makedirs(test_labels_dir,  exist_ok=True)

# --- Collect only image filenames from the input folder ---
all_files = os.listdir(input_folder)
all_image_files = []
for f in all_files:
    ext = os.path.splitext(f)[1].lower()
    if ext in image_extensions:
        all_image_files.append(f)

# Shuffle the file list for random splitting
random.shuffle(all_image_files)

# --- Split the files ---
for image_file in all_image_files:
    # Derive label filename from image filename
    base_name, _ = os.path.splitext(image_file)
    label_file = base_name + ".txt"

    # Full paths for the original files
    image_path = os.path.join(input_folder, image_file)
    label_path = os.path.join(input_folder, label_file)

    # If there's no corresponding label file, skip
    if not os.path.isfile(label_path):
        print(f"Warning: No label found for image {image_file}, skipping.")
        continue

    # Decide which subset this file goes to based on random draw
    r = random.random()
    if r < train_ratio:
        subset_images_dir = train_images_dir
        subset_labels_dir = train_labels_dir
    elif r < train_ratio + val_ratio:
        subset_images_dir = val_images_dir
        subset_labels_dir = val_labels_dir
    else:
        subset_images_dir = test_images_dir
        subset_labels_dir = test_labels_dir

    # Copy image and label files to the appropriate subset
    shutil.copy2(image_path, os.path.join(subset_images_dir, image_file))
    shutil.copy2(label_path, os.path.join(subset_labels_dir, label_file))

print("Splitting complete!")
print(f"Train images/labels in: {os.path.join(output_base, 'train')}")
print(f"Val images/labels in:   {os.path.join(output_base, 'val')}")
print(f"Test images/labels in:  {os.path.join(output_base, 'test')}")
