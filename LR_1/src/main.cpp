#include "../include/turtle_stalker/ROS_commands.hpp"
#include "../include/turtle_stalker/Random.hpp"

int main(int argc, char** argv) {
    rclcpp::init(argc, argv);

    if (argc != 4) {
        RCLCPP_ERROR(rclcpp::get_logger("main"), "Usage: turtle_stalker_node <turtle_speed> <stalker_turtle_name> <target_turtle_name>");
        return 1;
    }

    double turtleSpeed = atof(argv[1]);
    std::string stalkerTurtleName = argv[2];
    std::string targetTurtleName = argv[3];

    Turtle targetTurtle(targetTurtleName);
    Turtle stalkerTurtle(
        Random::get_rand_value_double(0, 11),
        Random::get_rand_value_double(0, 11),
        0.0,
        0.0,
        0.0,
        stalkerTurtleName,
        turtleSpeed
    );

    auto ros_com = std::make_shared<ROS_commands>(targetTurtle, stalkerTurtle);
    ros_com->spawnTurtle();

    rclcpp::Rate rate(60);
    while (rclcpp::ok()) {
        ros_com->movePublishStalker();
        rclcpp::spin_some(ros_com);
        rate.sleep();
    }

    rclcpp::shutdown();
    return 0;
}
