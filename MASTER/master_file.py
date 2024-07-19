import sys
import os
import csv
import cv2
from PIL import Image 

def csv_to_list(file_path):
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            
            # Assuming there's only one row and it contains the values separated by commas
            for row in csv_reader:
                # Convert the row to a list of strings
                data_list = row
                break  # Stop after the first row
                
            return data_list
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def calculate_subset_percentage(list1, list2):
    # Convert lists to sets for efficient comparison
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the intersection of both sets
    intersection = set1.intersection(set2)
    
    # Find the elements in list1 that are not in list2
    missing_elements = set1 - set2

    # Calculate the percentage of list1 elements that are in list2
    if len(set1) == 0:
        return 0.0  # Avoid division by zero
    percentage = (len(intersection) / len(set1)) * 100
    
    return percentage, missing_elements
        
#adding path other directory

##ACTIVATE LATER
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../YOLO')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../database_creation/image_stitching')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../image_processing_testing/connecting_database')))

from final_detect_10 import apply_yolo
from framesextraction_and_imagestitching import create_panoramic_shelf_view
from database_connection import text_detection

# apply_yolo(source = /"Documents/automated_planogram_compliance-2/MASTER/video_1.mp4")

##ACTIVATE LATER
# create_panoramic_shelf_view(video_path = "MASTER/test_panorama.mp4", output_image_path = "MASTER/final_image.jpg", output_folder = "MASTER/frames")

# ##ACTIVATE LATER
apply_yolo(source = "MASTER/updated.jpg")

##ACTIVATE LATER
text_detection(folder_path = "MASTER/yolo_results/exp/crops/chips")

#planogram compliance
folder_path = "MASTER/yolo_results/exp/crops/chips"
product_list = [f[:6] for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


file_path = "MASTER/company_requirement.csv"  # Replace with your CSV file path
data_list = csv_to_list(file_path)      
print(data_list)

percentage, missing_elements = calculate_subset_percentage(product_list, data_list)
print("percentage accuracy = ", percentage)
print("missing elements = ", missing_elements)

missing_elements = list(missing_elements)

for i in missing_elements:
    file_name = i + ".jpg"
    img = Image.open("MASTER/yolo_results/exp/crops/chips/"+file_name)
    img.show()
    