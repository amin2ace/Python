import scapy.all as scapy
import subprocess
import manuf

def scan():
    # Implement the logic to extract local IP and subnet mask based on your system
    # You may use platform-specific commands like ifconfig or ipconfig
    # Replace the following with the actual implementation based on your system

    # For Linux:
    # result = subprocess.check_output(["ifconfig"]).decode("utf-8")

    # For Windows:
    # result = subprocess.check_output(["ipconfig"]).decode("utf-8")

    #OR

    # Extract local IP and subnet mask from the result
    local_ip = "192.168.1.1"
    subnet_mask = "255.255.255.0"
    # Get the local IP and subnet mask

    # Calculate the IP range based on the subnet mask
    ip_range = f"{local_ip[:-len(local_ip.split('.')[-1])]}101"#{subnet_mask.split('.')[-1]}"

    return ip_range


def send_arp(ip_range):
    # Create ARP request packet
    scapu
 
    # To list the fields in ARP()
    
    print(scapy.ls(scapy.ARP()))
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send and receive ARP requests using srp
    result = srp(packet, timeout=3, verbose=0)[0]

    return result

def result(response_list):
    devices_info = {}
    for sent, received in response_list:
        devices_info[received.psrc] = received.hwsrc

    return devices_info

if __name__ == "__main__":
    ip_range = scan()
    print(f"Scanning IP range: {ip_range}")

    responses = send_arp(ip_range)
    devices_info = result(responses)

    print("\nResults:")
    print("IP Address\t\tMAC Address")
    print("-----------\t\t------------")
    for ip, mac in devices_info.items():
        print(f"{ip}\t\t{mac}")
