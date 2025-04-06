import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load MNIST data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess the data
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

train_images, test_images = train_images / 255.0, test_images / 255.0

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.1)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc}")


# 1. Importing Libraries
# python
# Copy code
# import tensorflow as tf
# from tensorflow.keras import layers, models
# from tensorflow.keras.datasets import mnist
# from tensorflow.keras.utils import to_categorical
# tensorflow: This is the main deep learning framework we are using. tensorflow provides tools to build and train machine learning models, particularly deep learning models.
# layers: This module contains different types of layers that can be used to build neural networks. Layers like Conv2D, MaxPooling2D, Dense, etc., are imported here.
# models: This module contains the model-building utilities, like Sequential, which is used to define the architecture of the neural network.
# mnist: This is the dataset used in the code. The mnist dataset contains images of handwritten digits (0 to 9).
# to_categorical: This function is used to convert class labels (like 0, 1, 2...) into one-hot encoded vectors, which is necessary for classification problems in deep learning.
# 2. Loading the MNIST Dataset
# python
# Copy code
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# mnist.load_data(): This function loads the MNIST dataset. It returns two tuples:
# (train_images, train_labels): The training set images and their corresponding labels.
# (test_images, test_labels): The test set images and their corresponding labels.
# The images are 28x28 pixel grayscale images, and the labels are integers (0-9), representing the digit in each image.

# 3. Preprocessing the Data
# python
# Copy code
# train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
# test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# train_images, test_images = train_images / 255.0, test_images / 255.0
# Reshaping:
# The original shape of train_images and test_images is (num_samples, 28, 28), where num_samples is the number of images in the dataset.
# We reshape them to (num_samples, 28, 28, 1), adding a "channel" dimension (1 for grayscale images). This step is necessary because Keras expects the input to have the shape (height, width, channels).
# Normalization:
# The pixel values in the MNIST images are integers between 0 and 255. To help the model learn faster and more effectively, we normalize the pixel values by dividing them by 255. This scales the pixel values to the range [0, 1], making the training process more stable.
# 4. One-Hot Encoding the Labels
# python
# Copy code
# train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)
# to_categorical:
# The labels (the digits 0-9) are originally integers, but for training a neural network in a multi-class classification problem, they need to be converted to one-hot encoded vectors.
# For example, the label 3 becomes [0, 0, 0, 1, 0, 0, 0, 0, 0, 0] (a vector where only the 4th element is 1).
# This is because the output layer of the model will have 10 units (one for each digit), and each output corresponds to a one-hot vector.

# 5. Building the Convolutional Neural Network (CNN) Model
# python
# Copy code
# model = models.Sequential([
#     layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
#     layers.MaxPooling2D((2, 2)),
#     layers.Conv2D(64, (3, 3), activation='relu'),
#     layers.MaxPooling2D((2, 2)),
#     layers.Conv2D(64, (3, 3), activation='relu'),
#     layers.Flatten(),
#     layers.Dense(64, activation='relu'),
#     layers.Dense(10, activation='softmax')
# ])
# Here we are defining the model using a Sequential model, which is a linear stack of layers.

# Conv2D: This is a convolutional layer that detects patterns in the input images.

# 32 and 64 are the number of filters used in these layers, meaning the layer will output 32 or 64 different feature maps (one for each filter).
# (3, 3) is the size of the convolutional filter (kernel), which is a 3x3 window that slides across the image.
# activation='relu' specifies the activation function used after the convolution, which is the Rectified Linear Unit (ReLU). ReLU introduces non-linearity to the model and helps it learn complex patterns.
# input_shape=(28, 28, 1) specifies the shape of the input images (28x28 pixels, 1 channel for grayscale).
# MaxPooling2D: This is a pooling layer that reduces the spatial dimensions of the feature maps, making the model more efficient.

# (2, 2) means the pooling operation takes a 2x2 window and outputs the maximum value within that window, effectively reducing the size of the feature map by half.
# Flatten: This layer flattens the 3D feature maps from the convolutional layers into a 1D vector, which is necessary before passing the data to fully connected layers (Dense layers).

# Dense: These are fully connected layers.

# The first dense layer has 64 units and uses ReLU as the activation function.
# The second dense layer has 10 units and uses softmax as the activation function. Softmax is used for multi-class classification because it converts the network's output into probabilities (the sum of all outputs will be 1, each output representing the probability of the input belonging to one of the 10 classes).
# 6. Compiling the Model
# python
# Copy code
# model.compile(optimizer='adam',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])
# optimizer='adam': The optimizer is responsible for adjusting the weights of the model during training. Adam is a popular optimizer because it adapts the learning rate based on the gradients, making the training process faster and more efficient.

