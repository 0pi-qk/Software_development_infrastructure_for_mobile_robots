#ifndef TURTLE_STALKER_TURTLE_HPP
#define TURTLE_STALKER_TURTLE_HPP

#include <cmath>
#include <string>
#include <memory>


class Turtle {
private:
    double x = 0.0;
    double y = 0.0;
    double theta = 0.0;
    double linear_velocity = 0.0;
    double angular_velocity = 0.0;

    std::string turtleName;

    double turtleSpeed = 0.0;
    double linear_x = 0.0;
    double angular_z = 0.0;

public:
    Turtle(std::string);
    Turtle(double, double, double, double, double, std::string, double);

    void move(Turtle&);

    void update_position(double, double, double, double, double);

    double get_x();
    double get_y();
    double get_theta();
    std::string get_turtleName();
    double get_linear_x();
    double get_angular_z();
};


#endif
