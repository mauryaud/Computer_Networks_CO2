print("NAT TRANSLATION TABLE")

print("Inside Local       Inside Port    Inside Global      Global Port")

nat_entries = [
    ("192.168.1.10", 50000, "203.0.113.10", 40001),
    ("192.168.1.11", 50000, "203.0.113.10", 40002)
]

for entry in nat_entries:
    print(
        entry[0],
        entry[1],
        entry[2],
        entry[3]
    )