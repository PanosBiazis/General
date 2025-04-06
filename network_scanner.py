from scapy.all import ARP, Ether, srp
from uuid import getnode
import socket
import requests
import ipaddress
from concurrent.futures import ThreadPoolExecutor
import scapy.all as scapy

def scan_network(ip_range):
    # Create an ARP request packet to discover devices in the network
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send the packet and receive responses
    result = srp(packet, timeout=2, verbose=0)[0]

    # Extract IPs from responses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    # Print the list of devices
    print("Available devices on the network:")
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t{device['mac']}")

# def get_mac_address():
#     # Get the MAC address as a hexadecimal number
#     mac = getnode()
#     # Convert to human-readable MAC address format
#     mac_address = ':'.join(format((mac >> i) & 0xff, '02x') for i in range(0, 48, 8)[::-1])
#     return mac_address

def get_mac_of_device():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"Local device IP: {local_ip}")
        arp_response = scapy.ARP(pdst=local_ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_broadcast = broadcast/arp_response
        answered_list = scapy.srp(arp_broadcast, timeout=2, verbose=False)[0]
        for _, packet in answered_list:
            return packet[scapy.ARP].hwsrc
    except Exception as e:
        print(f"Error while fetching MAC address: {e}")


def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        return public_ip
    except requests.RequestException:
        return "Unable to retrieve public IP"
    
    
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Open port {port} found on {ip}")
    except Exception as e:
        pass  # Ignoring errors to keep the output clean

def scan_device(ip):
    print(f"Scanning IP: {ip}")
    for port in range(1,65536):  # Scans common ports (1-1024) 1025
        scan_port(ip, port)

def ports():
    ipnet=str(input("Give the ip of your network (e.g., 192.168.1.0/24) \n IP OF NETWORK: "))
    # Define the network to scan (e.g., 192.168.1.0/24)
    network = ipaddress.ip_network(ipnet, strict=False)#"192.168.1.0/24"

    with ThreadPoolExecutor(max_workers=256) as executor:#(1-49)50
        for ip in network:
            executor.submit(scan_device, str(ip))

if __name__ == "__main__":
    while True:  # Start an infinite loop
        choice = str(input("Do you want to find: \n 1.IP/MAC of the network \n 2.MAC of your device \n 3.PUBLIC IP \n 4.LOCAL IP \n 5.Available ports \n 6.Exit \n Selection: "))
        
        if choice == "1":
            scan_ips = input("Enter the IP to scan the network (e.g., 192.168.1.1/24) \n IP: ")
            scan_network(scan_ips)
        
        elif choice == "2":
            # print(get_mac_address())
            mac = get_mac_of_device()
            if mac:
                print(f"MAC Address of the device: {mac}")
        
        elif choice == "3":
            print(f"Your public IP address is: {get_public_ip()}")
        
        elif choice == "4":
            print(f"Your local IP address is: {get_local_ip()}")
        
        elif choice == "5":
            ports()
        
        elif choice == "6":
            print("Exiting the program.")
            break  # Exit the loop and end the program
        
        else:
            print("Invalid choice. Please select a valid option.")

