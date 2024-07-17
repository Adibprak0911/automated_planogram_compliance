import cv2
import os
import numpy as np

def extract_frames(video_path, output_folder, frame_rate=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        if count % frame_rate == 0:
            cv2.imwrite(f"{output_folder}/frame{count}.jpg", image)
        success, image = vidcap.read()
        count += 1
    vidcap.release()
    print(f"Extracted {count // frame_rate} frames from the video.")

# Example usage:
# extract_frames("path_to_your_video.mov", "output_frames", frame_rate=10)

def stitch_frames(frame_folder, output_image_path):
    # Read the frames from the folder
    frame_files = [os.path.join(frame_folder, f) for f in os.listdir(frame_folder) if f.endswith(".jpg")]
    frames = [cv2.imread(frame_file) for frame_file in sorted(frame_files)]

    # Initialize the stitcher
    stitcher = cv2.Stitcher_create()

    # Perform stitching
    status, stitched_image = stitcher.stitch(frames)

    if status == cv2.Stitcher_OK:
        # Save the final stitched image
        cv2.imwrite(output_image_path, stitched_image)
        print(f"Stitched image saved at {output_image_path}")
    else:
        print(f"Stitching failed with status code {status}")

# Example usage:
# stitch_frames("output_frames", "panoramic_shelf.jpg")

def create_panoramic_shelf_view(video_path, output_folder, output_image_path, frame_rate=1):
    extract_frames(video_path, output_folder, frame_rate)
    stitch_frames(output_folder, output_image_path)

# Example usage:
<<<<<<< Updated upstream
create_panoramic_shelf_view("/home/user/Documents/automated_planogram_compliance-1/database_creation/image_stitching/videos/trialvideo.mp4", 
                            "/home/user/Documents/automated_planogram_compliance-1/database_creation/image_stitching/output frames", 
                            "/home/user/Documents/automated_planogram_compliance-1/database_creation/image_stitching/trial_panoramic_videoofchips.jpg", frame_rate=10)
=======
create_panoramic_shelf_view("database_creation/image_stitching/videos/output_video.mov", 
                            "database_creation/image_stitching/output frames", 
                            "database_creation/image_stitching/panoramic_shelf.jpg", frame_rate=10)
>>>>>>> Stashed changes




#-------------------------STITCH FUNCTION USING " Stitcher_SCANS" MODE---------------------------
# Here’s an improved version of the stitching function using OpenCV’s feature-based stitching capabilities:
# def stitch_frames(frame_folder, output_image_path):
#     # Read the frames from the folder
#     frame_files = [os.path.join(frame_folder, f) for f in os.listdir(frame_folder) if f.endswith(".jpg")]
#     frames = [cv2.imread(frame_file) for frame_file in sorted(frame_files)]
    
#     # Initialize the stitcher
#     stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
    
#     # Perform stitching
#     status, stitched_image = stitcher.stitch(frames)
    
#     if status == cv2.Stitcher_OK:
#         # Save the final stitched image
#         cv2.imwrite(output_image_path, stitched_image)
#         print(f"Stitched image saved at {output_image_path}")
#     else:
#         print(f"Stitching failed with status code {status}")

# # Example usage:
# # stitch_frames("output_frames", "panoramic_shelf.jpg")