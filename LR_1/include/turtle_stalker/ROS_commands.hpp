#ifndef TURTLE_STALKER_ROS_COMMANDS_HPP
#define TURTLE_STALKER_ROS_COMMANDS_HPP

#include "Turtle.hpp"
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "turtlesim/msg/pose.hpp"
#include "turtlesim/srv/spawn.hpp"

class ROS_commands : public rclcpp::Node {
private:
    rclcpp::Client<turtlesim::srv::Spawn>::SharedPtr spawnClient;
    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr poseSubStalker;
    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr poseSubTarget;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr velPub;

    Turtle &targetTurtle;
    Turtle &stalkerTurtle;

public:
    ROS_commands(Turtle&, Turtle&);

    void spawnTurtle();

    void movePublishStalker();

    void poseCallbackStalker(const turtlesim::msg::Pose::SharedPtr);
    void poseCallbackTarget(const turtlesim::msg::Pose::SharedPtr);
};

#endif
