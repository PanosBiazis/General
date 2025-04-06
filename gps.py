from geopy.geocoders import Nominatim
import requests
import asyncio
from bleak import BleakScanner, BleakClient
import re

def get_geographical_location():
    try:
        # Get the public IP address
        response = requests.get("https://api.ipify.org?format=json")
        ip_address = response.json().get("ip")

        # Get geographical details using IP
        location_data = requests.get(f"https://ipinfo.io/{ip_address}/json").json()
        loc = location_data.get("loc", "0,0").split(",")
        latitude, longitude = float(loc[0]), float(loc[1])

        # Use geopy to get more detailed location info
        geolocator = Nominatim(user_agent="geo_locator")
        location = geolocator.reverse((latitude, longitude), language="en")

        print("IP Address:", ip_address)
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("Address:", location.address if location else "Address not found")
    except Exception as e:
        print("Error occurred:", e)


def parse_nmea_sentence(nmea_sentence):
    """Parse an NMEA GPS sentence and extract latitude and longitude."""
    if nmea_sentence.startswith("$GPGGA"):
        fields = nmea_sentence.split(",")
        if len(fields) > 6:
            latitude = fields[2]
            latitude_dir = fields[3]
            longitude = fields[4]
            longitude_dir = fields[5]
            
            # Convert to decimal degrees
            if latitude and longitude:
                lat_deg = int(latitude[:2]) + float(latitude[2:]) / 60.0
                lon_deg = int(longitude[:3]) + float(longitude[3:]) / 60.0
                if latitude_dir == "S":
                    lat_deg = -lat_deg
                if longitude_dir == "W":
                    lon_deg = -lon_deg
                return lat_deg, lon_deg
    return None, None


async def find_and_connect_to_gps():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()

    for device in devices:
        print(f"Found Device: {device.name} ({device.address})")
        if "GPS" in device.name.upper():
            print("GPS device found!")
            return device.address

    print("No GPS device found.")
    return None


async def read_gps_data(address):
    try:
        print(f"Connecting to GPS device at {address}...")
        async with BleakClient(address) as client:
            print("Connected successfully!")
            
            # Reading GPS data (simulate reading NMEA sentences)
            while True:
                # Replace this with actual characteristic UUID for your GPS device
                raw_data = await client.read_gatt_char("YOUR-CHARACTERISTIC-UUID")
                nmea_sentence = raw_data.decode("utf-8")
                print("Raw GPS Data:", nmea_sentence)

                latitude, longitude = parse_nmea_sentence(nmea_sentence)
                if latitude and longitude:
                    print(f"Latitude: {latitude}, Longitude: {longitude}")
    except Exception as e:
        print("Failed to read GPS data:", e)


async def main():
    gps_address = await find_and_connect_to_gps()
    if gps_address:
        await read_gps_data(gps_address)
    


if __name__ == "__main__":
    while True:
        print("Choose for gps:")
        print("1. Get GPS from IP")
        print("2. Get GPS from bluetooth device")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            get_geographical_location()
        elif choice == "2":
            # Get GPS from device
            asyncio.run(main())
        elif choice.lower() == "3" or "exit":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")
        