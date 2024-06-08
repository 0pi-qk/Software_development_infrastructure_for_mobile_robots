cmake_minimum_required(VERSION 3.5)
project(turtle_stalker)

# Find packages
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(turtlesim REQUIRED)
find_package(geometry_msgs REQUIRED)

# Add executable
add_executable(turtle_stalker_node
        src/main.cpp
        src/Turtle.cpp
        src/ROS_commands.cpp
        src/Random.cpp
        )

# Include directories
include_directories(
        include
)

# Link dependencies
ament_target_dependencies(turtle_stalker_node
        rclcpp
        turtlesim
        geometry_msgs
        )

# Install
install(TARGETS
        turtle_stalker_node
        DESTINATION lib/${PROJECT_NAME}
        )

# Export dependencies
ament_export_dependencies(rclcpp turtlesim geometry_msgs)
ament_package()
