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

# def process_image(image_path, reader):
#     result = reader.readtext(image_path)
#     print(len(result))

#     img = cv2.imread(image_path)  # Read the image once outside the inner loop

#     if result:
#         # Find the largest text bounding box
#         largest_box = None
#         max_area = 0
#         largest_text = ""

#         for res in result:
#             # Extract the four corners of the bounding box
#             top_left_corner = tuple(map(int, res[0][0]))
#             top_right_corner = tuple(map(int, res[0][1]))
#             bottom_right_corner = tuple(map(int, res[0][2]))
#             bottom_left_corner = tuple(map(int, res[0][3]))

#             # Calculate the area of the bounding box
#             width = np.linalg.norm(np.array(top_right_corner) - np.array(top_left_corner))
#             height = np.linalg.norm(np.array(top_left_corner) - np.array(bottom_left_corner))
#             area = width * height

#             if area > max_area:
#                 max_area = area
#                 largest_box = [top_left_corner, top_right_corner, bottom_right_corner, bottom_left_corner]
#                 largest_text = res[1]

#         if largest_box:
#             # Draw polygon for the largest detected text
#             pts = np.array(largest_box, np.int32)
#             pts = pts.reshape((-1, 1, 2))
#             img = cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 0), thickness=5)

#             # Write the text just above the bounding box
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             font_scale = 2
#             font_thickness = 2 
#             text_size = cv2.getTextSize(largest_text, font, font_scale, font_thickness)[0]
#             text_x = largest_box[0][0]
#             text_y = largest_box[0][1] - 10
#             cv2.putText(img, largest_text, (text_x, text_y), font, font_scale, (255, 0, 0), font_thickness)

#             print(largest_text)

#     else:
#         print(f"No text detected in image {image_path}")

#     return img

# def process_video(video_path, output_path, reader):
#     cap = cv2.VideoCapture(video_path)
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fps = int(cap.get(cv2.CAP_PROP_FPS))

#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         # Convert frame to image format compatible with easyOCR
#         temp_image_path = 'temp_frame.jpg'
#         cv2.imwrite(temp_image_path, frame)
#         processed_frame = process_image(temp_image_path, reader)
        
#         out.write(processed_frame)

#     cap.release()
#     out.release()

# folder_path = 'image_processing_testing/text_detection/identify_all_bounding/images'
# video_path = 'image_processing_testing/text_detection/identify_all_bounding/video_file/MicrosoftTeams-video.mp4'
# output_video_path = 'image_processing_testing/text_detection/identify_all_bounding/processed_video_file/processed_video.mp4'

# image_files = list_image_files(folder_path)
# print(image_files)
# print(len(image_files))

# if not image_files:
#     print("No image files in the folder")
# else:
#     reader = easyocr.Reader(['en'], gpu=True)
    
#     for i in range(len(image_files)):
#         image = folder_path + '/' + image_files[i]
#         processed_image = process_image(image, reader)

#         # Display the image with the bounding box and text
#         plt.imshow(cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB))
#         plt.axis('off')
#         plt.show()

# # Process the video
# process_video(video_path, output_video_path, reader)

import easyocr
import cv2
import numpy as np
import os

def list_video_files(folder_path):
    video_extensions = {'.mov', '.mp4', '.avi', '.mkv'}
    video_files = []

    for file_name in os.listdir(folder_path):
        if os.path.splitext(file_name)[1].lower() in video_extensions:
            video_files.append(file_name)
    
    return video_files

def process_frame(frame, reader):
    result = reader.readtext(frame)

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
            frame = cv2.polylines(frame, [pts], isClosed=True, color=(255, 0, 0), thickness=2)

            # Write the text just above the bounding box
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            font_thickness = 2
            text_size = cv2.getTextSize(largest_text, font, font_scale, font_thickness)[0]
            text_x = largest_box[0][0]
            text_y = largest_box[0][1] - 10
            cv2.putText(frame, largest_text, (text_x, text_y), font, font_scale, (255, 0, 0), font_thickness)

    return frame

def process_video(video_path, output_path, reader):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_frame(frame, reader)
        out.write(processed_frame)

    cap.release()
    out.release()

def process_videos_in_folder(folder_path, output_folder_path):
    video_files = list_video_files(folder_path)
    if not video_files:
        print("No video files in the folder")
        return

    reader = easyocr.Reader(['en'], gpu=True)

    for video_file in video_files:
        video_path = os.path.join(folder_path, video_file)
        output_video_path = os.path.join(output_folder_path, f"processed_{video_file}")
        print(f"Processing {video_file}...")
        process_video(video_path, output_video_path, reader)
        print(f"Processed video saved to {output_video_path}")

# Specify the folder containing videos and the folder to save processed videos
folder_path = 'image_processing_testing/text_detection/identify_all_bounding/video_file'
output_folder_path = 'image_processing_testing/text_detection/identify_all_bounding/processed_video_file'

# Create output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Process all videos in the folder
process_videos_in_folder(folder_path, output_folder_path)

