import ephem
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Set the interactive backend
import matplotlib
matplotlib.use('TkAgg')  # Use Tkinter for interactive plots

# Set your location
latitude = '' #'52.379189'  # Example: Amsterdam's latitude
longitude ='' #'4.900931'  # Example: Amsterdam's longitude

# geo://37.9842,23.7353

# Define the observer
observer = ephem.Observer()
observer.lat = latitude
observer.lon = longitude

# Generate dates for the year (e.g., 2024)
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Convert dates to numerical values (days since the start of the year)
numerical_dates = [(date - start_date).days for date in dates]

# Prepare lists to store times
sunrise_times = []
sunset_times = []
moonrise_times = []
moonset_times = []

# Calculate sunrise, sunset, moonrise, and moonset times for each day
for date in dates:
    observer.date = date

    # Calculate times for the day
    sunrise = observer.next_rising(ephem.Sun()).datetime()
    sunset = observer.next_setting(ephem.Sun()).datetime()
    moonrise = observer.next_rising(ephem.Moon()).datetime()
    moonset = observer.next_setting(ephem.Moon()).datetime()

    # Store the times (in seconds since midnight)
    sunrise_times.append((sunrise - datetime(sunrise.year, sunrise.month, sunrise.day)).total_seconds())
    sunset_times.append((sunset - datetime(sunset.year, sunset.month, sunset.day)).total_seconds())
    moonrise_times.append((moonrise - datetime(moonrise.year, moonrise.month, moonrise.day)).total_seconds())
    moonset_times.append((moonset - datetime(moonset.year, moonset.month, moonset.day)).total_seconds())

# Create a 2D graph for sunrise and sunset
plt.figure(figsize=(16, 9))#(10,6)
plt.plot(dates, sunrise_times, label='Sunrise', color='orange')
plt.plot(dates, sunset_times, label='Sunset', color='blue')
plt.plot(dates, moonrise_times, label='Moonrise', color='gray', linestyle='--')
plt.plot(dates, moonset_times, label='Moonset', color='darkgray', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Time (seconds from midnight)')
plt.title('Sunrise, Sunset, Moonrise, and Moonset Times (2024)')
plt.legend()
plt.xticks(dates[::30], rotation=45)  # Show date labels every 30 days
plt.tight_layout()
plt.show()

# Create a 3D graph (time vs. date vs. type of event)
fig = plt.figure(figsize=(16, 9))#(10,6)
ax = fig.add_subplot(111, projection='3d')

# Prepare data for 3D plot (we'll use the type of event as the z-axis)
event_types = ['Sunrise', 'Sunset', 'Moonrise', 'Moonset']
time_data = np.array([sunrise_times, sunset_times, moonrise_times, moonset_times])
z_values = np.array([0, 1, 2, 3])  # Map events to integer z values for 3D plotting

for i, event in enumerate(event_types):
    ax.scatter(numerical_dates, [z_values[i]] * len(dates), time_data[i], label=event)

ax.set_xlabel('Date')
ax.set_ylabel('Event Type')
ax.set_zlabel('Time (seconds from midnight)')
ax.set_title('3D Plot of Sun and Moon Event Times (2024)')
ax.set_yticks(z_values)
ax.set_yticklabels(event_types)

plt.xticks(numerical_dates[::30], rotation=45)  # Show date labels every 30 days
plt.tight_layout()
plt.legend()
plt.show()
