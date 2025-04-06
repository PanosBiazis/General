import requests
from PIL import Image
from io import BytesIO
from PIL import Image, ImageEnhance
from datetime import datetime, timedelta

# NASA API settings
API_KEY = "" #"YOUR_NASA_API_KEY"  # Replace with your actual NASA API key
BASE_URL = "https://api.nasa.gov/planetary/earth/assets"

# date (str): Date in 'YYYY-MM-DD' format.
# date (str): Date in 'YYYY-MM-DDTHH:mm:ss' format (UTC time).

def fetch_satellite_image(lat, lon, date, dim=0.1):
    """
    Fetch satellite image for a specific latitude, longitude, and date.

    Parameters:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
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
        print(f"Error fetching satellite image: {e}")
        return None
    
    
def adjust_to_daytime(lat, lon):
    """
    Adjust date and time to local daytime for a given latitude and longitude.

    Parameters:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.

    Returns:
        str: Adjusted date and time in 'YYYY-MM-DDTHH:mm:ss' format (UTC time).
    """
    # Current UTC date and time
    now_utc = datetime.utcnow()

    # Convert UTC to local time for Greece (UTC+2 in winter, UTC+3 in summer)
    # Adjust based on time zone rules if needed
    greece_offset = timedelta(hours=2)
    local_time = now_utc + greece_offset

    # Adjust to ensure it falls within daytime
    local_time = local_time.replace(hour=12, minute=0, second=0, microsecond=0)  # Set to noon

    # Convert back to UTC for NASA API
    daytime_utc = local_time - greece_offset
    return daytime_utc.strftime("%Y-%m-%dT%H:%M:%S")



# Example usage
if __name__ == "__main__":
    # Specify the latitude and longitude of the location, Example: Greece
    #latitude =  #horizontal lines
    #longitude =  #vertical lines
    latitude 
    longitude = 
    date = "2024-11-22"
    # Adjust date and time to daytime
    # adjusted_date = adjust_to_daytime(latitude, longitude)
    dimension = 0.5

    print("Fetching satellite image...")
    image = fetch_satellite_image(latitude, longitude, date, dimension)
    
    # print(f"Fetching satellite image for date/time: {adjusted_date}")
    # image = fetch_satellite_image(latitude, longitude, adjusted_date, dimension)
    
    if image:
        image = image.convert("RGB")  # Convert to RGB before saving as JPEG
        image.show()  # Open the image
        image.save(r"F:\panag\Pictures\Saved Pictures\satellite\satellite_image_22_11_24.jpg")  # Save locally
        print("Image saved as 'satellite_image_22_11_24.jpg'.")
        

        # Load the existing image
        image_path = r"F:\panag\Pictures\Saved Pictures\satellite\satellite_image_22_11_24.jpg"  # Update this path to your image location
        image = Image.open(image_path)

        # Enhance the contrast
        enhancer = ImageEnhance.Contrast(image)
        contrast_level = 2  # You can increase this value (e.g., 3, 4, etc.) for stronger contrast
        enhanced_image = enhancer.enhance(contrast_level)

        # Save and show the enhanced image
        enhanced_image.show()  # Open the enhanced image
        enhanced_image.save(r"F:\panag\Pictures\Saved Pictures\satellite\satellite_image_contrast_22_11_24.jpg")  # Save it with a new name
        print("Enhanced image saved as 'satellite_image_contrast_22_11_24.jpg'.")

    else:
        print("Failed to fetch image.")
