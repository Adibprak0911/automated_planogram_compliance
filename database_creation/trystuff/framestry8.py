import cv2
import os

# Path to the video file
video_file = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kurkure.mp4'

# Specific directory to save frames
output_dir = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kurkureframes1'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Directory to save resized ROIs with bounding box
resized_roi_dir = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kurkureframesresized1'
if not os.path.exists(resized_roi_dir):
    os.makedirs(resized_roi_dir)

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

        # Extract region of interest (ROI)
        roi = image[y:y+h, x:x+w]

        # Resize the ROI to focus/zoom in on the object detected
        resized_roi = cv2.resize(roi, (w * 2, h * 2), interpolation=cv2.INTER_LINEAR)

        # Draw the bounding rectangle on the resized ROI with desired color (e.g., red)
        bounding_box_color = (0, 0, 255)  # Red color
        cv2.rectangle(resized_roi, (0, 0), (w * 2 - 1, h * 2 - 1), bounding_box_color, 2)

        # Save the resized ROI with bounding box to a directory
        resized_roi_filename = os.path.join(resized_roi_dir, os.path.basename(image_path))
        cv2.imwrite(resized_roi_filename, resized_roi)

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

    # Process the frame to find contours and resize ROI with bounding box
    process_image(frame_filename)

    frame_number += 1

    # Print frame number as feedback (optional)
    print(f"Processed frame {frame_number}")

# Release the video capture object
cap.release()

print(f"Extracted {frame_number} frames to {output_dir}.")
print(f"Resized ROIs with bounding box saved to {resized_roi_dir}.")

# Close all windows and clean up (if any were opened)
# cv2.destroyAllWindows()
