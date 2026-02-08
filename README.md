address, block_size):
    """
    Filters an IP address through a subnet mask to find the Network ID.
    Uses it logic to show networking

"""
try:

    ipint_str = ipaddress.IPv4Address(ipnode_address)
    maskint_str = ipaddress.IPv4Address(block_size)

ipnode_int = int(ipint_str)
block_int = int(maskint_str)
net_int = ipnode_int & block_int

net_ip = ipaddress.IPv4Address(net_int)

return {
    "Input IP": ipnode_address,
    "Subnet Mask": block_size,
    "Network ID": str(net_ip),
    "Binary IP": f"{ipnode_int:032b}",
    "Binary Mask": f"{block_int:032b}",
