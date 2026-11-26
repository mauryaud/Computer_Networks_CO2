from ipaddress import ip_network, ip_address

routes = [
    ("10.0.0.0/8", "192.0.2.1"),
    ("10.1.0.0/16", "192.0.2.5"),
    ("10.1.2.0/24", "192.0.2.9"),
    ("10.1.2.128/25", "192.0.2.13"),
    ("0.0.0.0/0", "198.51.100.1")
]

destinations = [
    "10.1.2.200",
    "10.1.2.100",
    "10.1.9.9",
    "10.7.7.7",
    "8.8.8.8"
]

for destination in destinations:
    address = ip_address(destination)

    matching = [
        (ip_network(network), next_hop)
        for network, next_hop in routes
        if address in ip_network(network)
    ]

    best = max(matching, key=lambda x: x[0].prefixlen)

    print(
        destination,
        "->",
        best[1],
        "via",
        best[0]
    )