import requests
from PIL import Image
from io import BytesIO
from datetime import datetime, timedelta

# NASA API settings for Mars Rover
API_KEY = ""  # Replace with your actual NASA API key
BASE_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

def fetch_mars_rover_image(sol, camera='FHAZ', count=1):
    """
    Fetch Mars rover images for a specific sol (day on Mars), camera type, and photo count.

    Parameters:
        sol (int): The Martian day (sol) for which to fetch images.
        camera (str): The camera to fetch images from (e.g., 'FHAZ', 'RHAZ', etc.).
        count (int): The number of images to fetch (default: 1).

    Returns:
        List of Image objects or an empty list if the request fails.
    """
    params = {
        "sol": sol,
        "camera": camera,
        "api_key": API_KEY,
        "count": count  # Limit the number of images to fetch
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        # Get image URLs
        data = response.json()
        photos = data.get("photos", [])
        if not photos:
            print("No images found for the specified parameters.")
            return []

        images = []
        for photo in photos:
            image_url = photo.get("img_src")
            if image_url:
                # Fetch and open the image
                img_response = requests.get(image_url)
                img_response.raise_for_status()
                img = Image.open(BytesIO(img_response.content))
                images.append(img)

        return images

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Mars rover images: {e}")
        return []

# Example usage
if __name__ == "__main__":
    sol = 2500  # Martian day (sol)
    camera = "FHAZ"  # Front Hazard Camera
    count = 1  # Number of images to fetch

    print(f"Fetching Mars rover images for sol {sol}...")
    images = fetch_mars_rover_image(sol, camera, count)

    if images:
        # Process the first image from the list (if multiple images are fetched)
        image = images[0]
        image.show()  # Show the image
        image.save(r"F:\panag\Pictures\Saved Pictures\mars_rover_image_sol_2500.jpg")  # Save locally
        print("Image saved as 'mars_rover_image_sol_2500.jpg'.")
    else:
        print("Failed to fetch Mars rover image.")
