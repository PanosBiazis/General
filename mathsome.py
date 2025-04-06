import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, integrate
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Numerical Computation (Like MATLAB)
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()


# Symbolic Computation (Like Mathematica)
x = symbols('x')
expr = x**2 + 3*x + 2

derivative = diff(expr, x)  # Differentiation
integral = integrate(expr, x)  # Integration

print(f"Derivative: {derivative}")
print(f"Integral: {integral}")



# 3D Colorful Graph

# Create a grid of points (X, Y)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Define the Z values based on some function of X and Y
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot a 3D surface with color mapping
surface = ax.plot_surface(X, Y, Z, cmap='viridis')

# Add a color bar to map the colors to Z values
fig.colorbar(surface)

# Add labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Show the plot
plt.show()



# Explanation:
# np.linspace(-5, 5, 100) creates 100 points between -5 and 5 for both the X and Y axes.
# np.meshgrid(x, y) creates a grid of points in the XY plane.
# Z = np.sin(np.sqrt(X**2 + Y**2)) defines the Z-values as a function of X and Y, creating a surface that looks like waves.
# plot_surface() creates the 3D surface, and cmap='viridis' applies a color map to make it colorful.
# # fig.colorbar(surface) adds a color bar that shows how the colors correspond to Z values.


# Define parameters
g = 9.81  # gravity (m/s^2)
v0 = 50   # initial velocity (m/s)
theta = np.radians(45)  # launch angle in radians

# Time of flight
t_flight = 2 * v0 * np.sin(theta) / g

# Time intervals
t = np.linspace(0, t_flight, num=500)

# Equations of motion
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Plotting the trajectory
plt.plot(x, y)
plt.title('Projectile motion under gravity')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.show()

# This code simulates and visualizes the motion of a projectile in 2D, using basic physics equations. Similar approaches can be applied to solve more complex problems.




# # import numpy as np
# # import matplotlib.pyplot as plt
# # from mpl_toolkits.mplot3d import Axes3D

# # Function to generate and display random 3D surface plot
# def generate_random_3d_plot():
#     # Create a new figure for the 3D plot
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
    
#     # Create random data for the plot
#     x = np.linspace(-5, 5, 100)
#     y = np.linspace(-5, 5, 100)
#     X, Y = np.meshgrid(x, y)
    
#     # Generate random Z values for a random surface
#     Z = np.sin(np.sqrt(X**2 + Y**2)) + np.random.rand(*X.shape) * 2 - 1

#     # Plot the surface with a random colormap
#     surface = ax.plot_surface(X, Y, Z, cmap=np.random.choice(['viridis', 'plasma', 'inferno', 'coolwarm', 'spring', 'summer', 'winter']))

#     # Add a color bar
#     fig.colorbar(surface)

#     # Clear the current canvas and draw the new plot
#     canvas.get_tk_widget().pack_forget()
#     canvas._tkcanvas.pack_forget()

#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack()

# # Create the main window
# root = tk.Tk()
# root.title("Random 3D Colorful Graph Generator")

# # Create a frame for the plot
# frame = tk.Frame(root)
# frame.pack()

# # Create the initial plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# canvas = FigureCanvasTkAgg(fig, master=frame)
# canvas.draw()
# canvas.get_tk_widget().pack()

# # Create the button to generate a new random plot
# button = tk.Button(root, text="Generate Random 3D Graph", command=generate_random_3d_plot)
# button.pack()

# # Start the Tkinter event loop
# root.mainloop()


# # Define canvas as a global variable
# canvas = None

# # Function to generate and display random 3D surface plot
# def generate_random_3d_plot():
#     global canvas  # Indicate that we are using the global 'canvas' variable
    
#     # Create a new figure for the 3D plot
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
    
#     # Create random data for the plot
#     x = np.linspace(-5, 5, 100)
#     y = np.linspace(-5, 5, 100)
#     X, Y = np.meshgrid(x, y)
    
#     # Generate random Z values for a random surface
#     Z = np.sin(np.sqrt(X**2 + Y**2)) + np.random.rand(*X.shape) * 2 - 1

