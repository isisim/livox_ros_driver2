from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python import get_package_share_path

rviz_config_path = str(get_package_share_path('livox_ros_driver2') / 'config' / 'display_point_cloud_ROS2.rviz')
lidar_config_path = get_package_share_path('livox_ros_driver2') / 'config' / 'final_config.json'

def generate_launch_description():
    declare_args = [ 
        DeclareLaunchArgument('xfer_format', default_value= '0', description='Transfer format (0-Pointcloud2, 1-customized)'),
        DeclareLaunchArgument('multi_topic', default_value= '1', description='Multi-topic configuration (0-All LiDARs share same topic, 1-One LiDAR one topic)'),
        DeclareLaunchArgument('data_src', default_value= '0', description='Data source configuration (0-lidar, others-invalid)'),
        DeclareLaunchArgument('publish_freq', default_value='10.0', description='Publish frequency'),
        DeclareLaunchArgument('output_type', default_value='0', description='Output type'),
        DeclareLaunchArgument('frame_id', default_value='livox_frame', description='Frame ID'),
        DeclareLaunchArgument('lvx_file_path', default_value='/home/livox/livox_test.lvx', description='Path to LVX file'),
        DeclareLaunchArgument('cmdline_bd_code', default_value='livox0000000001', description='Command line board code'),
        DeclareLaunchArgument('user_config_path', default_value=str(lidar_config_path), description='Path to the user config file')
    ]
    
    xfer_format = LaunchConfiguration('xfer_format')
    multi_topic = LaunchConfiguration('multi_topic')
    data_src= LaunchConfiguration('data_src')            
    publish_freq= LaunchConfiguration('publish_freq')
    output_type= LaunchConfiguration('output_type')
    frame_id= LaunchConfiguration('frame_id')
    lvx_file_path=LaunchConfiguration('lvx_file_path')
    user_config_path= LaunchConfiguration('user_config_path')
    cmdline_bd_code= LaunchConfiguration('cmdline_bd_code')
    
    livox_driver = Node(
        package='livox_ros_driver2',
        executable='livox_ros_driver2_node',
        name='livox_lidar_publisher',
        output='screen',
        parameters= [{
            "xfer_format": xfer_format,
            "multi_topic": multi_topic,
            "data_src": data_src,
            "publish_freq": publish_freq,
            "output_data_type": output_type,
            "frame_id": frame_id,
            "lvx_file_path": lvx_file_path,
            "user_config_path": user_config_path,
            "cmdline_input_bd_code": cmdline_bd_code
        }]
        )
    
    # livox_rviz = Node(
    #         package='rviz2',
    #         executable='rviz2',
    #         output='screen',
    #         arguments=['--display-config', rviz_config_path]
    #     )
    
    ld = LaunchDescription(declare_args)
    ld.add_action(livox_driver)
    # ld.add_action(livox_rviz)
    return ld