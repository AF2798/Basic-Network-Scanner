from scapy.all import ARP , Ether, srp

t_ip=input("Enter the Target IP like 192.168.0.1/24 : ") #get the ip address of the machine that we want to scan
arp =ARP(pdst=t_ip)

ether=Ether(dst="ff:ff:ff:ff:ff:ff") #indicate the broadcast address

packet=ether/arp

result = srp(packet, timeout=3)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    
# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))