#     # Plot the surface with a random colormap
#     surface = ax.plot_surface(X, Y, Z, cmap=np.random.choice(['viridis', 'plasma', 'inferno', 'coolwarm', 'spring', 'summer', 'winter']))

#     # Add a color bar
#     fig.colorbar(surface)

#     # If a previous plot exists, clear it from the window
#     if canvas:
#         canvas.get_tk_widget().pack_forget()
#         canvas._tkcanvas.pack_forget()

#     # Create a new canvas for the updated plot
#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack()

# # Create the main window
# root = tk.Tk()
# root.title("Random 3D Colorful Graph Generator")

# # Create a frame for the plot
# frame = tk.Frame(root)
# frame.pack()

# # Initial placeholder plot (empty)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# canvas = FigureCanvasTkAgg(fig, master=frame)
# canvas.draw()
# canvas.get_tk_widget().pack()

# # Create the button to generate a new random plot
# button = tk.Button(root, text="Generate Random 3D Graph", command=generate_random_3d_plot)
# button.pack()

# # Start the Tkinter event loop
# root.mainloop()





# Global variable for canvas
# canvas = None

# # Function to generate and display random 3D surface plot
# def generate_random_3d_plot():
#     global canvas  # Access global canvas variable
    
#     # Create a new figure for the 3D plot
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
    
#     # Create random data for the plot
#     x = np.linspace(-5, 5, 100)
#     y = np.linspace(-5, 5, 100)
#     X, Y = np.meshgrid(x, y)

#     # Define a list of 100 different mathematical functions for Z
#     functions = [
#         np.sin(np.sqrt(X**2 + Y**2)),
#         np.cos(np.sqrt(X**2 + Y**2)),
#         np.sin(X) * np.cos(Y),
#         np.sin(X) + np.cos(Y),
#         X**2 - Y**2,
#         np.tan(np.sqrt(X**2 + Y**2)),
#         np.sin(X**2) + np.cos(Y**2),
#         np.sinh(X) + np.cosh(Y),
#         np.log(X**2 + Y**2 + 1),
#         np.exp(-X**2 - Y**2),
#         X * np.sin(Y),
#         Y * np.cos(X),
#         X**2 + Y**2,
#         X**3 - Y**3,
#         np.abs(np.sin(X)) + np.abs(np.cos(Y)),
#         np.tanh(X) + np.tanh(Y),
#         X**4 - Y**4,
#         X**2 + Y**2 - np.sin(np.sqrt(X**2 + Y**2)),
#         np.cos(np.sqrt(X**2 + Y**2)) * np.sin(X),
#         np.sin(np.sqrt(X**2 + Y**2)) * np.cos(Y),
#         np.random.rand(*X.shape),
#         np.random.rand(*X.shape) * np.sin(X) * np.cos(Y),
#         np.log(np.abs(X + Y) + 1),
#         X * Y - np.sin(X),
#         np.sin(X*Y),
#         np.sin(X + Y),
#         np.cos(X + Y),
#         np.sin(X) + np.cos(Y) + np.random.rand(*X.shape),
#         np.sinh(X**2) - np.cosh(Y**2),
#         np.arctan(X*Y),
#         X**3 + Y**3,
#         X**2 - Y**2 + np.random.rand(*X.shape),
#         X**2 + Y**2 + np.sin(X) * np.cos(Y),
#         np.sqrt(np.abs(X**2 - Y**2)),
#         np.exp(np.sin(np.sqrt(X**2 + Y**2))),
#         np.tan(np.sin(X) + np.cos(Y)),
#         np.exp(X) + np.exp(Y),
#         np.abs(X - Y),
#         X * Y**2 - Y * X**2,
#         np.sin(X * Y**2),
#         np.cos(X**2 * Y),
#         np.sin(np.sqrt(np.abs(X + Y))),
#         X * np.sin(X) + Y * np.cos(Y),
#         np.abs(np.sin(np.sqrt(X**2 + Y**2))),
#         np.sin(X * Y) + np.random.rand(*X.shape),
#         X * np.cos(Y) + Y * np.sin(X),
#         X**3 * np.sin(Y),
#         np.exp(X * Y) - np.sin(X),
#         np.sinh(np.sqrt(X**2 + Y**2)),
#         np.abs(np.sin(X) * np.cos(Y)),
#         np.tan(X) * np.sin(Y),
#         np.sqrt(X**2 + Y**2 + 1),
#         np.sin(X) * np.tanh(Y),
#         np.sinh(np.sin(X)) + np.cosh(np.cos(Y)),
#         np.log(X**3 + Y**3 + 1),
#         np.exp(np.cos(X)) + np.exp(np.sin(Y)),
#         X * np.tan(Y),
#         Y * np.tan(X),
#         X * np.cosh(Y),
#         Y * np.sinh(X),
#         np.sin(X**2) * np.cos(Y**2),
#         X**2 - Y**2 + np.sin(X*Y),
#         X**3 + Y**3 + np.sin(X) + np.cos(Y),
#         np.random.rand(*X.shape) * np.sin(X**2 + Y**2),
#         np.sqrt(X**2 + np.abs(Y)),
#         X**2 * np.sin(Y),
#         Y**2 * np.cos(X),
#         np.random.rand(*X.shape) * np.sinh(X*Y),
#         np.tan(np.sqrt(X**2 + Y**2)),
#         np.exp(-X*Y),
#         np.sin(X) * np.sinh(Y),
#         X * np.sin(Y**2),
#         np.cos(X*Y) + np.sin(X + Y),
#         np.sin(X**2 + Y**2),
#         X**2 + Y**2 + np.exp(np.sin(X + Y)),
#         np.abs(np.cos(X) * np.sin(Y)),
#         np.sin(X * Y) + np.cos(X + Y),
#         X**2 - np.abs(Y) + np.sin(X*Y),
#         np.sin(X) * np.random.rand(*X.shape),
#         np.abs(np.tan(X) - np.tan(Y)),
#         np.cos(X) * np.sin(Y) * np.random.rand(*X.shape),
#         np.sinh(X) * np.cosh(Y) + np.random.rand(*X.shape),
#         np.sin(np.sqrt(X + Y)),
#         np.cos(X**2 + Y**2) + np.sin(X),
#         np.abs(np.sin(X)) + np.abs(np.cos(Y)) + np.random.rand(*X.shape),
#         np.exp(X**2 - Y**2),
#         np.sin(np.sqrt(X**2 + Y**2 + np.random.rand(*X.shape))),
#         X * np.cos(Y**2),
#         Y * np.sin(X**2),
#         np.exp(X*Y) - np.sinh(X),
#         np.tan(X) + np.cos(Y),
#         np.abs(X) * np.random.rand(*X.shape),
#         np.cos(np.sin(X + Y)),
#         np.random.rand(*X.shape) * np.exp(np.sin(X + Y)),
#     ]
    
