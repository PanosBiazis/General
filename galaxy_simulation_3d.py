import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use('TkAgg')

# Set the number of stars in the galaxy simulation
num_stars = 100000
# 100000000000 745 GB required

# Generate random positions for stars in a spiral galaxy-like shape
theta = np.random.uniform(0, 4 * np.pi, num_stars)
r = np.random.normal(loc=0, scale=1, size=num_stars)
z = np.random.normal(loc=0, scale=0.05, size=num_stars)

# Generate the 3D coordinates for the stars
x = r * np.cos(theta)
y = r * np.sin(theta)

# Generate random colors for the stars
colors = np.random.choice(['white', 'yellow', 'blue', 'lightblue', 'orange','red','purple','pink','green','brown'], num_stars)

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 7))#10,7 size of window# fig = plt.figure(figsize=(400, 200),dpi=25)#10,7 size of window
ax = fig.add_subplot(111, projection='3d')

# Set the window title
fig.canvas.manager.set_window_title("Galaxy Simulation 3D")

# Set the figure to fullscreen mode
# fig.canvas.manager.full_screen_toggle()

# Plot the stars with different colors
ax.scatter(x, y, z, c=colors, s=0.5)

# Setting plot parameters
ax.set_facecolor('black')  # Set background to black to mimic space
ax.set_title("3D Simulation of a Galaxy with Colored Stars")
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")
ax.set_zlabel("Z Coordinate")

# Remove grid and axes for a cleaner look
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

plt.show()
