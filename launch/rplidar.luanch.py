import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    serial_port_path = '/dev/serial/...'
    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': serial_port_path,
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )
    ])