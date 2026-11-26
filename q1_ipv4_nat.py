"""Q1: Validate the four IPv4 host addresses and illustrate PAT port translation."""
from ipaddress import ip_interface

devices = [
    ("Admission PC", "172.16.45.200/20"),
    ("Lab printer", "10.0.15.255/21"),
    ("X-ray server", "192.168.4.0/23"),
    ("Clinic router", "203.0.113.10/29"),
]

for name, value in devices:
    interface = ip_interface(value)
    network = interface.network
    usable = list(network.hosts())
    valid = interface.ip in usable

    print(f"{name}: {interface.ip}/{network.prefixlen}")
    print(f"  network={network.network_address}, broadcast={network.broadcast_address}")
    print(f"  usable={usable[0]} - {usable[-1]}")
    print(
        f"  decision={'VALID HOST' if valid else 'INVALID HOST (network/broadcast address)'}"
    )

print("\nPAT example: two inside devices share one public IPv4 address.")

flows = [
    ("192.168.1.10", 50000, "203.0.113.10", 40001, "198.51.100.20:443"),
    ("192.168.1.11", 50000, "203.0.113.10", 40002, "198.51.100.20:443"),
]

print("Inside local       Inside port  Public address  Public port  Remote")

for src, sport, public, pport, remote in flows:
    print(f"{src:<18} {sport:<12} {public:<15} {pport:<12} {remote}")