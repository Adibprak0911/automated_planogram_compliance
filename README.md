# Automated Planogram Compliance 

## Problem Statement

Ensuring products are correctly placed according to planograms in retail stores is labor-intensive and prone to human error, impacting inventory management and customer satisfaction.

## Solution

Our solution integrates drones, computer vision, and machine learning to automate planogram compliance. Drones capture shelf images, and machine learning models analyze these images to ensure products are correctly placed. This system improves store efficiency, reduces labor costs, and enhances inventory management.

## Structure of our project - Computer Vision aspect

1) Panorama Generation - Generates a workable panorama image from the video taken by the drone

2) Object identification - Detect the item so as to use text detection upon it (Using Keras and TF)

3) Text detection - To get the product name (Using EasyOCR)

4) Object detection - To obtain location data of the products (Using YOLO)

5) Planogram Generation - Uses Location data from YOLO and product ID from Easy OCR for generation of a planogram

6) Planogram Compliance Checking - Compares the planogram requirements and planogram identified and finds out products out of place

## Structure of our project - Robotics (ROS2 and Gazebo)

1) Creating a virtual environment - Simulate the “Walmart” environment with items, shelves and a warehouse (Using Gazebo)

2) Importing the drone module - Understand the real world physics of drone flight travel in the environment (Using PX4-Autopilot)

3) Controls function and sensory feedback - Movement to control thrust,rpy with sensor feedback (Using Python and MavSDK)

4) Spawning items with an excel planogram - Goes through a document and spawns items based on given X,Y,Z coordinates

5) Camera feedback and launch file - Mounting a depth camera onto the drone and getting the drone’s POV (Using Python and CV_bridge)

6) Front end - Website for users to customise the world. Can also be utilised to feed planograms to Walmart from vendors