#     # Randomly select one of the 100 functions
#     Z = random.choice(functions)

#     # Random colormap for the surface
#     surface = ax.plot_surface(X, Y, Z, cmap=np.random.choice(['viridis', 'plasma', 'inferno', 'coolwarm', 'spring', 'summer', 'winter']))

#     # Add a color bar
#     fig.colorbar(surface)

#     # If a previous plot exists, clear it from the window
#     if canvas:
#         canvas.get_tk_widget().pack_forget()
#         canvas._tkcanvas.pack_forget()

#     # Create a new canvas for the updated plot
#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack()

# # Create the main window
# root = tk.Tk()
# root.title("Random 3D Colorful Graph Generator")

# # Create a frame for the plot
# frame = tk.Frame(root)
# frame.pack()

# # Initial placeholder plot (empty)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# canvas = FigureCanvasTkAgg(fig, master=frame)
# canvas.draw()
# canvas.get_tk_widget().pack()

# # Create the button to generate a new random plot
# button = tk.Button(root, text="Generate Random 3D Graph", command=generate_random_3d_plot)
# button.pack()

# # Start the Tkinter event loop
# root.mainloop()



# Global variable for canvas
canvas = None

# Function to generate and display random 3D surface plot
def generate_random_3d_plot():
    global canvas  # Access global canvas variable
    
    # Create a new figure for the 3D plot
    fig = plt.figure(figsize=(21, 12))# Adjust the figure size as needed
    ax = fig.add_subplot(111, projection='3d')# Create a 3D axis
    
    # Create random data for the plot
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Define a list of 100 different mathematical functions for Z
    functions = [
        np.sin(np.sqrt(X**2 + Y**2)),
        np.cos(np.sqrt(X**2 + Y**2)),
        np.sin(X) * np.cos(Y),
        np.sin(X) + np.cos(Y),
        X**2 - Y**2,
        np.tan(np.sqrt(X**2 + Y**2)),
        np.sin(X**2) + np.cos(Y**2),
        np.sinh(X) + np.cosh(Y),
        np.log(np.abs(X**2 + Y**2 + 1)),  # Fixed: log needs positive values
        np.exp(-X**2 - Y**2),
        X * np.sin(Y),
        Y * np.cos(X),
        X**2 + Y**2,
        X**3 - Y**3,
        np.abs(np.sin(X)) + np.abs(np.cos(Y)),
        np.tanh(X) + np.tanh(Y),
        X**4 - Y**4,
        X**2 + Y**2 - np.sin(np.sqrt(X**2 + Y**2)),
        np.cos(np.sqrt(X**2 + Y**2)) * np.sin(X),
        np.sin(np.sqrt(X**2 + Y**2)) * np.cos(Y),
        np.random.rand(*X.shape),
        np.random.rand(*X.shape) * np.sin(X) * np.cos(Y),
        np.log(np.abs(X + Y) + 1),  # Fixed: log with abs to ensure positive values
        X * Y - np.sin(X),
        np.sin(X*Y),
        np.sin(X + Y),
        np.cos(X + Y),
        np.sin(X) + np.cos(Y) + np.random.rand(*X.shape),
        np.sinh(X**2) - np.cosh(Y**2),
        np.arctan(X*Y),
        X**3 + Y**3,
        X**2 - Y**2 + np.random.rand(*X.shape),
        X**2 + Y**2 + np.sin(X) * np.cos(Y),
        np.sqrt(np.abs(X**2 - Y**2)),  # Fixed: sqrt only accepts non-negative values
        np.exp(np.sin(np.sqrt(X**2 + Y**2))),
        np.tan(np.sin(X) + np.cos(Y)),
        np.exp(X) + np.exp(Y),
        np.abs(X - Y),
        X * Y**2 - Y * X**2,
        np.sin(X * Y**2),
        np.cos(X**2 * Y),
        np.sin(np.sqrt(np.abs(X + Y))),  # Fixed: sqrt with abs to avoid negatives
        X * np.sin(X) + Y * np.cos(Y),
        np.abs(np.sin(np.sqrt(X**2 + Y**2))),
        np.sin(X * Y) + np.random.rand(*X.shape),
        X * np.cos(Y) + Y * np.sin(X),
        X**3 * np.sin(Y),
        np.exp(X * Y) - np.sin(X),
        np.sinh(np.sqrt(X**2 + Y**2)),
        np.abs(np.sin(X) * np.cos(Y)),
        np.tan(X) * np.sin(Y),
        np.sqrt(X**2 + Y**2 + 1),  # Ensures positive input for sqrt
        np.sin(X) * np.tanh(Y),
        np.sinh(np.sin(X)) + np.cosh(np.cos(Y)),
        np.log(np.abs(X**3 + Y**3 + 1)),  # Fixed: log with abs to ensure positive values
        np.exp(np.cos(X)) + np.exp(np.sin(Y)),
        X * np.tan(Y),
        Y * np.tan(X),
        X * np.cosh(Y),
        Y * np.sinh(X),
        np.sin(X**2) * np.cos(Y**2),
        X**2 - Y**2 + np.sin(X*Y),
        X**3 + Y**3 + np.sin(X) + np.cos(Y),
        np.random.rand(*X.shape) * np.sin(X**2 + Y**2),
        np.sqrt(np.abs(X**2 + Y)),  # Fixed: sqrt with abs to avoid negatives
        X**2 * np.sin(Y),
        Y**2 * np.cos(X),
        np.random.rand(*X.shape) * np.sinh(X*Y),
        np.tan(np.sqrt(X**2 + Y**2)),
        np.exp(-X*Y),
        np.sin(X) * np.sinh(Y),
        X * np.sin(Y**2),
        np.cos(X*Y) + np.sin(X + Y),
        np.sin(X**2 + Y**2),
        X**2 + Y**2 + np.exp(np.sin(X + Y)),
        np.abs(np.cos(X) * np.sin(Y)),
        np.sin(X * Y) + np.cos(X + Y),
        X**2 - np.abs(Y) + np.sin(X*Y),
        np.sin(X) * np.random.rand(*X.shape),
        np.abs(np.tan(X) - np.tan(Y)),
        np.cos(X) * np.sin(Y) * np.random.rand(*X.shape),
        np.sinh(X) * np.cosh(Y) + np.random.rand(*X.shape),
        np.sin(np.sqrt(np.abs(X + Y))),  # Fixed: sqrt with abs to avoid negatives
        np.cos(X**2 + Y**2) + np.sin(X),
        np.abs(np.sin(X)) + np.abs(np.cos(Y)) + np.random.rand(*X.shape),
        np.exp(X**2 - Y**2),
        np.sin(np.sqrt(X**2 + Y**2 + np.random.rand(*X.shape))),
        X * np.cos(Y**2),
        Y * np.sin(X**2),
        np.exp(X*Y) - np.sinh(X),
        np.tan(X) + np.cos(Y),
        np.abs(X) * np.random.rand(*X.shape),
        np.cos(np.sin(X + Y)),
        np.random.rand(*X.shape) * np.exp(np.sin(X + Y)),
        np.sin(X) * np.cos(Y) + np.random.rand(*X.shape),
        np.tan(X) * np.tan(Y),
        np.sin(X) + np.cos(Y) + np.random.rand(*X.shape),
        np.sin(X**2 + Y**2) + np.cos(X + Y),
        np.exp(X**2 - Y**2) + np.sin(X*Y),
        np.sin(X + Y) + np.cos(X*Y),
        # Additional functions
        np.arcsin(np.sin(X)) + np.arccos(np.cos(Y)),
        np.exp(-(X**2 + Y**2)/2) / (2 * np.pi),  # Gaussian function
        np.sin(X) * np.exp(-Y**2),
        np.sqrt(np.abs(X*Y)) * np.cos(X + Y),
        np.log1p(np.abs(X**2 + Y**2)),
        np.sinh(X) * np.tanh(Y),
        np.cosh(X) * np.sinh(Y),
        np.exp(-np.abs(X)) * np.sin(Y),
        np.arctan2(Y, X),
        np.maximum(X**2, Y**2),
        np.minimum(np.abs(X), np.abs(Y)),
        np.hypot(X, Y),
        np.clip(np.sin(X), -0.5, 0.5) * np.cos(Y),
        np.sin(X) * np.sign(Y),
        np.floor(np.sin(X)) + np.ceil(np.cos(Y)),
        np.exp(-np.abs(X*Y)),
        np.sin(X) * np.log1p(np.abs(Y)),
        np.sqrt(np.abs(X*Y)) * np.sin(X - Y),
        np.exp(-X**2) * np.sin(Y**2),
        np.arctan(X) * np.arctan(Y)
    ]    
    # Randomly select one of the 100 functions
    Z = random.choice(functions)

    # Random colormap for the surface
    surface = ax.plot_surface(X, Y, Z, cmap=np.random.choice(['viridis', 'plasma', 'inferno', 'coolwarm', 'spring', 'summer', 'winter']))

    # Add a color bar
    fig.colorbar(surface)

    # If a previous plot exists, clear it from the window
    if canvas:
        canvas.get_tk_widget().pack_forget()
        canvas._tkcanvas.pack_forget()

    # Create a new canvas for the updated plot
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the main window
root = tk.Tk()
root.title("Random 3D Colorful Graph Generator")
root.geometry("2222x1280")  # Set the window size to 800x600 pixels

# Create a frame for the plot
frame = tk.Frame(root)
frame.pack()

# Initial placeholder plot (empty)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Create the button to generate a new random plot
button = tk.Button(root, text="Generate Random 3D Graph", command=generate_random_3d_plot)
button.pack()

# Start the Tkinter event loop
root.mainloop()