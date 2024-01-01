import scapy.all as scapy
import subprocess
import manuf


ip = '192.168.1.101'
# creating an ARP request to the ip address
arp_request = scapy.ARP(pdst=ip) 

# setting the denstination MAC address to broadcast MAC address
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

# combining the ARP packet with the broadcast message
arp_request_broadcast = broadcast / arp_request


answ = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]


print(answ[0][1].hwsrc)



