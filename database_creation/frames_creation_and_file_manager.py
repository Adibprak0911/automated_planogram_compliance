import cv2
import os
import shutil

def extract_and_combine_frames(video_folder, output_folder, final_output_folder):
    # Check if the video folder exists
    if not os.path.exists(video_folder):  # Error handling for non-existent directory
        print(f"Error: The video directory {video_folder} does not exist.")
        return
    
    # Create the output folders if they don't exist
    os.makedirs(output_folder, exist_ok=True)  # Concise directory creation
    os.makedirs(final_output_folder, exist_ok=True)  # Concise directory creation

    # Get list of video files
    video_files = [f for f in os.listdir(video_folder) if f.endswith('.mov')]
    
    if not video_files:  # Error handling for no video files found
        print(f"No video files found in the directory {video_folder}.")
        return

    saved_frame_number = 0

    # Process each video file
    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error: Could not open video {video_path}.")
            continue

        frame_number = 0

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            if frame_number % 3 == 0:
                frame_filename = os.path.join(output_folder, f'frame_{saved_frame_number:04d}.jpg')
                cv2.imwrite(frame_filename, frame)
                saved_frame_number += 1

            frame_number += 1

            print(f"Processed frame {frame_number} from video {video_file}")

        cap.release()

    counter = 1

    # Combine and rename frames
    for filename in sorted(os.listdir(output_folder)):
        file_path = os.path.join(output_folder, filename)

        if os.path.isfile(file_path):
            new_filename = f'{counter}.jpg'
            new_file_path = os.path.join(final_output_folder, new_filename)

            shutil.copy(file_path, new_file_path)
            counter += 1

    print(f"Files have been successfully combined and renamed in {final_output_folder}.")

# Example usage
video_folder = '/home/user/Documents/automated_planogram_compliance-1/database_creation/cheetos_masalaballs_videos/cheetos_masalaballs/'
output_folder = '/home/user/Documents/automated_planogram_compliance-1/database_creation/cheetos_masalaballs_frames/'
final_output_folder = '/home/user/Documents/automated_planogram_compliance-1/database_creation/frames/cheetos_masalaballs/'

extract_and_combine_frames(video_folder, output_folder, final_output_folder)