import sys
import os

#adding path other directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../YOLO/yolo_custom/yolov5_3')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../database_creation/image_stitching')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../image_processing_testing/connecting_database')))

from final_detect_6 import apply_yolo
from framesextraction_and_imagestitching import create_panoramic_shelf_view
from database_connection import text_detection

# apply_yolo(source = /"Documents/automated_planogram_compliance-2/MASTER/video_1.mp4")

##ACTIVATE LATER
# create_panoramic_shelf_view(video_path = "MASTER/test_panorama.mp4", output_image_path = "MASTER/final_image.jpg", output_folder = "MASTER/frames")

# ##ACTIVATE LATER
coordinates = apply_yolo(source = "MASTER/updated.jpg")

##ACTIVATE LATER
# text_detection(folder_path = "MASTER/yolo_results/exp/crops/chips")


#creating planogram
