#pragma once

#include <string> // Include this for std::string

// Constants
const double PI = 3.14159;

// Function declarations
void printMessage(const std::string &message);
int add(int a, int b);
double circleArea(double radius);

// Class definition
class Calculator {
public:
    Calculator();
    double add(double a, double b);
    double multiply(double a, double b);
    double getLastResult() const; // Getter for lastResult
private:
    double lastResult;
};

