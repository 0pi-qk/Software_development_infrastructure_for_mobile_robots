#include "../include/turtle_stalker/Random.hpp"
#include <random>

double Random::get_rand_value_double(double min = 0, double max = 100) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> X(min, max);
    return X(gen);
}
