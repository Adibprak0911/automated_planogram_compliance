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

## Demonstration 

### Step 1 - Website 

Access our website we generated with Streamlit. You give all the details (such as coordinates) of where to place an item to help generate the simulated environment. Here's a snippet of how it looks!

<img width="795" alt="Screenshot 2024-08-08 at 2 54 25 AM" src="https://github.com/user-attachments/assets/f9e223ea-d508-42c0-bd20-9cb5d57602b2">

<img width="916" alt="Screenshot 2024-08-08 at 2 57 36 AM" src="https://github.com/user-attachments/assets/c05d3a35-516a-422d-8eca-892069e37634">

You then just simply generate the excel sheet with all these details, which will later be used to make the Gazebo environment 

<img width="943" alt="Screenshot 2024-08-08 at 2 57 47 AM" src="https://github.com/user-attachments/assets/c1c1372e-10b1-4250-8a97-8393513f3c99">

### Step 2 - Launch Gazebo 

Here's how the world looks like with a drone at its supposed origin 

<img width="808" alt="Screenshot 2024-08-08 at 2 57 56 AM" src="https://github.com/user-attachments/assets/4652c2d1-b3ad-4aea-9fa7-965e3a52baab">

### Step 3 - Camera feedback and control functions

The code allows you to access the drone's control features such as throttle, roll, pitch and yaw by utilising some teleopkey capabilites. Hence from the depth camera mounted on our drone we can capture live footage of the drone's movements. Heres a snippet of the video it generates while moving through our shelves.

<img width="753" alt="Screenshot 2024-08-08 at 2 58 06 AM" src="https://github.com/user-attachments/assets/e94fb72d-377b-4823-b620-9164350466ab">

### Step 4 - Panorama generation (Image stitching)

Stiches the video into 1 image - Given below are the computer vision models tested in a real world scenario and Gazebo environment respectively.

### Step 5 - Product identification 









