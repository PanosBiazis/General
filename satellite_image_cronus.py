import requests
import json
import os

# Function to get the Astronomy Picture of the Day (APOD) from NASA API
def get_apod(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Title:", data['title'])
        print("Date:", data['date'])
        print("Explanation:", data['explanation'])
        print("Image URL:", data['url'])
        
        # If it's an image, save it locally
        if 'url' in data and data['url'].endswith(('jpg', 'png')):
            img_data = requests.get(data['url']).content
            img_name = f"F:\\panag\\Pictures\\Saved Pictures\\satellite\\apod_{data['date']}.jpg"
            with open(img_name, 'wb') as handler:
                handler.write(img_data)
            print(f"Image saved as {img_name}")
    else:
        print("Failed to retrieve data from NASA API")

# Replace with your actual NASA API key
api_key = "" #"DEMO_KEY"  # Use your own API key here

# Get APOD and save the image
get_apod(api_key)
