import matplotlib.pyplot as plt#Importing matplotlib module
import pandas as pd#Importing pandas module
import pylab as pl#Importing pylab module
import numpy as np#Importing numpy module
import seaborn as sns#Importing seaborn module
import itertools#Importing itertools module
import matplotlib.ticker as ticker#Importing ticker module from matplotlib
from sklearn import preprocessing#Importing preprocessing module from scikit learn
from sklearn import datasets, linear_model, metrics#Importing sklearn module
from sklearn.linear_model import LinearRegression#Importing LinearRegression module from sklearn
from sklearn.datasets import fetch_california_housing#Importing fetch_california_housing module from sklearn
from sklearn.model_selection import train_test_split#Importing train_test_split module from sklearn
from sklearn.metrics import r2_score#Importing r2_score module from sklearn
from sklearn.metrics import mean_squared_error#Importing mean_squared_error module from sklearn
from sklearn.metrics import mean_absolute_error#Importing mean_absolute_error module from sklearn
from sklearn.metrics import explained_variance_score#Importing explained_variance_score module from sklearn
from sklearn.model_selection import cross_val_score#Importing cross_val_score module from sklearn
from sklearn.model_selection import GridSearchCV#Importing GridSearchCV module from sklearn
from sklearn.metrics import classification_report#Importing classification_report module from sklearn
from sklearn.metrics import confusion_matrix#Importing confusion_matrix module from sklearn
from sklearn.metrics import accuracy_score#Importing accuracy_score module from sklearn
from sklearn.metrics import precision_score#Importing precision_score module from sklearn
from sklearn.metrics import recall_score#Importing recall_score module from sklearn
from sklearn.metrics import f1_score#Importing f1_score module from sklearn
from sklearn.metrics import roc_curve#Importing roc_curve module from sklearn
from sklearn.metrics import roc_auc_score#Importing roc_auc_score module from sklearn
from sklearn.metrics import log_loss#Importing log_loss module from sklearn
from sklearn.metrics import mean_poisson_deviance#Importing mean_poisson_deviance module from sklearn
from sklearn.metrics import mean_gamma_deviance#Importing mean_gamma_deviance module from sklearn
from sklearn.metrics import mean_tweedie_deviance#Importing mean_tweedie_deviance module from sklearn
from sklearn.metrics import mean_absolute_percentage_error#Importing mean_absolute_percentage_error module from sklearn
from sklearn.model_selection import train_test_split#Importing train_test_split module from sklearn
from sklearn.neighbors import KNeighborsClassifier#Importing KNeighborsClassifier module from sklearn
from sklearn.preprocessing import StandardScaler#Importing StandardScaler module from sklearn
from sklearn.tree import DecisionTreeRegressor#Importing DecisionTreeRegressor module from sklearn
from sklearn.tree import DecisionTreeClassifier#Importing DecisionTreeClassifier module from sklearn
#from sklearn.externals.six import StringIO##For Python 3 compatibility
import six #For Python 3 compatibility
from six import StringIO#For Python 3 compatibility
import pydotplus#For visualization of decision tree
import matplotlib.image as mpimg#For visualization of decision tree
from sklearn import tree#For visualization of decision tree
from sklearn.ensemble import RandomForestClassifier#Importing RandomForestClassifier module from sklearn
from sklearn.ensemble import RandomForestRegressor#Importing RandomForestRegressor module from sklearn
from sklearn.ensemble import GradientBoostingClassifier#Importing GradientBoostingClassifier module from sklearn
from sklearn.ensemble import GradientBoostingRegressor#Importing GradientBoostingRegressor module from sklearn
from sklearn.preprocessing import LabelEncoder#Importing LabelEncoder module from sklearn
from sklearn.preprocessing import OneHotEncoder#Importing OneHotEncoder module from sklearn
from sklearn.tree import plot_tree#Importing plot_tree module from sklearn
import pydot#For visualization of decision tree
from sklearn.tree import export_graphviz#Importing export_graphviz module from sklearn
from IPython.display import Image#Importing Image module from IPython.display for displaying images in Jupyter notebooks
from PIL import Image#Importing Image module from PIL for displaying images in Jupyter notebooks
from mpl_toolkits.mplot3d import Axes3D#Importing Axes3D module from mpl_toolkits.mplot3d
from tensorflow import keras#Importing keras module from tensorflow
from keras import layers#Importing layers module from tensorflow.keras
import time#Importing time module to record the execution time
from matplotlib.widgets import Button#Importing Button module from matplotlib.widgets



# Sample data
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

x2 = [1, 2, 3, 4, 5]
y2 = [1, 4, 9, 16, 25]

# Create scatter plot for the first data
plt.scatter(x1, y1, color='red', label='Data 1')

