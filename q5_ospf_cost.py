print("OSPF COST CALCULATION")

speeds = [10, 100, 1000, 10000]

print("\nDefault Reference Bandwidth: 100 Mbps")

for speed in speeds:
    cost = max(1, 100 // speed)
    print(speed, "Mbps =", cost)


print("\nNew Reference Bandwidth: 10000 Mbps")

for speed in speeds:
    cost = max(1, 10000 // speed)
    print(speed, "Mbps =", cost)