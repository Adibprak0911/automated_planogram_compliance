import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'camera',
            self.listener_callback,
            10)
        self.subscription
        self.br = CvBridge()

        # Directory to save video
        self.video_filename = 'simulations/PX4-ROS2-Gazebo-YOLOv8/output_video.avi'  # Change this path as needed
        self.frame_width = 640  # Set according to your image width
        self.frame_height = 480  # Set according to your image height
        self.frame_rate = 24  # frames per second

        # Initialize VideoWriter
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self.video_writer = cv2.VideoWriter(self.video_filename, fourcc, self.frame_rate, (self.frame_width, self.frame_height))
        
        if not self.video_writer.isOpened():
            self.get_logger().error('Failed to open VideoWriter')
            rclpy.shutdown()

        self.should_exit = False

    def listener_callback(self, data):
        self.get_logger().info('Receiving video frame')
        current_frame = self.br.imgmsg_to_cv2(data, desired_encoding="bgr8")

        # Check if the frame was correctly converted
        if current_frame is None:
            self.get_logger().error('Failed to convert ROS Image to OpenCV frame')
            return

        # Display the frame
        cv2.imshow('Detected Frame', current_frame)

        # Save the frame to the video file
        self.get_logger().info(f'Saving frame to {self.video_filename}')
        self.video_writer.write(current_frame)

        # Check for 'Q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.should_exit = True
            rclpy.shutdown()

    def destroy_node(self):
        # Release the VideoWriter and close all OpenCV windows
        self.get_logger().info('Releasing VideoWriter and closing all OpenCV windows')
        self.video_writer.release()
        cv2.destroyAllWindows()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()

    # Check if the subscription is correctly created
    if image_subscriber.subscription is None:
        image_subscriber.get_logger().error('Failed to create subscription')
        rclpy.shutdown()

    while rclpy.ok() and not image_subscriber.should_exit:
        rclpy.spin_once(image_subscriber)

    image_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
