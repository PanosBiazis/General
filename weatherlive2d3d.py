import requests
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to fetch live weather data from OpenWeatherMap
def fetch_weather_data(api_key, city=""):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        weather_description = data['weather'][0]['description']
        return temp, humidity, pressure, weather_description
    else:
        print("Error fetching data:", data)
        return None

# Plotting the weather data on a 2D and 3D graph
def plot_weather_data(temp, humidity, pressure):
    # 2D plot
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"], [temp, humidity, pressure], color=['blue', 'green', 'red'])
    ax.set_title("Weather Data (2D)")
    ax.set_ylabel("Value")
    plt.show()

    # 3D plot
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Set the data for the 3D plot
    x = np.array([1, 2, 3])
    y = np.array([temp, humidity, pressure])
    z = np.array([0, 0, 0])

    ax.bar3d(x, y, z, dx=0.5, dy=0.5, dz=[10, 10, 10], color=['blue', 'green', 'red'])

    ax.set_xlabel('Data Points')
    ax.set_ylabel('Values')
    ax.set_zlabel('Height')
    ax.set_title("Weather Data (3D)")

    plt.show()

# Main function
def main():
    api_key = ""  # Replace with your actual API key
    city = ""  # You can change this to any city you like

    weather_data = fetch_weather_data(api_key, city)
    if weather_data:
        temp, humidity, pressure, weather_description = weather_data
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")

        plot_weather_data(temp, humidity, pressure)

if __name__ == "__main__":
    main()
