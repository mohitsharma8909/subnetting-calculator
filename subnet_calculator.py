import ipaddress

network = input("Enter Network (Example: 192.168.1.0/24): ")

try:
    net = ipaddress.ip_network(network)

    print("Network Address:", net.network_address)
    print("Broadcast Address:", net.broadcast_address)
    print("Total Hosts:", net.num_addresses)

    hosts = list(net.hosts())

    if hosts:
        print("First Host:", hosts[0])
        print("Last Host:", hosts[-1])

except ValueError:
    print("Invalid Network")
