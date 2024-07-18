# import easyocr
# import cv2
# from matplotlib import pyplot as plt
# import numpy as np
# import os
# import itertools
# import database_interaction
# import predict
# from itertools import permutations

# def list_image_files(folder_path):
#     image_extensions = {'.jpg'}
#     image_files = []

#     for file_name in os.listdir(folder_path):
#         if os.path.splitext(file_name)[1].lower() in image_extensions:
#             image_files.append(file_name)
    
#     return image_files

# def generate_two_combinations(items):
#     return [' '.join(p) for p in permutations(items, 2)]


# def text_detection(folder_path):

#     image_files = list_image_files(folder_path)

#     if not image_files:
#         print("No image files in the folder")
#     else:
#         for i in range(len(image_files)):
#             image = folder_path + '/' + image_files[i]
#             reader = easyocr.Reader(['en'], gpu=True)
#             result = list(reader.readtext(image))
            
#             text_only = list()
#             for j in range(0, len(result)):
#                 text_only.append(result[j][1].lower())

#             img = cv2.imread(image)  # Read the image once outside the inner loop

#             if result:
#                 # Find the largest text bounding box
#                 largest_box = None
#                 max_area = 0
#                 largest_text = ""

#                 for res in result:
#                     # Extract the four corners of the bounding box
#                     top_left_corner = tuple(map(int, res[0][0]))
#                     top_right_corner = tuple(map(int, res[0][1]))
#                     bottom_right_corner = tuple(map(int, res[0][2]))
#                     bottom_left_corner = tuple(map(int, res[0][3]))

#                     # Calculate the area of the bounding box
#                     width = np.linalg.norm(np.array(top_right_corner) - np.array(top_left_corner))
#                     height = np.linalg.norm(np.array(top_left_corner) - np.array(bottom_left_corner))
#                     area = width * height

#                     if area > max_area:
#                         max_area = area
#                         largest_box = [top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner]
#                         largest_text = res[1].lower()

#                 if largest_box:
#                     largest_text = predict.possible_corrections(largest_text)[0]
#                     if largest_text != "kurkure":
#                         largest_text = "cheetos"
#                     # largest_text = "geers"
#                     print("largest_text = " , largest_text)

#                     # Draw polygon for the largest detected text
#                     pts = np.array(largest_box, np.int32)
#                     pts = pts.reshape((-1, 1, 2))
#                     img = cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 0), thickness=5)

#                     # Write the text just above the bounding box
#                     font = cv2.FONT_HERSHEY_SIMPLEX
#                     font_scale = 1
#                     font_thickness = 2 
#                     text_size = cv2.getTextSize(largest_text, font, font_scale, font_thickness)[0]
#                     text_x = largest_box[0][0]
#                     text_y = largest_box[0][1] - 10
#                     cv2.putText(img, largest_text, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness)
                    
#                     flavours = database_interaction.get_flavours(largest_text)

#                     # Apply possible corrections to all words in text_only
#                     corrected_text_only = [predict.possible_corrections(word)[0] for word in text_only]
#                     print(corrected_text_only)
#                     combinations = generate_two_combinations(corrected_text_only)
#                     print("combinations = " , combinations)
#                     matches = list({sub for item in combinations for sub in flavours if sub in item})

#                     # print(matches)
#                     print(largest_text + ",", matches[0])  

#             else:
#                 print(f"No text detected in image {image_files[i]}")

#             # Display the image with the bounding box and text
#             plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#             plt.axis('off')
#             plt.show()


# import easyocr
# import cv2
# from matplotlib import pyplot as plt
# import numpy as np
# import os
# import database_interaction
# import predict
# from itertools import permutations

# def list_image_files(folder_path):
#     image_extensions = {'.jpg'}
#     image_files = []

#     for file_name in os.listdir(folder_path):
#         if os.path.splitext(file_name)[1].lower() in image_extensions:
#             image_files.append(file_name)
    
#     return image_files

# def generate_two_combinations(items):
#     return [' '.join(p) for p in permutations(items, 2)]

# def get_unique_filename(folder_path, base_name, extension='.jpg'):
#     count = 1
#     new_filename = base_name + extension
#     while os.path.exists(os.path.join(folder_path, new_filename)):
#         new_filename = f"{base_name}_copy{count}{extension}"
#         count += 1
#     return new_filename

# def text_detection(folder_path):
#     image_files = list_image_files(folder_path)

#     if not image_files:
#         print("No image files in the folder")
#     else:
#         for i in range(len(image_files)):
#             image_path = os.path.join(folder_path, image_files[i])
#             reader = easyocr.Reader(['en'], gpu=True)
#             result = list(reader.readtext(image_path))
            
#             text_only = [res[1].lower() for res in result]

#             img = cv2.imread(image_path)  # Read the image once outside the inner loop

#             if result:
#                 # Find the largest text bounding box
#                 largest_box = None
#                 max_area = 0
#                 largest_text = ""

#                 for res in result:
#                     # Extract the four corners of the bounding box
#                     top_left_corner = tuple(map(int, res[0][0]))
#                     top_right_corner = tuple(map(int, res[0][1]))
#                     bottom_right_corner = tuple(map(int, res[0][2]))
#                     bottom_left_corner = tuple(map(int, res[0][3]))

