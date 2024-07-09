
import cv2 as cv
import numpy as np

# File paths
# weights_path = "image_processing_testing/YOLO/trial_2/yolov3.weights"
# cfg_path = "image_processing_testing/YOLO/yolov3.cfg"
# names_path = "image_processing_testing/YOLO/coco.names"
# image_path = "image_processing_testing/YOLO/dog.jpg"
weights_path = "yolov3.weights"
cfg_path = "yolov3.cfg"
names_path = "coco.names"
image_path = "test_1.jpeg"

# Load YOLO
print("Loading YOLO")
net = cv.dnn.readNet(weights_path, cfg_path)

# Load class names
classes = []
with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()

# Determine the output layer names from the YOLO model
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
print("YOLO LOADED")

# Capture frame-by-frame
img = cv.imread(image_path)
img = cv.resize(img, None, fx=0.4, fy=0.4)
height, width, channels = img.shape

# Blob for preprocessing
blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

# Detecting objects
net.setInput(blob)
outs = net.forward(output_layers)

# Showing information on the screen
class_ids = []
confidences = []
boxes = []

for out in outs:
    for detection in out:
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
            class_ids.append(class_id)  # Corrected this line

# NMS for non-maximum suppression
indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
colors = np.random.uniform(0, 255, size=(len(classes), 3))
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])  # Corrected this line
        color = colors[class_ids[i]]
        cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv.putText(img, label, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
