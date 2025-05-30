# import easyocr
# import cv2
# from matplotlib import pyplot as plt
# import numpy as np
# import os

# def list_image_files(folder_path):
#     image_extensions = {'.jpg'}
    
#     image_files = []

#     for file_name in os.listdir(folder_path):
#         if os.path.splitext(file_name)[1].lower() in image_extensions:
#             image_files.append(file_name)
    
#     return image_files

# folder_path = 'image_processing_testing/text_detection/identify_all_bounding/images'

# image_files = list_image_files(folder_path)
# print(image_files)
# print(len(image_files))

# top_left = []
# bottom_right = []
# text = []

# if not image_files:
#     print("No image files in the folder")
# else:
#     for i in range(len(image_files)):
#         image = folder_path + '/' + image_files[i]
#         reader = easyocr.Reader(['en'], gpu=False)
#         result = reader.readtext(image)
#         print(len(result))

#         img = cv2.imread(image)  # Read the image once outside the inner loop

#         if result:
#             for res in result:
#                 tl = tuple(map(int, res[0][0]))  # Ensure the coordinates are tuples of integers
#                 br = tuple(map(int, res[0][2]))  # Ensure the coordinates are tuples of integers

#                 top_left.append(tl)
#                 bottom_right.append(br)
#                 text.append(res[1])

#                 # Draw rectangle for each detected text
#                 img = cv2.rectangle(img, top_left[-1], bottom_right[-1], (255, 0, 0), 5)
#                 print(res)

#         else:
#             print(f"No text detected in image {image_files[i]}")
#             top_left.append(None)
#             bottom_right.append(None)
#             text.append(None)

#         # Display the image with all bounding boxes
#         plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#         plt.axis('off')
#         plt.show()


# import easyocr
# import cv2
# from matplotlib import pyplot as plt
# import numpy as np
# import os

# def list_image_files(folder_path):
#     image_extensions = {'.jpg'}
#     image_files = []

#     for file_name in os.listdir(folder_path):
#         if os.path.splitext(file_name)[1].lower() in image_extensions:
#             image_files.append(file_name)
    
#     return image_files

# folder_path = 'image_processing_testing/text_detection/identify_all_bounding/images'

# image_files = list_image_files(folder_path)
# print(image_files)
# print(len(image_files))

# top_left = []
# bottom_right = []
# text = []

# if not image_files:
#     print("No image files in the folder")
# else:
#     for i in range(len(image_files)):
#         image = folder_path + '/' + image_files[i]
#         reader = easyocr.Reader(['en'], gpu=False)
#         result = reader.readtext(image)
#         print(len(result))

#         img = cv2.imread(image)  # Read the image once outside the inner loop

#         if result:
#             for res in result:
#                 # Extract the four corners of the bounding box
#                 top_left_corner = tuple(map(int, res[0][0]))
#                 top_right_corner = tuple(map(int, res[0][1]))
#                 bottom_right_corner = tuple(map(int, res[0][2]))
#                 bottom_left_corner = tuple(map(int, res[0][3]))

#                 top_left.append(top_left_corner)
#                 bottom_right.append(bottom_right_corner)
#                 text.append(res[1])

#                 # Draw polygon for each detected text
#                 pts = np.array([top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner], np.int32)
#                 pts = pts.reshape((-1, 1, 2))
#                 img = cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 0), thickness=5)
#                 print(res)

#         else:
#             print(f"No text detected in image {image_files[i]}")
#             top_left.append(None)
#             bottom_right.append(None)
#             text.append(None)

#         # Display the image with all bounding boxes
#         plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#         plt.axis('off')
#         plt.show()


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

if not image_files:
    print("No image files in the folder")
else:
    for i in range(len(image_files)):
        image = folder_path + '/' + image_files[i]
        reader = easyocr.Reader(['en'], gpu=True)
        result = reader.readtext(image)
        print(len(result))

        img = cv2.imread(image)  # Read the image once outside the inner loop

        if result:
            # Find the largest text bounding box
            largest_box = None
            max_area = 0
            largest_text = ""

            for res in result:
                # Extract the four corners of the bounding box
                top_left_corner = tuple(map(int, res[0][0]))
                top_right_corner = tuple(map(int, res[0][1]))
                bottom_right_corner = tuple(map(int, res[0][2]))
                bottom_left_corner = tuple(map(int, res[0][3]))

                # Calculate the area of the bounding box
                width = np.linalg.norm(np.array(top_right_corner) - np.array(top_left_corner))
                height = np.linalg.norm(np.array(top_left_corner) - np.array(bottom_left_corner))
                area = width * height

                if area > max_area:
                    max_area = area
                    largest_box = [top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner]
                    largest_text = res[1]

            if largest_box:
                # Draw polygon for the largest detected text
                pts = np.array(largest_box, np.int32)
                pts = pts.reshape((-1, 1, 2))
                img = cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 0), thickness=5)

                # Write the text just above the bounding box
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 100
                font_thickness = 10 
                text_size = cv2.getTextSize(largest_text, font, font_scale, font_thickness)[0]
                text_x = largest_box[0][0]
                text_y = largest_box[0][1] - 10
                cv2.putText(img, largest_text, (text_x, text_y), font, font_scale, (255, 0, 0), font_thickness)

                print(largest_text)

        else:
            print(f"No text detected in image {image_files[i]}")

        # Display the image with the bounding box and text
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()
