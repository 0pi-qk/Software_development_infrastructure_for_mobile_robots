#include "../include/turtle_stalker/ROS_commands.hpp"

ROS_commands::ROS_commands(Turtle &targetTurtle_, Turtle &stalkerTurtle_) :
        Node("turtle_stalker_node"),
        targetTurtle(targetTurtle_),
        stalkerTurtle(stalkerTurtle_) {
    spawnClient = create_client<turtlesim::srv::Spawn>("/spawn");
    poseSubStalker = create_subscription<turtlesim::msg::Pose>("/" + stalkerTurtle.get_turtleName() + "/pose", 10, std::bind(&ROS_commands::poseCallbackStalker, this, std::placeholders::_1));
    poseSubTarget = create_subscription<turtlesim::msg::Pose>("/" + targetTurtle.get_turtleName() + "/pose", 10, std::bind(&ROS_commands::poseCallbackTarget, this, std::placeholders::_1));
    velPub = create_publisher<geometry_msgs::msg::Twist>("/" + stalkerTurtle.get_turtleName() + "/cmd_vel", 10);
}

void ROS_commands::spawnTurtle() {
    auto request = std::make_shared<turtlesim::srv::Spawn::Request>();
    request->x = stalkerTurtle.get_x();
    request->y = stalkerTurtle.get_y();
    request->name = stalkerTurtle.get_turtleName();
    request->theta = stalkerTurtle.get_theta();
    spawnClient->async_send_request(request);
}

void ROS_commands::movePublishStalker() {
    stalkerTurtle.move(targetTurtle);

    auto velMsg = std::make_unique<geometry_msgs::msg::Twist>();
    velMsg->linear.x = stalkerTurtle.get_linear_x();
    velMsg->angular.z = stalkerTurtle.get_angular_z();

    velPub->publish(std::move(velMsg));
}

void ROS_commands::poseCallbackStalker(const turtlesim::msg::Pose::SharedPtr msg) {
    stalkerTurtle.update_position(
            msg->x,
            msg->y,
            msg->theta,
            msg->linear_velocity,
            msg->angular_velocity
    );
}

void ROS_commands::poseCallbackTarget(const turtlesim::msg::Pose::SharedPtr msg) {
    targetTurtle.update_position(
            msg->x,
            msg->y,
            msg->theta,
            msg->linear_velocity,
            msg->angular_velocity
    );
}
