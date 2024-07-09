import cv2
import os
import numpy as np

#path to the video file
video_file = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kurkure.mp4'

# # Directory to save frames
# output_dir = 'frames'
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # Directory to save frames on your desktop
# videoframes = os.path.join(os.path.expanduser('~'), 'Desktop')
# output_dir = os.path.join(videoframes, 'frames')
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# Specific directory to save frames
output_dir = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kurkureframes'  
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the video file
cap = cv2.VideoCapture(video_file)
if not cap.isOpened():
    print(f"Error: Could not open video {video_file}.")
    exit()

frame_number = 0

# Loop through the video frames
while True:
    ret, frame = cap.read()

    # If the frame was read correctly, ret is True
    if not ret:
        break

    # Save the frame as an image
    frame_filename = os.path.join(output_dir, f'frame_{frame_number:04d}.jpg')
    cv2.imwrite(frame_filename, frame)

    frame_number += 1

    # # Display the frame
    # cv2.imshow('Frame', frame)
    
    # # Press 'q' on keyboard to exit
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     break
    # Print frame number as feedback (optional)
    print(f"Processed frame {frame_number}")

# Release the video capture object and close all windows
cap.release()
# cv2.destroyAllWindows()

print(f"Extracted {frame_number} frames to {output_dir}.")