# loss='categorical_crossentropy': This is the loss function used for multi-class classification problems. It measures how well the model's predicted probabilities match the actual labels.

# metrics=['accuracy']: We are interested in tracking the accuracy of the model during training, so we specify accuracy as a metric.

# 7. Training the Model
# python
# Copy code
# model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.1)
# fit: This is where the model starts training on the data.
# train_images and train_labels: The training data and their corresponding labels.
# epochs=5: The number of times the entire dataset will be passed through the network. Each pass is called an epoch.
# batch_size=64: The number of samples the model will process before updating the weights. A smaller batch size can make the model more accurate but slower, while a larger batch size speeds up the process but might reduce accuracy.
# validation_split=0.1: This splits 10% of the training data to be used for validation during training. The validation data is not used for training but helps monitor the model's performance.
# 8. Evaluating the Model
# python
# Copy code
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print(f"Test accuracy: {test_acc}")
# evaluate: This evaluates the model's performance on the test data.

# test_images and test_labels: The test data and their corresponding labels.
# The function returns the loss and accuracy for the test dataset.
# The accuracy of the model on the test set is printed.

# Summary
# The code uses Convolutional Neural Networks (CNNs), which are effective for image classification tasks.
# The model is trained on the MNIST dataset, which contains images of handwritten digits.
# The dataset is preprocessed by reshaping the images and normalizing the pixel values.
# The model is a CNN with convolutional layers, max-pooling layers, and fully connected layers.
# The training process uses the Adam optimizer and categorical crossentropy loss, which are typical choices for multi-class classification problems.
# After training, the model's performance is evaluated on a test set, and the accuracy is printed.

# import tensorflow as tf
# from tensorflow.keras import layers, models
# from tensorflow.keras.datasets import mnist
# from tensorflow.keras.utils import to_categorical

# Load MNIST data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess data
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))
train_images, test_images = train_images / 255.0, test_images / 255.0
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build a simple neural network
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),  # Flatten the 28x28 image into a 1D vector
    layers.Dense(128, activation='relu'),  # Fully connected layer with 128 neurons and ReLU activation
    layers.Dense(10, activation='softmax')  # Output layer with 10 neurons (for 10 digits) and softmax activation
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5, batch_size=64)

# Evaluate the model on test data
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc}")


# explaination:
# This code creates and trains a simple neural network (a type of artificial neural network, or ANN) for classifying handwritten digits from the MNIST dataset using Keras, which is a high-level API built on top of TensorFlow.

# Step-by-Step Explanation:
# 1. Importing Required Libraries
# python
# Copy code
# import tensorflow as tf
# from tensorflow.keras import layers, models
# from tensorflow.keras.datasets import mnist
# from tensorflow.keras.utils import to_categorical
# tensorflow: This is the main deep learning framework. Keras is included in TensorFlow as the high-level API, so it’s essential to import it.

# layers: This module contains different types of layers you can use to build a neural network (e.g., Dense, Flatten, Conv2D).

# models: This is used to define the architecture of the neural network. It provides Sequential, which is a model where you stack layers on top of each other in a linear fashion.

# mnist: The MNIST dataset is a famous dataset that contains 28x28 grayscale images of handwritten digits (0-9), used to train and evaluate image classification models.

# to_categorical: This function is used to convert class labels (e.g., the digits 0, 1, 2, etc.) into one-hot encoded vectors. This is needed because the output layer of the neural network will use softmax activation, which outputs probabilities for each class.

# 2. Loading the MNIST Dataset
# python
# Copy code
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# mnist.load_data() loads the MNIST dataset.
# train_images: This is a NumPy array containing the training images. It has the shape (60000, 28, 28), where 60000 is the number of training images and 28x28 is the image size.
# train_labels: This is a NumPy array of shape (60000,) containing the corresponding labels (digits 0-9) for the training images.
# test_images: This is a NumPy array containing 10000 test images of shape (10000, 28, 28).
# test_labels: This is a NumPy array of shape (10000,) containing the labels for the test images.
# 3. Preprocessing the Data
# python
# Copy code
# train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
# test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# train_images, test_images = train_images / 255.0, test_images / 255.0
# Reshaping:

# The original shape of train_images and test_images is (num_samples, 28, 28). These are grayscale images, so they have one channel.
# We reshape the images to (num_samples, 28, 28, 1), where 1 represents the number of channels (grayscale). This format is necessary because Keras expects image data to be in the form (height, width, channels).
# Normalization:

