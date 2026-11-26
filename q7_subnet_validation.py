from ipaddress import ip_network

subnets = [
    ("Labs", "192.168.10.0/25"),
    ("Staff", "192.168.10.128/26"),
    ("Library", "192.168.10.192/27"),
    ("WAN", "192.168.10.224/30"),
    ("Hostel", "192.168.11.0/26")
]

networks = []

print("REVISED CAMPUS NETWORK\n")

for name, address in subnets:

    net = ip_network(address)

    networks.append(net)

    print("Department:", name)
    print("Network:", net.network_address)
    print("Subnet Mask:", net.netmask)
    print("First Host:", net.network_address + 1)
    print("Last Host:", net.broadcast_address - 1)
    print("Broadcast:", net.broadcast_address)
    print("-" * 40)


print("\nOVERLAP VALIDATION")

for i in range(len(networks)):

    for j in range(i + 1, len(networks)):

        if networks[i].overlaps(networks[j]):
            print("Overlap detected!")
        else:
            print(
                networks[i],
                "and",
                networks[j],
                "do not overlap"
            )

print("\nRedesigned network validation completed.")