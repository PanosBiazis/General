import requests
from PIL import Image
from io import BytesIO
from datetime import datetime

# NASA API settings for Lunar Reconnaissance Orbiter (LRO)
API_KEY = ""  # Replace with your actual NASA API key
BASE_URL = "https://api.nasa.gov/planetary/earth/assets"

def fetch_lunar_image(lat, lon, date, dim=0.1):
    """
    Fetch lunar image for a specific latitude, longitude, and date from the Lunar Reconnaissance Orbiter.

    Parameters:
        lat (float): Latitude of the location on the Moon.
        lon (float): Longitude of the location on the Moon.
        date (str): Date in 'YYYY-MM-DD' format.
        dim (float): Dimension of the image (default: 0.1 degrees).

    Returns:
        Image object or None if the request fails.
    """
    params = {
        "lat": lat,
        "lon": lon,
        "date": date,
        "dim": dim,
        "api_key": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        # Get the image URL
        data = response.json()
        image_url = data.get("url")
        if not image_url:
            print("No image found for the specified parameters.")
            return None

        # Fetch the image
        img_response = requests.get(image_url)
        img_response.raise_for_status()
        img = Image.open(BytesIO(img_response.content))
        return img

    except requests.exceptions.RequestException as e:
        print(f"Error fetching lunar image: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Specify the latitude and longitude of the location on the Moon (Example: Moon's South Pole)
    latitude = -90.0  # Latitude of the Moon's South Pole
    longitude = 0.0  # Longitude of the Moon's South Pole
    date = "2024-11-22"  # Date in 'YYYY-MM-DD' format
    dimension = 0.5  # Image dimension

    print("Fetching lunar image...")
    image = fetch_lunar_image(latitude, longitude, date, dimension)

    if image:
        image = image.convert("RGB")  # Convert to RGB before saving as JPEG
        image.show()  # Open the image
        image.save(r"F:\panag\Pictures\Saved Pictures\lunar\lunar_image_22_11_24.jpg")  # Save locally
        print("Lunar image saved as 'lunar_image_22_11_24.jpg'.")
    else:
        print("Failed to fetch lunar image.")
