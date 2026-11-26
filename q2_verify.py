from ipaddress import ip_network

subnets = [
    ("Labs", "192.168.10.0/25"),
    ("Staff", "192.168.10.128/26"),
    ("Library", "192.168.10.192/27"),
    ("WAN Link", "192.168.10.224/30")
]

networks = []

for name, cidr in subnets:
    net = ip_network(cidr)

    networks.append(net)

    print("\n", name)
    print("Network:", net.network_address)
    print("Prefix:", net.prefixlen)
    print("Subnet Mask:", net.netmask)
    print("First Host:", net.network_address + 1)
    print("Last Host:", net.broadcast_address - 1)
    print("Broadcast:", net.broadcast_address)

for i in range(len(networks)):
    for j in range(i + 1, len(networks)):
        assert not networks[i].overlaps(networks[j])

print("\nAll original subnets are non-overlapping.")

hostel = ip_network("192.168.11.0/26")

print("\nHostel Network:", hostel)
print("Usable Hosts:", hostel.num_addresses - 2)

summary = ip_network("172.16.8.0/22")

print("\nSummary Route:", summary)
print("Summary Mask:", summary.netmask)