# Create scatter plot for the second data
plt.scatter(x2, y2, color='blue', label='Data 2')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Add legend
plt.legend()

# Show the plot
plt.show()
x1 = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y1 = np.array([2, 3, 5, 7, 11])

x2 = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y2 = np.array([1, 4, 9, 16, 25])

# Combine the data
X = np.vstack((x1, x2))
y = np.concatenate((y1, y2))

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Print the coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
# Sample data
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 3, 5, 7, 11])

x2 = np.array([1, 2, 3, 4, 5])
y2 = np.array([1, 4, 9, 16, 25])

# Combine the data
X = np.vstack((x1, x2))
y = np.concatenate((y1, y2))

# Create and train the linear regression model
model = LinearRegression()
model.fit(X.reshape(-1, 1), y)

# Generate points for the circle
theta = np.linspace(0, 2*np.pi, 100)
r = 10  # radius of the circle

# Plot the circle
plt.figure(figsize=(8, 8))
plt.plot(r * np.cos(theta), r * np.sin(theta), color='black')

# Plot the data points
plt.scatter(x1, y1, color='red', label='Data 1')
plt.scatter(x2, y2, color='blue', label='Data 2')

# Plot the regression line
x_values = np.array([0, 5])  # assuming x-axis range from 0 to 5
y_values = model.predict(x_values.reshape(-1, 1))
plt.plot(x_values, y_values, color='green', linestyle='--', label='Regression Line')

# Set aspect ratio to equal for circle
plt.gca().set_aspect('equal', adjustable='box')

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot on a Circle')

# Add legend
plt.legend()

# Show the plot
plt.show()

# Sample data
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 3, 5, 7, 11])
z1 = np.array([10, 20, 30, 40, 50])

x2 = np.array([1, 2, 3, 4, 5])
y2 = np.array([1, 4, 9, 16, 25])
z2 = np.array([100, 200, 300, 400, 500])

# Combine the data
X = np.vstack((x1, x2))
y = np.concatenate((y1, y2))
Z = np.vstack((z1, z2))

# Create and train the linear regression model
model = LinearRegression()
model.fit(np.hstack((X.reshape(-1, 1), Z.reshape(-1, 1))), y)

# Generate points for the circle
theta = np.linspace(0, 2*np.pi, 100)
r = 10  # radius of the circle

# Plot the circle
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot(r * np.cos(theta), r * np.sin(theta), np.zeros_like(theta), color='black')

# Plot the data points
ax.scatter(x1, y1, z1, color='red', label='Data 1')
ax.scatter(x2, y2, z2, color='blue', label='Data 2')

# Plot the regression line
x_values = np.linspace(0, 5, 100)
z_values = np.linspace(0, 500, 100)
X_values, Z_values = np.meshgrid(x_values, z_values)
Y_values = model.predict(np.hstack((X_values.reshape(-1, 1), Z_values.reshape(-1, 1)))).reshape(X_values.shape)
ax.plot_surface(X_values, Y_values, Z_values, color='green', alpha=0.2, label='Regression Surface')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Scatter Plot on a Circle')

# Add legend
ax.legend()

# Show the plot
plt.show()

# Generate initial training data
num_samples = 1000
X_train = np.random.rand(num_samples, 3)  # Assume 3 sensor readings/features
y_train = np.sum(X_train, axis=1) + np.random.randn(num_samples)  # Simulate target values

# Define the deep neural network model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(3,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)  # Output layer for regression
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the initial model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Initialize the live-changing 3D graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set black background
ax.set_facecolor('black')

# Function to update the 3D scatter plot
def update_plot(x, y_true, y_pred):
    ax.clear()
    ax.scatter(x[:, 0], x[:, 1], y_true, color='blue', label='True')  # True values
    ax.scatter(x[:, 0], x[:, 1], y_pred, color='red', label='Predicted')  # Predicted values
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_zlabel('Target')
    ax.set_title('Live-Changing 3D Graph')
    ax.legend()

# Function to handle stop button click event
def stop_button_clicked(event):
    global stop_program
    stop_program = True

# Create stop button
stop_button_ax = plt.axes([0.85, 0.05, 0.1, 0.075])
stop_button = Button(stop_button_ax, 'Stop')
stop_button.on_clicked(stop_button_clicked)

# Real-time inference and visualization
stop_program = False
while not stop_program:
    # Simulate new streaming data (randomly generated for demonstration)
    X_new = np.random.rand(10, 3)  # Assume 10 new samples arrive
    y_true_new = np.sum(X_new, axis=1) + np.random.randn(10)  # Simulate true values for new data

    # Predict using the updated model
    y_pred_new = model.predict(X_new)

    # Update the 3D scatter plot
    update_plot(X_new, y_true_new, y_pred_new)

    # Add delay
    plt.pause(0.1)

plt.show()

