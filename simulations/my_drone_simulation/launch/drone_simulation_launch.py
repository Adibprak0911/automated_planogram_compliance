# ~/Documents/automated_planogram_compliance-1/simulations/my_drone_simulation/launch/drone_simulation_launch.py

import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['make', 'px4_sitl', 'gz_x500_depth_windy'],
            cwd=os.path.expanduser('~/Documents/automated_planogram_compliance-1/simulations/PX4-Autopilot'),
            output='screen'
        ),
        ExecuteProcess(
            cmd=['python3', 'keyboard-mavsdk-test.py'],
            cwd=os.path.expanduser('~/Documents/automated_planogram_compliance-1/simulations/PX4-ROS2-Gazebo-YOLOv8'),
            output='screen'
        ),
        ExecuteProcess(
            cmd=['python3', 'uav_camera_det.py'],
            cwd=os.path.expanduser('~/Documents/automated_planogram_compliance-1/simulations/PX4-ROS2-Gazebo-YOLOv8'),
            output='screen'
        ),
        ExecuteProcess(
            cmd=['ros2', 'run', 'ros_gz_image', 'image_bridge', '/camera'],
            output='screen'
        )
    ])
