import datetime
import requests
import ntplib

# API Endpoints
API_KEY = ""#api of nasa
CHRONUS_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
LUNAR_URL = "https://api.nasa.gov/planetary/earth/assets"
MARS_URL = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key={API_KEY}"
TIME_API_URL = "http://api.timeapi.io/api/Time/current/zone?timeZone=UTC"

def fetch_pc_time():
    return datetime.datetime.now()

def fetch_ntp_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('time.google.com', version=3)
        # Use datetime.datetime.utcfromtimestamp correctly
        return datetime.datetime.utcfromtimestamp(response.tx_time)
    except Exception as e:
        return f"Error fetching NTP time: {e}"

def fetch_chronus_data():
    try:
        response = requests.get(CHRONUS_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def fetch_lunar_data(latitude, longitude):
    current_date = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    params = {
        "lon": longitude,
        "lat": latitude,
        "date": current_date,
        "dim": 0.1,
        "api_key": API_KEY,
    }
    try:
        response = requests.get(LUNAR_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def fetch_mars_data(sol=1000):
    params = {
        "sol": sol,
        "api_key": API_KEY,
    }
    try:
        response = requests.get(MARS_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def main():
    print("Fetching time and astronomical data...\n")

    pc_time = fetch_pc_time()
    print(f"PC Time: {pc_time}\n")

    ntp_time = fetch_ntp_time()
    print(f"NTP Time: {ntp_time}\n")

    chronus_data = fetch_chronus_data()
    if "error" in chronus_data:
        print(f"Error fetching Chronus data: {chronus_data['error']}")
    else:
        print(f"Chronus Data:\n  Date: {chronus_data['date']}\n  Title: {chronus_data['title']}\n  Description: {chronus_data['explanation']}\n")

    lunar_data = fetch_lunar_data(latitude=36.7783, longitude=-119.4179)
    if "error" in lunar_data:
        print(f"Error fetching Lunar data: {lunar_data['error']}")
    else:
        print(f"Lunar Data:\n  ID: {lunar_data.get('id')}\n  Date: {lunar_data.get('date')}\n  URL: {lunar_data.get('url')}\n")

    mars_data = fetch_mars_data()
    if "error" in mars_data:
        print(f"Error fetching Mars data: {mars_data['error']}")
    else:
        photos = mars_data.get("photos", [])
        print("Mars Data:")
        for i, photo in enumerate(photos[:5], 1):
            print(f"  Photo {i}:\n    ID: {photo['id']}\n    Earth Date: {photo['earth_date']}\n    URL: {photo['img_src']}")

if __name__ == "__main__":
    main()
