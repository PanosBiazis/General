#include <stdio.h>
#include <math.h>

#define LEARNING_RATE 0.1
#define EPOCHS 10

// Activation function
double activation(double sum) {
    return sum > 0 ? 1 : 0;
}

// Perceptron training function
void perceptron(double weights[], double bias, double inputs[], int length, double target) {
    double sum = 0;

    // Calculate weighted sum
    for (int i = 0; i < length; i++) {
        sum += weights[i] * inputs[i];
    }

    // Add bias to the sum
    sum += bias;

    // Get perceptron output
    double output = activation(sum);

    // Calculate error
    double error = target - output;

    // Update weights and bias
    for (int i = 0; i < length; i++) {
        weights[i] += LEARNING_RATE * error * inputs[i];
    }
    bias += LEARNING_RATE * error;

    // Verbose output
    printf("Updated weights: ");
    for (int i = 0; i < length; i++) {
        printf("%f ", weights[i]);
    }
    printf(" | Bias: %f | Error: %f\n", bias, error);
}

int main() {
    // Initialize weights and bias
    double weights[] = {0.2, 0.3};
    double bias = 0.1;
    
    // Training data: inputs and corresponding targets
    double inputs[][2] = {
        {1, 0},
        {0, 1},
        {1, 1},
        {0, 0}
    };
    double targets[] = {1, 1, 0, 0};

    int num_samples = sizeof(targets) / sizeof(targets[0]);
    int num_inputs = sizeof(inputs[0]) / sizeof(inputs[0][0]);

    // Training loop
    for (int epoch = 0; epoch < EPOCHS; epoch++) {
        printf("Epoch %d\n", epoch + 1);
        for (int i = 0; i < num_samples; i++) {
            perceptron(weights, bias, inputs[i], num_inputs, targets[i]);
        }
        printf("\n");
    }

    // Final weights and bias
    printf("Final weights: ");
    for (int i = 0; i < num_inputs; i++) {
        printf("%f ", weights[i]);
    }
    printf(" | Final bias: %f\n", bias);

    return 0;
}
