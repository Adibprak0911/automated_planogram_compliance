import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

def list_image_files(folder_path):
    image_extensions = {'.jpg'}
    
    image_files = []

    for file_name in os.listdir(folder_path):
        if os.path.splitext(file_name)[1].lower() in image_extensions:
            image_files.append(file_name)
    
    return image_files

folder_path = 'image_processing_testing/text_detection/identify_all_bounding/images'

image_files = list_image_files(folder_path)
print(image_files)
print(len(image_files))


top_left = []
bottom_right = []
text = []

if not image_files:
    print("no image files in the folder")

else:
    for i in range(0,len(image_files)):
        image = folder_path +'/' + image_files[i]
        reader = easyocr.Reader(['en'], gpu = False)
        result = reader.readtext(image)

        if result:
            top_left.append(tuple(result[0][0][0]))
            bottom_right.append(tuple(result[0][0][2]))
            text.append(result[0][1])

            img = cv2.imread(image)
            img = cv2.rectangle(img, top_left[i], bottom_right[i], (255, 0, 0), 5)
            
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()
            print(result)
            
        else: 
            print(f"No text detected in image {image_files[i]}")
            top_left.append(None)
            bottom_right.append(None)
            text.append(None)

plt.show()