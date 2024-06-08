import launch
import launch_ros.actions


def generate_launch_description():
    num_cycles = 2

    nodes = []

    # Add the turtlesim_node
    nodes.append(
        launch_ros.actions.Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim_node',
            output='screen'
        )
    )

    # Add the turtle_teleop_key node
    #nodes.append(
    #    launch_ros.actions.Node(
    #        package='turtlesim',
    #        executable='turtle_teleop_key',
    #        name='turtle_teleop_key',
    #        output='screen'
    #    )
    #)

    # Add turtle_stalker_node for each cycle
    for i in range(num_cycles):
        nodes.append(
            launch_ros.actions.Node(
                package='turtle_stalker',
                executable='turtle_stalker_node',
                name='turtle_stalker_node_{}'.format(i+1),
                output='screen',
                arguments=['1.0', 'turtle{}'.format(i+2), 'turtle{}'.format(i+1)]
            )
        )

    return launch.LaunchDescription(nodes)


if __name__ == "__main__":
    launch_description = generate_launch_description()
    print(launch_description)

