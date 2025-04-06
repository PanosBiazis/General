from bleak import BleakScanner

async def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()

    if devices:
        print(f"{len(devices)} devices found:")
        for device in devices:
            print(f"  {device.name} - {device.address}")
    else:
        print("No devices found.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(scan_bluetooth_devices())
