#include "../include/turtle_stalker/Turtle.hpp"

Turtle::Turtle(std::string turtleName_) {
    turtleName = turtleName_;
}

Turtle::Turtle(double x_, double y_, double theta_, double linear_velocity_, double angular_velocity_, std::string turtleName_, double turtleSpeed_) {
    x = x_;
    y = y_;
    theta = theta_;
    linear_velocity = linear_velocity_;
    angular_velocity = angular_velocity_;
    turtleName = turtleName_;
    turtleSpeed = turtleSpeed_;
}

void Turtle::move(Turtle &targetTurtle) {
    // Вычисляем угол и расстояние до преследуемой черепахи
    double dx = targetTurtle.get_x()-x;
    double dy = targetTurtle.get_y()-y;
    double distance = sqrt(dx * dx + dy * dy);
    double target_angle = atan2(dy, dx);

    // Команды для движения
    linear_x = turtleSpeed * distance;
    angular_z = 4 * (atan2(sin(target_angle - theta), cos(target_angle - theta)));
}

void Turtle::update_position(double x_, double y_, double theta_, double linear_velocity_, double angular_velocity_) {
    x = x_;
    y = y_;
    theta = theta_;
    linear_velocity = linear_velocity_;
    angular_velocity = angular_velocity_;
}

double Turtle::get_x() {
    return x;
}

double Turtle::get_y() {
    return y;
}

double Turtle::get_theta() {
    return theta;
}

std::string Turtle::get_turtleName() {
    return turtleName;
}

double Turtle::get_linear_x() {
    return linear_x;
}

double Turtle::get_angular_z() {
    return angular_z;
}
