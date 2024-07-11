import cv2
import os

# Path to the video file
video_file = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kurkure.mp4'

# Specific directory to save frames
output_dir = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kurkureframes1'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Directory to save resized ROIs
resized_roi_dir = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kurkureframesresized1'
if not os.path.exists(resized_roi_dir):
    os.makedirs(resized_roi_dir)

# Function to find all image files recursively in a directory
def find_images(directory):
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                image_files.append(os.path.join(root, file))
    return image_files

# Function to process images and find contours
def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find contours
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ensure there is at least one contour
    if len(contours) > 0:
        # Assume only one contour for simplicity (you can modify for multiple contours)
        contour = max(contours, key=cv2.contourArea)
        
        # Get the coordinates of the bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)
        
        # Calculate center of the bounding rectangle
        center_x = x + w // 2
        center_y = y + h // 2
        
        # Determine the size of the resized image (adjust the scale factor as needed)
        scale_factor = 2.0  # Example scale factor
        new_width = int(w * scale_factor)
        new_height = int(h * scale_factor)
        
        # Calculate new top-left corner of the bounding box for cropping
        crop_x = max(center_x - new_width // 2, 0)
        crop_y = max(center_y - new_height // 2, 0)
        
        # Ensure the crop stays within image bounds
        crop_x = min(crop_x, image.shape[1] - new_width)
        crop_y = min(crop_y, image.shape[0] - new_height)
        
        # Crop and resize the ROI to focus/zoom in on the object detected
        cropped_resized_roi = cv2.resize(image[crop_y:crop_y+new_height, crop_x:crop_x+new_width], (new_width, new_height), interpolation=cv2.INTER_LINEAR)

        # Save the cropped and resized ROI to a directory
        resized_roi_filename = os.path.join(resized_roi_dir, os.path.basename(image_path))
        cv2.imwrite(resized_roi_filename, cropped_resized_roi)

    else:
        print(f"No contours found in {image_path}")

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

    # Process the frame to find contours and resize ROI
    process_image(frame_filename)

    frame_number += 1

    # Print frame number as feedback (optional)
    print(f"Processed frame {frame_number}")

# Release the video capture object
cap.release()

print(f"Extracted {frame_number} frames to {output_dir}.")
print(f"Cropped and resized ROIs saved to {resized_roi_dir}.")

# Close all windows and clean up (if any were opened)
# cv2.destroyAllWindows()
