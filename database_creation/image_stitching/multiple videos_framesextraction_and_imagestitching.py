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

def stitch_frames(frame_folder, output_image_path):
    frame_files = [os.path.join(frame_folder, f) for f in os.listdir(frame_folder) if f.endswith(".jpg")]
    frames = [cv2.imread(frame_file) for frame_file in sorted(frame_files)]

    stitcher = cv2.Stitcher_create()
    status, stitched_image = stitcher.stitch(frames)

    if status == cv2.Stitcher_OK:
        cv2.imwrite(output_image_path, stitched_image)
        print(f"Stitched image saved at {output_image_path}")
    else:
        print(f"Stitching failed with status code {status}")

def create_panoramic_shelf_view(video_path, output_folder, output_image_path, frame_rate=1):
    extract_frames(video_path, output_folder, frame_rate)
    stitch_frames(output_folder, output_image_path)

def process_videos(videos_folder, output_base_folder, frame_rate=1):
    for video_file in os.listdir(videos_folder):
        if video_file.endswith(('.mp4', '.mov', '.avi', '.mkv')):
            video_path = os.path.join(videos_folder, video_file)
            video_name = os.path.splitext(video_file)[0]
            output_folder = os.path.join(output_base_folder, video_name + "_frames")
            output_image_path = os.path.join(output_base_folder, video_name + "_panorama.jpg")
            create_panoramic_shelf_view(video_path, output_folder, output_image_path, frame_rate)

# Example usage:
process_videos("/home/user/Documents/automated_planogram_compliance-1/database_creation/image_stitching/videos/", "/home/user/Documents/automated_planogram_compliance-1/database_creation/image_stitching/output frames/", frame_rate=10)
