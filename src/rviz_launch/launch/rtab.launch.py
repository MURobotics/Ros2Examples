#
#!/usr/bin/env python3
# Copyright  All Rights Reserved.
# @author 
#
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node, ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('rviz_launch'),
        'config',
        'params.yml'
    )

    my_node_2 = Node(
        package ='my_package',
        executable ='my_node',
        parameters = [config],
        arguments = []
    )

    my_node = Node(
        package = 'rviz2',
        executable = 'rviz2',
        parameters = [config],
        arguments= []
    )
         
    return LaunchDescription([
        my_node
    ])