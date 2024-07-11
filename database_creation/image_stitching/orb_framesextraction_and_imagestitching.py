#manually handle the stitching process using key points and homography:

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


def stitch_frames_manual(frame_folder, output_image_path):
    # Read the frames from the folder
    frame_files = [os.path.join(frame_folder, f) for f in os.listdir(frame_folder) if f.endswith(".jpg")]
    frames = [cv2.imread(frame_file) for frame_file in sorted(frame_files)]
    
    # Initialize ORB detector
    orb = cv2.ORB_create()
    
    # Initialize lists to store keypoints and descriptors
    keypoints_list = []
    descriptors_list = []
    
    # Detect ORB features and compute descriptors
    for frame in frames:
        keypoints, descriptors = orb.detectAndCompute(frame, None)
        keypoints_list.append(keypoints)
        descriptors_list.append(descriptors)
    
    # Initialize matcher
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    # Stitching result initialized with the first frame
    stitched_image = frames[0]
    
    for i in range(1, len(frames)):
        # Match descriptors between consecutive frames
        matches = matcher.match(descriptors_list[i-1], descriptors_list[i])
        matches = sorted(matches, key=lambda x: x.distance)
        
        # Extract matched keypoints
        src_pts = np.float32([keypoints_list[i-1][m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints_list[i][m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
        
        # Compute homography matrix
        H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)
        
        # Warp current frame to align with the previous frames
        height, width = stitched_image.shape[:2]
        stitched_image = cv2.warpPerspective(stitched_image, H, (width + frames[i].shape[1], height))
        
        # Copy the current frame onto the stitched image
        stitched_image[0:frames[i].shape[0], 0:frames[i].shape[1]] = frames[i]
    
    # Save the final stitched image
    cv2.imwrite(output_image_path, stitched_image)
    print(f"Stitched image saved at {output_image_path}")

# Example usage:
# stitch_frames_manual("output_frames", "panoramic_shelf.jpg")

def create_panoramic_shelf_view(video_path, output_folder, output_image_path, frame_rate=1):
    extract_frames(video_path, output_folder, frame_rate)
    stitch_frames_manual(output_folder, output_image_path)

# Example usage:
create_panoramic_shelf_view("/home/user/Documents/automated_planogram_compliance-1/database_creation/image_stitching/videos/panoramatrial2.mov", 
                            "/home/user/Documents/automated_planogram_compliance-1/database_creation/image_stitching/output frames", 
                            "/home/user/Documents/automated_planogram_compliance-1/database_creation/image_stitching/panoramic_shelf.jpg", frame_rate=10)