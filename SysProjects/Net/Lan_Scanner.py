from scapy.all import ARP, Ether, srp
import socket
import struct

def get_default_gateway():
    """Get the default gateway of the current network"""
    with open("/proc/net/route") as route_file:
        for line in route_file:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue
            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

def scan_network(ip_range):
    """Scan the given IP range for connected devices"""
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def main():
    default_gateway = get_default_gateway()
    if default_gateway:
        ip_parts = default_gateway.split('.')
        ip_range = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.1/24"
        devices = scan_network(ip_range)
        print("Devices connected to the network:")
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}")
    else:
        print("Could not determine the default gateway.")

if __name__ == "__main__":
    main()
