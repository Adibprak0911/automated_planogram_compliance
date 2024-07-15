import cv2
import os

# Path to the video file
video_file = '/home/user/Documents/automated_planogram_compliance-1/database_creation/newkurkure.mov'

# Specific directory to save frames
output_dir = '/home/user/Documents/automated_planogram_compliance-1/database_creation/frames/newkurkure/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the video file
cap = cv2.VideoCapture(video_file)
if not cap.isOpened():
    print(f"Error: Could not open video {video_file}.")
    exit()

frame_number = 0
saved_frame_number = 0

# Loop through the video frames
while True:
    ret, frame = cap.read()

    # If the frame was read correctly, ret is True
    if not ret:
        break

    # Save only every third frame
    if frame_number % 10 == 0:
        frame_filename = os.path.join(output_dir, f'frame_{saved_frame_number:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
        saved_frame_number += 1

    frame_number += 1

    # Print frame number as feedback (optional)
    print(f"Processed frame {frame_number}")

# Release the video capture object and close all windows
cap.release()

print(f"Extracted {saved_frame_number} frames to {output_dir}.")
