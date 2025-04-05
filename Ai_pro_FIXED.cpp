#include <iostream> // input/output
#include <vector>// dynamic array
#include <cmath>// math functions
#include <GLFW/glfw3.h> // OpenGL framework
#include <GL/glu.h> // OpenGL Utility Library


struct Neuron { // Neuron structure
    float x, y, z; // 3D coordinates
};

float sigmoid(float x) { // Sigmoid activation function
    return 1.0f / (1.0f + exp(-x)); // Sigmoid function
}

float feedForward(float input1, float input2) {// Feedforward function
    // Simple feedforward neural network simulation
    // Simulate a small feedforward network
    float hidden1 = sigmoid(input1 * 0.5f + input2 * 0.3f);// hidden layer neuron 1
    float hidden2 = sigmoid(input1 * 0.8f + input2 * 0.1f);// hidden layer neuron 2
    float output = sigmoid(hidden1 * 0.9f + hidden2 * 0.4f);// output layer neuron
    // Return the final output
    return output;
}

void drawNeuron(float x, float y, float z) {// Draw a neuron as a point in 3D space
    glPointSize(10.0f);// Set point size
    glBegin(GL_POINTS);// Begin drawing points
    glColor3f(0.2f, 1.0f, 0.2f); // green
    glVertex3f(x, y, z);// Set vertex position
    glEnd();// End drawing points
}

void drawConnection(const Neuron& from, const Neuron& to) {// Draw a connection between two neurons
    glColor3f(0.5f, 0.5f, 1.0f); // bluish
    glBegin(GL_LINES);// Begin drawing lines
    glVertex3f(from.x, from.y, from.z);// Set start vertex position
    glVertex3f(to.x, to.y, to.z);// Set end vertex position
    glEnd();// End drawing lines
}

void renderGraph() {// Render the neural network graphically
    // Initialize GLFW and create a window
    if (!glfwInit()) {// Initialize GLFW
        std::cerr << "Failed to initialize GLFW\n";// Check for initialization errors
        return;// Exit if initialization fails
    }

    GLFWwindow* window = glfwCreateWindow(800, 600, "Mini AI Graph", nullptr, nullptr);// Create a window
    if (!window) {// Check if window creation was successful
        glfwTerminate();// Terminate GLFW if window creation fails
        std::cerr << "Failed to create window\n";// Check for window creation errors
        return;
    }

    glfwMakeContextCurrent(window);// Make the window's context current

    // Setup OpenGL
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);// Set clear color
    glEnable(GL_DEPTH_TEST);// Enable depth testing
    glMatrixMode(GL_PROJECTION);// Set projection matrix mode
    glLoadIdentity();// Load identity matrix
    gluPerspective(45.0, 800.0/600.0, 0.1, 100.0);// Set perspective projection
    glMatrixMode(GL_MODELVIEW);// Set modelview matrix mode

    // Set up neurons
    std::vector<Neuron> inputLayer = {{-0.5f,  0.5f, 0.0f}, {0.5f, 0.5f, 0.0f}};// Input layer neurons
    std::vector<Neuron> hiddenLayer = {{-0.5f, 0.0f, 0.0f}, {0.5f, 0.0f, 0.0f}};// Hidden layer neurons
    std::vector<Neuron> outputLayer = {{0.0f, -0.5f, 0.0f}};// Output layer neurons

    while (!glfwWindowShouldClose(window)) {// Main loop
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);// Clear the screen
        glLoadIdentity();// Load identity matrix
        glTranslatef(0.0f, 0.0f, -3.0f); // move back to see the neurons

        // Draw connections
        for (auto& in : inputLayer)// Draw connections from input layer to hidden layer
            for (auto& h : hiddenLayer)// Draw connections from input layer to hidden layer
                drawConnection(in, h);// Draw connections from input layer to hidden layer
        for (auto& h : hiddenLayer)// Draw connections from hidden layer to output layer
            for (auto& o : outputLayer)// Draw connections from hidden layer to output layer
                drawConnection(h, o);// Draw connections from hidden layer to output layer

        // Draw neurons
        for (auto& n : inputLayer) drawNeuron(n.x, n.y, n.z);// Draw input layer neurons
        for (auto& n : hiddenLayer) drawNeuron(n.x, n.y, n.z);// Draw hidden layer neurons
        for (auto& n : outputLayer) drawNeuron(n.x, n.y, n.z);// Draw output layer neurons

        glfwSwapBuffers(window);// Swap buffers to display the rendered image
        glfwPollEvents();// Poll for events
    }

    glfwDestroyWindow(window);// Destroy the window
    glfwTerminate();// Terminate GLFW
}

int main() {// Main function
    int input1, input2;// Input values for the neural network
    std::cout << "Enter value for input1 (0 or 1): ";// Prompt for input1
    std::cin >> input1;// Read input1 from user
    std::cout << "Enter value for input2 (0 or 1): ";// Prompt for input2
    std::cin >> input2;// Read input2 from user

    float result = feedForward((float)input1, (float)input2);// Call the feedforward function with user inputs
    std::cout << "Final Output: " << result << std::endl;// Print the final output

    renderGraph();// Call the renderGraph function to display the neural network graphically

    return 0;// Return success
}// End of main function

