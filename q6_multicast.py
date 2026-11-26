from ipaddress import IPv4Address

group = IPv4Address("239.1.2.3")

# Map lower 23 bits of IPv4 multicast address
low23 = int(group) & 0x7FFFFF

mac_int = 0x01005E000000 | low23

multicast_mac = ":".join(
    f"{(mac_int >> shift) & 0xff:02x}"
    for shift in (40, 32, 24, 16, 8, 0)
)

print("IPv4 Multicast Group:", group)

print(
    "Ethernet Multicast MAC:",
    multicast_mac
)