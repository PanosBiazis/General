import tkinter as tk
from tkinter import ttk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation


def clear_simulation_frame():
    """Clears the frame to display the next simulation."""
    for widget in simulation_frame.winfo_children():
        widget.destroy()


def simulate_projectile():
    """Simulates projectile motion."""
    clear_simulation_frame()

    v0 = 20  # Initial velocity
    theta = np.radians(45)  # Launch angle
    g = 9.8  # Gravitational acceleration

    t_values = np.linspace(0, 2 * v0 * np.sin(theta) / g, 500)
    x_values = v0 * np.cos(theta) * t_values
    y_values = v0 * np.sin(theta) * t_values - 0.5 * g * t_values**2

    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, max(x_values))
    ax.set_ylim(0, max(y_values) * 1.1)
    ax.set_title("Projectile Motion")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")

    line, = ax.plot([], [], 'ro-')

    def update(frame):
        line.set_data(x_values[:frame], y_values[:frame])
        return line,

    canvas = FigureCanvasTkAgg(fig, master=simulation_frame)
    canvas.get_tk_widget().pack()

    ani = FuncAnimation(fig, update, frames=len(t_values), interval=20, blit=True)
    canvas.draw()


def simulate_shm():
    """Simulates simple harmonic motion."""
    clear_simulation_frame()

    A = 1  # Amplitude
    omega = 2 * np.pi  # Angular frequency

    t_values = np.linspace(0, 10, 500)
    y_values = A * np.sin(omega * t_values)

    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, max(t_values))
    ax.set_ylim(-A * 1.5, A * 1.5)
    ax.set_title("Simple Harmonic Motion")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Displacement (m)")

    line, = ax.plot([], [], 'b-')

    def update(frame):
        line.set_data(t_values[:frame], y_values[:frame])
        return line,

    canvas = FigureCanvasTkAgg(fig, master=simulation_frame)
    canvas.get_tk_widget().pack()

    ani = FuncAnimation(fig, update, frames=len(t_values), interval=20, blit=True)
    canvas.draw()


def simulate_pendulum():
    """Simulates pendulum motion."""
    clear_simulation_frame()

    length = 2  # Length of the pendulum
    g = 9.8  # Gravitational acceleration
    theta0 = np.radians(30)  # Initial angle

    omega = np.sqrt(g / length)
    t_values = np.linspace(0, 10, 500)
    theta_values = theta0 * np.cos(omega * t_values)

    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_xlim(-length * 1.5, length * 1.5)
    ax.set_ylim(-length * 1.5, length * 1.5)
    ax.set_title("Pendulum Motion")
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")

    line, = ax.plot([], [], 'r-')

    def update(frame):
        x = length * np.sin(theta_values[frame])
        y = -length * np.cos(theta_values[frame])
        line.set_data([0, x], [0, y])
        return line,

    canvas = FigureCanvasTkAgg(fig, master=simulation_frame)
    canvas.get_tk_widget().pack()

    ani = FuncAnimation(fig, update, frames=len(t_values), interval=20, blit=True)
    canvas.draw()


# def simulate_circular_motion():
#     """Simulates circular motion."""
#     clear_simulation_frame()

#     radius = 1  # Radius of the circle
#     omega = 2 * np.pi  # Angular velocity

#     t_values = np.linspace(0, 10, 500)
#     x_values = radius * np.cos(omega * t_values)
#     y_values = radius * np.sin(omega * t_values)

#     fig = Figure(figsize=(6, 4))
#     ax = fig.add_subplot(111)
#     ax.set_xlim(-radius * 1.5, radius * 1.5)
#     ax.set_ylim(-radius * 1.5, radius * 1.5)
#     ax.set_title("Circular Motion")
#     ax.set_xlabel("X Position (m)")
#     ax.set_ylabel("Y Position (m)")

#     point, = ax.plot([], [], 'bo')

#     def update(frame):
#         point.set_data(x_values[frame], y_values[frame])
#         return point,

#     canvas = FigureCanvasTkAgg(fig, master=simulation_frame)
#     canvas.get_tk_widget().pack()

#     ani = FuncAnimation(fig, update, frames=len(t_values), interval=20, blit=True)
#     canvas.draw()


def simulate_circular_motion():
    """Simulates circular motion."""
    clear_simulation_frame()

    radius = 1  # Radius of the circle
    omega = 2 * np.pi  # Angular velocity

    t_values = np.linspace(0, 10, 500)
    x_values = radius * np.cos(omega * t_values)
    y_values = radius * np.sin(omega * t_values)

    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_xlim(-radius * 1.5, radius * 1.5)
    ax.set_ylim(-radius * 1.5, radius * 1.5)
    ax.set_title("Circular Motion")
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")

    point, = ax.plot([], [], 'bo')  # Initialize point

    def update(frame):
        """Update point position for each frame."""
        point.set_data([x_values[frame]], [y_values[frame]])
        return point,

    canvas = FigureCanvasTkAgg(fig, master=simulation_frame)
    canvas.get_tk_widget().pack()

    ani = FuncAnimation(fig, update, frames=len(t_values), interval=20, blit=True)
    canvas.draw()


def simulate_wave_propagation():
    """Simulates wave propagation."""
    clear_simulation_frame()

    A = 1  # Amplitude
    k = 2 * np.pi / 10  # Wave number
    omega = 2 * np.pi  # Angular frequency

    x_values = np.linspace(0, 10, 500)
    t_values = np.linspace(0, 10, 500)

    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 10)
    ax.set_ylim(-A * 1.5, A * 1.5)
    ax.set_title("Wave Propagation")
    ax.set_xlabel("Position (m)")
    ax.set_ylabel("Displacement (m)")

    line, = ax.plot([], [], 'g-')

    def update(frame):
        y_values = A * np.sin(k * x_values - omega * t_values[frame])
        line.set_data(x_values, y_values)
        return line,

    canvas = FigureCanvasTkAgg(fig, master=simulation_frame)
    canvas.get_tk_widget().pack()

    ani = FuncAnimation(fig, update, frames=len(t_values), interval=20, blit=True)
    canvas.draw()


# Tkinter GUI setup
root = tk.Tk()
root.title("Physics Simulations")

main_frame = ttk.Frame(root)
main_frame.pack(side=tk.LEFT, fill=tk.Y)

simulation_frame = ttk.Frame(root)
simulation_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Buttons for selecting simulations
ttk.Button(main_frame, text="Projectile Motion", command=simulate_projectile).pack(pady=10)
ttk.Button(main_frame, text="Simple Harmonic Motion", command=simulate_shm).pack(pady=10)
ttk.Button(main_frame, text="Pendulum Motion", command=simulate_pendulum).pack(pady=10)
ttk.Button(main_frame, text="Circular Motion", command=simulate_circular_motion).pack(pady=10)
ttk.Button(main_frame, text="Wave Propagation", command=simulate_wave_propagation).pack(pady=10)

root.mainloop()
