// #include <iostream>
// #include "example.hpp"

// // Function implementations
// void printMessage(const std::string &message) {
//     std::cout << message << std::endl;
// }

// int add(int a, int b) {
//     return a + b;
// }

// double circleArea(double radius) {
//     return PI * radius * radius;
// }

// // Class implementations
// Calculator::Calculator() : lastResult(0) {}

// double Calculator::add(double a, double b) {
//     lastResult = a + b;
//     return lastResult;
// }

// double Calculator::multiply(double a, double b) {
//     lastResult = a * b;
//     return lastResult;
// }


// int main() {
//     printMessage("Hello, World!");
//     int result = add(5, 3);
//     std::cout << "5 + 3 = " << result << std::endl;
//     double area = circleArea(5.0);
//     std::cout << "Area of a circle with radius 5 is " << area << std::endl;
//     Calculator calc;
//     calc.add(5.0, 3.0);
//     calc.multiply(5.0, 3.0);
//     std::cout << "Last result: " << calc.lastResult << std::endl;
//     return 0;
// }

#include <iostream>
#include "example.hpp"

// Function implementations
void printMessage(const std::string &message) {
    std::cout << message << std::endl;
}

int add(int a, int b) {
    return a + b;
}

double circleArea(double radius) {
    return PI * radius * radius;
}

// Class implementations
Calculator::Calculator() : lastResult(0) {}

double Calculator::add(double a, double b) {
    lastResult = a + b;
    return lastResult;
}

double Calculator::multiply(double a, double b) {
    lastResult = a * b;
    return lastResult;
}

double Calculator::getLastResult() const {
    return lastResult;
}


int main() {
    printMessage("Hello, World!");
    int result = add(5, 3);
    std::cout << "5 + 3 = " << result << std::endl;
    double area = circleArea(5.0);
    std::cout << "Area of a circle with radius 5 is " << area << std::endl;
    Calculator calc;
    calc.add(5.0, 3.0);
    calc.multiply(5.0, 3.0);
    std::cout << "Last result: " << calc.getLastResult() << std::endl;
    return 0;
}