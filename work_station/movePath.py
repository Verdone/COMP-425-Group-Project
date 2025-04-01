import os
curdir=os.path.abspath(os.getcwd())

cenparmi_ocr_dataset="cenparmi_ocr_dataset"



full_path_armi_ocr_dataset=curdir + "\\" + cenparmi_ocr_dataset


print ([name for name in os.listdir(".\\"+cenparmi_ocr_dataset) if os.path.isdir(name)])
os.listdir(".\\"+cenparmi_ocr_dataset)
os.path.isdir


import shutil

for each in os.listdir(full_path_armi_ocr_dataset):
    path = full_path_armi_ocr_dataset + '\\' + each + "\\"
    each = ["test\\label","train\\"]

full_path_armi_ocr_dataset
os.listdir(r"C:\Users\MV\Downloads\425\cenparmi_ocr_dataset\QC\train")
path = r"C:\Users\MV\Downloads\425\cenparmi_ocr_dataset\QC\train"
os.makedirs(path+"\\images")
os.makedirs(path+"\\labels")
for file in os.listdir(path):
    file_dir=path+"\\"+file
    
    if os.path.isfile(path+"\\images\\"+file):continue
    if os.path.isfile(path+"\\labels\\"+file):continue
    if file.endswith(".jpg"):
        
        os.rename(file_dir,path+"\\images\\"+file)
    elif file.endswith(".txt"):
        os.rename(file_dir,path+"\\labels\\"+file)

file.endswith(".jpg")
print(path+"\\images\\"+file)
file_dir=path+"\\"+file
path
path+"\\images\\"+file

shutil.move(file_dir,path+"\\images\\"+file)

for i in range(10):
    print(str(i)+": "+str(i))


for i in range(26):
    c=chr(ord('A')+i)
    print(str(ord(c)-55)+":"+c)
ord('A')- 55