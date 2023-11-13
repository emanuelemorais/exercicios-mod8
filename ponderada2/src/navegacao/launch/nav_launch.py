from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    gazebo_dir = get_package_share_directory('turtlebot3_gazebo')
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_dir + '/launch/turtlebot3_world.launch.py')
    )
    
    cartographer_dir = get_package_share_directory('turtlebot3_cartographer')
    cartographer_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(cartographer_dir + '/launch/cartographer.launch.py')
    )

    navigation_launch = ExecuteProcess(
        cmd=['ros2', 'launch', 'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=gazebo.yaml'],
        output='screen'
    )


    return LaunchDescription([
        gazebo_launch,
        Node(
            package='navegacao',
            executable='nav_robot',
            name='nav_robot',
            prefix='gnome-terminal --',
            output='screen'
        ),
        navigation_launch
        ])
