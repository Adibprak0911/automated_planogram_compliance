# import cv2 as cv
# import numpy as np

# # File paths
# weights_path = "yolov3.weights"
# cfg_path = "yolov3.cfg"
# names_path = "coco.names"
# video_path = "sample_video.mp4"  # Path to input video file
# output_path = "output_video.mp4"  # Path to save the output video file

# # Load YOLO
# print("Loading YOLO")
# net = cv.dnn.readNet(weights_path, cfg_path)

# # Load class names
# classes = []
# with open(names_path, "r") as f:
#     classes = [line.strip() for line in f.readlines()]

# layer_names = net.getLayerNames()

# # Determine the output layer names from the YOLO model
# output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
# print("YOLO LOADED")

# # Open video file
# cap = cv.VideoCapture(video_path)

# # Get video properties
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# fps = int(cap.get(cv.CAP_PROP_FPS))

# # Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'mp4v')  # You can use other codecs as well
# out = cv.VideoWriter(output_path, fourcc, fps, (width, height))

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Blob for preprocessing
#     blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

#     # Detecting objects
#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Showing information on the screen
#     class_ids = []
#     confidences = []
#     boxes = []

#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:
#                 # Object detected
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)

#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)

#                 # Rectangle coordinates
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # NMS for non-maximum suppression
#     indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#     colors = np.random.uniform(0, 255, size=(len(classes), 3))
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             color = colors[class_ids[i]]
#             cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#             cv.putText(frame, label, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#     # Write the frame to the output video file
#     out.write(frame)

#     # Display the resulting frame
#     cv.imshow("Frame", frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release everything if job is finished
# cap.release()
# out.release()
# cv.destroyAllWindows()


# import cv2 as cv
# import numpy as np
# import os

# # File paths
# weights_path = "yolov3.weights"
# cfg_path = "yolov3.cfg"
# names_path = "coco.names"
# video_path = "sample_video.mp4"  # Path to input video file
# output_path = "output_video.mp4"  # Path to save the output video file

# # Verify file paths
# for path in [weights_path, cfg_path, names_path, video_path]:
#     if not os.path.isfile(path):
#         print(f"Error: File not found - {path}")
#         exit()

# # Load YOLO
# print("Loading YOLO")
# net = cv.dnn.readNet(weights_path, cfg_path)
# print("YOLO LOADED")

# # Load class names
# classes = []
# with open(names_path, "r") as f:
#     classes = [line.strip() for line in f.readlines()]

# layer_names = net.getLayerNames()

# # Determine the output layer names from the YOLO model
# output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# # Open video file
# cap = cv.VideoCapture(video_path)

# if not cap.isOpened():
#     print(f"Error: Unable to open video file - {video_path}")
#     exit()

# # Get video properties
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# fps = int(cap.get(cv.CAP_PROP_FPS))

# # Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'mp4v')  # You can use other codecs as well
# out = cv.VideoWriter(output_path, fourcc, fps, (width, height))

# if not out.isOpened():
#     print(f"Error: Unable to open video writer - {output_path}")
#     cap.release()
#     exit()

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Blob for preprocessing
#     blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

#     # Detecting objects
#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Showing information on the screen
#     class_ids = []
#     confidences = []
#     boxes = []

#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.5:
#                 # Object detected
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)

#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)

#                 # Rectangle coordinates
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # NMS for non-maximum suppression
#     indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#     colors = np.random.uniform(0, 255, size=(len(classes), 3))
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             color = colors[class_ids[i]]
#             cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#             cv.putText(frame, label, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#     # Write the frame to the output video file
#     out.write(frame)

#     # Display the resulting frame
#     cv.imshow("Frame", frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release everything if job is finished
# cap.release()
# out.release()
# cv.destroyAllWindows()


import cv2 as cv
import numpy as np
import os

# File paths
weights_path = "yolov3.weights"
cfg_path = "yolov3.cfg"
names_path = "coco.names"
video_path = "test_  .mp4"  # Path to input video file
output_path = "output_video.mp4"  # Path to save the output video file

# Verify file paths
for path in [weights_path, cfg_path, names_path, video_path]:
    if not os.path.isfile(path):
        print(f"Error: File not found - {path}")
        exit()

# Load YOLO
print("Loading YOLO")
net = cv.dnn.readNet(weights_path, cfg_path)
print("YOLO LOADED")

# Load class names
classes = []
with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()

# Determine the output layer names from the YOLO model
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Open video file
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Unable to open video file - {video_path}")
    exit()

# Get video properties
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # You can use other codecs as well
out = cv.VideoWriter(output_path, fourcc, fps, (width, height))

if not out.isOpened():
    print(f"Error: Unable to open video writer - {output_path}")
    cap.release()
    exit()

# Debug print to check the type of out before entering the loop
print(f"Type of out before the loop: {type(out)}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Blob for preprocessing
    blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

    # Detecting objects
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing information on the screen
    class_ids = []
    confidences = []
    boxes = []

    for out_blob in outs:
        for detection in out_blob:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
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

    # NMS for non-maximum suppression
    indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv.putText(frame, label, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Debug print to check the type of out inside the loop
    print(f"Type of out inside the loop before writing: {type(out)}")

    # Write the frame to the output video file
    out.write(frame)

    # Display the resulting frame
    cv.imshow("Frame", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()

# Debug print to check the type of out after releasing everything
print(f"Type of out after release: {type(out)}")
