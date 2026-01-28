
import ipaddress 

def audit_net_Type(ipnode_address, block_size):
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
    "Type": "PRIVATE" if ipnode_address.is_private else "PUBLIC",
    "Binary Net": f"{net_int:032b}
}

ex

except ValueError as e:
    return f"Error Invalid IP or Mask provided. {e}"

    host = "10.168.47.212"
    mask = "255.255.255.128" # /25
    result = subnet_filter(host, mask)

    if isinstance(result, dict):
        print(f"Filtering {result['Input IP']} through {result['Subnet Mask']}...")
        print(f"Resulting Network ID: {result['Network ID']}")
        print("_" * 3)
        print(f"Logic Proof (Binary AND):")
print(f"IP:   {result['Binary IP']}")
        print(f"Mask: {result['Binary Mask']}") 
        print(f"Net:  {result['Binary Net']}")
        else 
        print (result)
    """


print(audit_net_Type("10.168.47.212", "255.255.255.128 "))