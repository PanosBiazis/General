import requests
from PIL import Image
from io import BytesIO

# Your Google Maps API key
api_key = "YOUR_GOOGLE_MAPS_API_KEY" #https://console.cloud.google.com/welcome?inv=1&invt=AbiLpA&project=decent-line-442517-j0 

# Latitude and Longitude of your location
latitude = 40.748817  # Example: Latitude of the Empire State Building
longitude = -73.985428  # Example: Longitude of the Empire State Building

# Google Maps Static API endpoint
url = "https://maps.googleapis.com/maps/api/staticmap?"

# Parameters for the Static Map API request
params = {
    "center": f"{latitude},{longitude}",  # Location (latitude, longitude)
    "zoom": 15,  # Zoom level (1 to 20)
    "size": "600x600",  # Image size (width x height)
    "markers": f"color:red|{latitude},{longitude}",  # Marker at the location
    "key": api_key  # Your Google Maps API key
}

# Send the request to the Google Maps API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Open the image using Pillow
    img = Image.open(BytesIO(response.content))
    img.show()
else:
    print(f"Error: {response.status_code}")