# The pixel values in the MNIST images range from 0 to 255 (since it's 8-bit grayscale).
# We normalize the pixel values by dividing them by 255.0, which scales them to the range [0, 1]. This helps improve training speed and stability.
# 4. One-Hot Encoding the Labels
# python
# Copy code
# train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)
# One-Hot Encoding:
# The labels in train_labels and test_labels are integers (0 to 9). For example, if the label is 3, it would be represented as 3 in the dataset.
# However, the output layer of the neural network will have 10 units (for digits 0 through 9), and each unit will correspond to a class.
# One-hot encoding converts each label into a vector of length 10, with all values set to 0 except for the index corresponding to the correct class.
# For example, the label 3 would become [0, 0, 0, 1, 0, 0, 0, 0, 0, 0].
# This is necessary for categorical classification, where the model predicts the probability of each class, and the loss function expects one-hot encoded vectors.

# 5. Building the Neural Network Model
# python
# Copy code
# model = models.Sequential([
#     layers.Flatten(input_shape=(28, 28, 1)),  # Flatten the 28x28 image into a 1D vector
#     layers.Dense(128, activation='relu'),  # Fully connected layer with 128 neurons and ReLU activation
#     layers.Dense(10, activation='softmax')  # Output layer with 10 neurons (for 10 digits) and softmax activation
# ])
# Sequential Model:

# We define the neural network using models.Sequential(). This type of model allows you to stack layers one after the other in a linear fashion.
# Flatten Layer:

# The input images are 28x28 pixels, but the neural network expects a 1D vector as input for dense layers. The Flatten layer converts the 2D array of pixels into a 1D vector.
# The input_shape=(28, 28, 1) specifies that the input data has the shape (28, 28, 1), which is a 28x28 image with 1 channel (grayscale).
# Dense Layer (Hidden Layer):

# The Dense layer represents a fully connected layer. Every neuron in this layer is connected to all neurons in the previous layer.
# 128: The number of neurons in this hidden layer. The larger the number of neurons, the more complex the model can be, but it also increases the computational cost.
# activation='relu': The activation function used is ReLU (Rectified Linear Unit), which is commonly used in hidden layers because it helps the model learn more complex patterns and prevents issues like vanishing gradients.
# Dense Layer (Output Layer):

# The final Dense layer has 10 neurons (one for each possible digit, 0 through 9).
# activation='softmax': The softmax activation function is used in the output layer for multi-class classification. It converts the raw output scores into probabilities, with the sum of all probabilities equal to 1. The model will output a probability for each class (0 to 9), and the class with the highest probability will be chosen as the predicted label.
# 6. Compiling the Model
# python
# Copy code
# model.compile(optimizer='adam',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])
# optimizer='adam':
# The optimizer is responsible for adjusting the weights of the neural network during training. Adam (short for Adaptive Moment Estimation) is a popular optimizer because it combines the advantages of two other optimizers, AdaGrad and RMSProp, and adapts the learning rate during training.
# loss='categorical_crossentropy':
# The loss function measures how well the model's predictions match the true labels. For a multi-class classification problem, categorical crossentropy is commonly used.
# It calculates the difference between the predicted probabilities and the true labels (which are one-hot encoded).
# metrics=['accuracy']:
# This specifies that the metric we care about during training is accuracy. The model's performance will be measured by how many correct predictions it makes.
# 7. Training the Model
# python
# Copy code
# model.fit(train_images, train_labels, epochs=5, batch_size=64)
# fit:
# This function trains the model on the training data (train_images and train_labels).
# epochs=5:
# An epoch refers to one complete pass through the entire training dataset. The model will be trained for 5 epochs, meaning it will process the training data 5 times.
# batch_size=64:
# The model is trained using batches of data. Instead of passing all the data at once, the model processes 64 images at a time, updating the weights after each batch. This is more memory-efficient and can speed up training.
# 8. Evaluating the Model
# python
# Copy code
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print(f"Test accuracy: {test_acc}")
# evaluate:

# After training, we evaluate the model on the test data (test_images and test_labels) to see how well it performs on unseen data.
# The function returns two values:

# test_loss: The loss on the test set (similar to the loss on the training set, but on unseen data).
# test_acc: The accuracy on the test set (the percentage of correct predictions).
# print(f"Test accuracy: {test_acc}"):

# The accuracy is printed to the console to give us an idea of how well the model generalizes to new, unseen data.
# Summary of the Code:
# We build a simple feedforward neural network (also called a multi-layer perceptron) using Keras.
# The neural network is trained on the MNIST dataset of handwritten digits.
# The model has:
# An input layer that flattens the 28x28 images into 1D vectors.
# A hidden layer with 128 neurons and ReLU activation.
# An output layer with 10 neurons, each representing one of the digits 0-9, using softmax for classification.
# The model is trained using Adam optimizer and categorical crossentropy loss.
# Finally, the model's accuracy on the test data is evaluated and printed.
# This simple neural network can classify handwritten digits with high accuracy after training. Let me know if you'd like further details on any specific part of the code!