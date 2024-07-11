import cv2
import numpy as np
import os

# Path to the video file
video_file = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kurkure2.mp4'

# Specific directory to save frames
output_dir = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kframes2'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Directory to save resized ROIs
resized_roi_dir = '/home/user/Documents/automated_planogram_compliance/automated_planogram_compliance-1/database_creation/kuresize2'
if not os.path.exists(resized_roi_dir):
    os.makedirs(resized_roi_dir)

# Load YOLO
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Function to process images and detect objects
def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}")
        return

    height, width = image.shape[:2]

    # Create a blob from the image
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Initialize lists to hold detected bounding boxes, confidences, and class IDs
    boxes = []
    confidences = []
    class_ids = []

    # Loop over each of the layer outputs
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # You can adjust the threshold
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Maxima Suppression to keep the best bounding boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Ensure there is at least one detection
    if len(indexes) > 0:
        # Loop over the detections
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = (0, 255, 0)  # Green bounding box

            # Draw bounding box and label
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Save the image with bounding boxes for debugging
        debug_filename = os.path.join(output_dir, f"debug_{os.path.basename(image_path)}")
        cv2.imwrite(debug_filename, image)

    else:
        print(f"No objects detected in {image_path}")

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

    # Process the frame to detect objects
    process_image(frame_filename)

    frame_number += 1

    # Print frame number as feedback (optional)
    print(f"Processed frame {frame_number}")

# Release the video capture object
cap.release()

print(f"Extracted {frame_number} frames to {output_dir}.")
print(f"Processed frames with bounding boxes saved to {output_dir}.")

# Close all windows and clean up (if any were opened)
# cv2.destroyAllWindows()