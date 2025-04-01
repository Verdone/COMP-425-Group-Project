import os
import cv2

# Paths to your input (color) and output (grayscale) folders
input_folder = r"C:\Users\MV\Downloads\425\cenparmi_ocr_dataset_1\cenparmi_ocr_dataset\QC\train"
output_folder = r"C:\Users\MV\Downloads\425\cenparmi_ocr_dataset_1\cenparmi_ocr_dataset\QC\train"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define acceptable image extensions
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}

# Loop through each file in the input_folder
for filename in os.listdir(input_folder):
    # Check file extension to ensure it's an image
    ext = os.path.splitext(filename)[1].lower()
    if ext in image_extensions:
        # Construct full file path
        color_image_path = os.path.join(input_folder, filename)

        # Read the image in color
        color_image = cv2.imread(color_image_path, cv2.IMREAD_COLOR)
        if color_image is None:
            print(f"Warning: Unable to read {color_image_path}. Skipping.")
            continue
        
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

        # Construct output file path
        gray_image_path = os.path.join(output_folder, filename)

        # Save the grayscale image
        cv2.imwrite(gray_image_path, gray_image)
        print(f"Converted {filename} to grayscale and saved to {gray_image_path}")