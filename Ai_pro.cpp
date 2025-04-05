// #include <iostream>
// #include <thread>
// #include <vector>
// #include <random>
// #include <GLFW/glfw3.h>

// // Struct to hold 3D data points
// struct Point3D {
//     float x, y, z;
// };

// // Container for all the points
// std::vector<Point3D> dataPoints;

// // Function to generate random data points
// void generateRandomData() {
//     std::random_device rd;
//     std::mt19937 gen(rd());
//     std::uniform_real_distribution<> dis(-1.0, 1.0);

//     while (true) {
//         Point3D point;
//         point.x = dis(gen);
//         point.y = dis(gen);
//         point.z = dis(gen);

//         // Protect shared resource with a mutex if needed
//         dataPoints.push_back(point);

//         // Simulate delay
//         std::this_thread::sleep_for(std::chrono::milliseconds(100));
//     }
// }

// // Function to render 3D graph using OpenGL and GLFW
// void renderGraph() {
//     if (!glfwInit()) {
//         std::cerr << "Failed to initialize GLFW" << std::endl;
//         return;
//     }

//     GLFWwindow* window = glfwCreateWindow(800, 600, "3D Visualization", nullptr, nullptr);
//     if (!window) {
//         std::cerr << "Failed to create GLFW window" << std::endl;
//         glfwTerminate();
//         return;
//     }

//     glfwMakeContextCurrent(window);

//     while (!glfwWindowShouldClose(window)) {
//         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
//         glLoadIdentity();

//         // Set up the 3D viewing
//         glTranslatef(0.0f, 0.0f, -5.0f);

//         // Render points
//         glBegin(GL_POINTS);
//         for (const auto& point : dataPoints) {
//             glVertex3f(point.x, point.y, point.z);
//         }
//         glEnd();

//         glfwSwapBuffers(window);
//         glfwPollEvents();

//         // Simulate delay for real-time rendering
//         std::this_thread::sleep_for(std::chrono::milliseconds(16)); // ~60 FPS
//     }

//     glfwDestroyWindow(window);
//     glfwTerminate();
// }

// int main(int argc, char** argv) {
//     // Start random data generation in a separate thread
//     std::thread dataThread(generateRandomData);

//     // Start rendering in the main thread
//     renderGraph();

//     dataThread.join();
//     return 0;
// }


// #include <iostream>
// #include <thread>
// #include <vector>
// #include <random>
// #include <chrono>
// #include <GLFW/glfw3.h>

// // Struct to hold 3D data points
// struct Point3D {
//     float x, y, z;
// };

// // Container for all the points
// std::vector<Point3D> dataPoints;

// // Function to generate random data points
// void generateRandomData() {
//     std::random_device rd;
//     std::mt19937 gen(rd());
//     std::uniform_real_distribution<> dis(-1.0, 1.0);

//     while (true) {
//         Point3D point;
//         point.x = dis(gen);
//         point.y = dis(gen);
//         point.z = dis(gen);

//         // Protect shared resource with a mutex if needed
//         dataPoints.push_back(point);

//         // Simulate delay
//         std::this_thread::sleep_for(std::chrono::milliseconds(100));
//     }
// }

// // Function to render 3D graph using OpenGL and GLFW
// void renderGraph() {
//     if (!glfwInit()) {
//         std::cerr << "Failed to initialize GLFW" << std::endl;
//         return;
//     }

//     GLFWwindow* window = glfwCreateWindow(800, 600, "3D Visualization", nullptr, nullptr);
//     if (!window) {
//         std::cerr << "Failed to create GLFW window" << std::endl;
//         glfwTerminate();
//         return;
//     }

//     glfwMakeContextCurrent(window);

//     while (!glfwWindowShouldClose(window)) {
//         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
//         glLoadIdentity();

//         // Set up the 3D viewing
//         glTranslatef(0.0f, 0.0f, -5.0f);

//         // Render points
//         glBegin(GL_POINTS);
//         for (const auto& point : dataPoints) {
//             glVertex3f(point.x, point.y, point.z);
//         }
//         glEnd();

//         glfwSwapBuffers(window);
//         glfwPollEvents();

//         // Simulate delay for real-time rendering
//         std::this_thread::sleep_for(std::chrono::milliseconds(16)); // ~60 FPS
//     }

//     glfwDestroyWindow(window);
//     glfwTerminate();
// }

// int main(int argc, char** argv) {
//     // Start random data generation in a separate thread
//     std::thread dataThread(generateRandomData);

//     // Start rendering in the main thread
//     renderGraph();

//     dataThread.join();
//     return 0;
// }

#include <iostream>
#include <thread>  // Required for std::thread
#include <chrono>  // Required for std::chrono and std::this_thread
#include <vector>
#include <random>
#include <GLFW/glfw3.h>

using namespace std;

// Struct to hold 3D data points
struct Point3D {
    float x, y, z;
};

// Container for all the points
std::vector<Point3D> dataPoints;

// Function to generate random data points
void generateRandomData() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(-1.0, 1.0);

    while (true) {
        Point3D point;
        point.x = dis(gen);
        point.y = dis(gen);
        point.z = dis(gen);

        dataPoints.push_back(point);

        // Simulate delay
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
}

// Function to render 3D graph using OpenGL and GLFW
void renderGraph() {
    if (!glfwInit()) {
        std::cerr << "Failed to initialize GLFW" << std::endl;
        return;
    }

    GLFWwindow* window = glfwCreateWindow(800, 600, "3D Visualization", nullptr, nullptr);
    if (!window) {
        std::cerr << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return;
    }

    glfwMakeContextCurrent(window);
    // Add these before your main render loop
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
    glEnable(GL_DEPTH_TEST);
    

    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        glLoadIdentity();

        // Set up the 3D viewing
        glTranslatef(0.0f, 0.0f, -5.0f);

        // Render points
        glBegin(GL_POINTS);
        for (const auto& point : dataPoints) {
            glVertex3f(point.x, point.y, point.z);
        }
        glEnd();

        glfwSwapBuffers(window);
        glfwPollEvents();

        // Simulate delay for real-time rendering
        std::this_thread::sleep_for(std::chrono::milliseconds(16)); // ~60 FPS
    }

    glfwDestroyWindow(window);
    glfwTerminate();
}

int main(int argc, char** argv) {
    // Start random data generation in a separate thread
    std::thread dataThread(generateRandomData);

    // Start rendering in the main thread
    renderGraph();

    dataThread.join();
    return 0;
}
