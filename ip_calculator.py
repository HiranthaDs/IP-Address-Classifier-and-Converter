# ip_calculator.py

def calculate_ip_class(octet1, octet2, octet3, octet4):
    """
    Calculates the class of the IP address, subnet mask, network ID, and host ID
    based on the first octet (octet1).
    """
    # Validate each octet
    for octet in [octet1, octet2, octet3, octet4]:
        if not (0 <= octet <= 255):
            raise ValueError("IP octets must be in the range of 0-255.")

    # Determine the IP class
    if 1 <= octet1 <= 126:
        ip_class = "A"
        subnet_mask = "255.0.0.0"
        network_id = f"{octet1}.0.0.0"
    elif 128 <= octet1 <= 191:
        ip_class = "B"
        subnet_mask = "255.255.0.0"
        network_id = f"{octet1}.{octet2}.0.0"
    elif 192 <= octet1 <= 223:
        ip_class = "C"
        subnet_mask = "255.255.255.0"
        network_id = f"{octet1}.{octet2}.{octet3}.0"
    elif 224 <= octet1 <= 239:
        ip_class = "D"
        subnet_mask = "N/A (Reserved for Multicast)"
        network_id = "N/A"
    else:
        ip_class = "E"
        subnet_mask = "N/A (Reserved for Experimental Use)"
        network_id = "N/A"

    # Host ID
    host_id = octet4 if ip_class in ["A", "B", "C"] else "N/A"

    return ip_class, subnet_mask, network_id, host_id


def convert_to_binary(octet1, octet2, octet3, octet4):
    """
    Converts the four octets of the IP address into their binary representation.
    """
    binary_octet1 = format(octet1, '08b')
    binary_octet2 = format(octet2, '08b')
    binary_octet3 = format(octet3, '08b')
    binary_octet4 = format(octet4, '08b')

    # Combine the binary octets
    binary_ip = f"{binary_octet1}.{binary_octet2}.{binary_octet3}.{binary_octet4}"

    return binary_ip
