"""
Variable-length subnetting (VLSM)
of 192.168.10.0/24 for a college campus.
"""

import math


def to_int(ip):
    a, b, c, d = map(int, ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d


def to_ip(n):
    return ".".join(
        str((n >> s) & 255)
        for s in (24, 16, 8, 0)
    )


def vlsm(base, needs):
    addr = to_int(base)

    for name, hosts in sorted(
        needs, key=lambda x: -x[1]
    ):

        # Find the smallest block
        block = 1 << math.ceil(
            math.log2(hosts + 2)
        )

        prefix = 32 - int(math.log2(block))

        # Align address to subnet boundary
        network = (
            (addr + block - 1) // block
        ) * block

        broadcast = network + block - 1

        first_host = network + 1
        last_host = broadcast - 1

        print(
            f"{name:<10} "
            f"{to_ip(network)}/{prefix} "
            f"hosts {to_ip(first_host)} - "
            f"{to_ip(last_host)} "
            f"bcast {to_ip(broadcast)}"
        )

        addr = broadcast + 1

    return to_ip(addr)


needs = [
    ("Labs", 100),
    ("Staff", 50),
    ("Library", 25),
    ("WAN link", 2)
]

print(
    "next free address:",
    vlsm("192.168.10.0", needs)
)