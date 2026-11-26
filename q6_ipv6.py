from ipaddress import IPv6Address

address = IPv6Address(
    "2001:0db8:0000:0000:0000:ff00:0042:8329"
)

print("Original IPv6 Address:")
print("2001:0db8:0000:0000:0000:ff00:0042:8329")

print("\nShortest IPv6 Address:")
print(address.compressed)


# EUI-64 calculation

mac = [0x00, 0x1A, 0x2B, 0x3C, 0x4D, 0x5E]

eui = (
    mac[:3]
    + [0xFF, 0xFE]
    + mac[3:]
)

# Invert universal/local bit
eui[0] ^= 0x02

print("\nModified EUI-64:")

print(
    ":".join(
        f"{byte:02x}"
        for byte in eui
    )
)