#                     # Calculate the area of the bounding box
#                     width = np.linalg.norm(np.array(top_right_corner) - np.array(top_left_corner))
#                     height = np.linalg.norm(np.array(top_left_corner) - np.array(bottom_left_corner))
#                     area = width * height

#                     if area > max_area:
#                         max_area = area
#                         largest_box = [top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner]
#                         largest_text = res[1].lower()

#                 if largest_box:
#                     largest_text = predict.possible_corrections(largest_text)[0]
#                     if largest_text != "kurkure":
#                         largest_text = "cheetos"

#                     # Draw polygon for the largest detected text
#                     pts = np.array(largest_box, np.int32)
#                     pts = pts.reshape((-1, 1, 2))
#                     img = cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 0), thickness=5)

#                     # Write the text just above the bounding box
#                     font = cv2.FONT_HERSHEY_SIMPLEX
#                     font_scale = 1
#                     font_thickness = 2 
#                     text_size = cv2.getTextSize(largest_text, font, font_scale, font_thickness)[0]
#                     text_x = largest_box[0][0]
#                     text_y = largest_box[0][1] - 10
#                     cv2.putText(img, largest_text, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness)
                    
#                     flavours = database_interaction.get_flavours(largest_text)

#                     # Apply possible corrections to all words in text_only
#                     corrected_text_only = [predict.possible_corrections(word)[0] for word in text_only]
#                     combinations = generate_two_combinations(corrected_text_only)
#                     matches = list({sub for item in combinations for sub in flavours if sub in item})

#                     if matches:
#                         match = matches[0]
#                         base_name = f"{largest_text}_{match}"
#                         new_filename = get_unique_filename(folder_path, base_name)

#                         # Rename the file
#                         new_filepath = os.path.join(folder_path, new_filename)
#                         os.rename(image_path, new_filepath)
#                         print(f"File renamed to {new_filename}")

#                         # Display the image with the bounding box and text
#                         plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#                         plt.axis('off')
#                         plt.show()
#                     else:
#                         print(f"No matches found for {largest_text}")

#                 else:
#                     print(f"No largest box found for image {image_files[i]}")

#             else:
#                 print(f"No text detected in image {image_files[i]}")


# # Example usage
# # text_detection("image_processing_testing/connecting_database/images/chips")
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import database_interaction
import predict
from itertools import permutations

def list_image_files(folder_path):
    image_extensions = {'.jpg'}
    image_files = []

    for file_name in os.listdir(folder_path):
        if os.path.splitext(file_name)[1].lower() in image_extensions:
            image_files.append(file_name)
    
    return image_files

def generate_two_combinations(items):
    return [' '.join(p) for p in permutations(items, 2)]

def get_unique_filename(folder_path, base_name, extension='.jpg'):
    count = 1
    new_filename = base_name + extension
    while os.path.exists(os.path.join(folder_path, new_filename)):
        new_filename = f"{base_name}_copy{count}{extension}"
        count += 1
    return new_filename

def text_detection(folder_path):
    image_files = list_image_files(folder_path)

    if not image_files:
        print("No image files in the folder")
    else:
        for i in range(len(image_files)):
            image_path = os.path.join(folder_path, image_files[i])
            reader = easyocr.Reader(['en'], gpu=True)
            result = list(reader.readtext(image_path))
            
            text_only = [res[1].lower() for res in result]

            img = cv2.imread(image_path)  # Read the image once outside the inner loop

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
                        largest_text = res[1].lower()

                if largest_box:
                    largest_text = predict.possible_corrections(largest_text)[0]
                    if largest_text != "kurkure":
                        largest_text = "cheetos"

                    # Draw polygon for the largest detected text
                    pts = np.array(largest_box, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    img = cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 0), thickness=5)

                    # Write the text just above the bounding box
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 1
                    font_thickness = 2 
                    text_size = cv2.getTextSize(largest_text, font, font_scale, font_thickness)[0]
                    text_x = largest_box[0][0]
                    text_y = largest_box[0][1] - 10
                    cv2.putText(img, largest_text, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness)
                    
                    flavours = database_interaction.get_flavours(largest_text)

                    # Apply possible corrections to all words in text_only
                    corrected_text_only = [predict.possible_corrections(word)[0] for word in text_only]
                    combinations = generate_two_combinations(corrected_text_only)
                    matches = list({sub for item in combinations for sub in flavours if sub in item})

                    if matches:
                        match = matches[0]
                        base_name = f"{largest_text}_{match}"
                        new_filename = get_unique_filename(folder_path, base_name)

                        # Rename the file
                        new_filepath = os.path.join(folder_path, new_filename)
                        os.rename(image_path, new_filepath)
                        
                        print(f"File renamed from {image_path} to {new_filepath}")

                        # Display the image with the bounding box and text
                        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                        plt.axis('off')
                        plt.show()
                    else:
                        print(f"No matches found for {largest_text}")

                else:
                    print(f"No largest box found for image {image_files[i]}")

            else:
                print(f"No text detected in image {image_files[i]}")

# Example usage
# text_detection("image_processing_testing/connecting_database/images/chips")
