# Version 0.2.0
# connect external functions and templates from templates.py and ext_func.py
import templates
import ext_func


def ip_calculator(entered_address, entered_mask):
    # Convert mask to int value and split entered address to 4 octets
    mask = int(entered_mask)
    ip_address = entered_address.split('.')
    # Assign received octets to variables
    ip1, ip2, ip3, ip4 = [
        int(ip_address[0]),
        int(ip_address[1]),
        int(ip_address[2]),
        int(ip_address[3]),
    ]
    # Assign IP's bin values octets to variables
    bin_ip1, bin_ip2, bin_ip3, bin_ip4 = [
        format(ip1, '08b'),
        format(ip2, '08b'),
        format(ip3, '08b'),
        format(ip4, '08b')
    ]
    # Get bin value ip, netmask, network, wildcard mask, broadcast address, min and max usable address
    bin_mask = ('1' * mask) + ('0' * (32 - mask))
    bin_wild_mask = ext_func.to_revert_mask(bin_mask)
    bin_ip = str(bin_ip1) + str(bin_ip2) + str(bin_ip3) + str(bin_ip4)
    bin_network = str(bin_ip[0:mask] + ('0' * (32 - mask)))
    bin_broadcast = str(bin_ip[0:mask] + ('1' * (32 - mask)))
    bin_min = bin_network[0:31] + '1'
    bin_max = bin_broadcast[0:31] + '0'

    # Get amount usable host
    value_of_hosts = abs(int(bin_network, 2) - int(bin_max, 2))
    # Assign bin values octets to variables in the format xN, where x - type of address, N - value of octet
    # Broadcast
    b1, b2, b3, b4 = [
        int(bin_broadcast[0:8], 2),
        int(bin_broadcast[8:16], 2),
        int(bin_broadcast[16:24], 2),
        int(bin_broadcast[24:32], 2),
    ]
    # Min usable IP address
    min1, min2, min3, min4 = [
        int(bin_min[0:8], 2),
        int(bin_min[8:16], 2),
        int(bin_min[16:24], 2),
        int(bin_min[24:32], 2),
    ]

    # Max usable IP address
    max1, max2, max3, max4 = [
        int(bin_max[0:8], 2),
        int(bin_max[8:16], 2),
        int(bin_max[16:24], 2),
        int(bin_max[24:32], 2),
    ]

    # Netmask(mask)
    m1, m2, m3, m4 = [
        int(bin_mask[0:8], 2),
        int(bin_mask[8:16], 2),
        int(bin_mask[16:24], 2),
        int(bin_mask[24:32], 2),
    ]

    # Network
    n1, n2, n3, n4 = [
        int(bin_network[0:8], 2),
        int(bin_network[8:16], 2),
        int(bin_network[16:24], 2),
        int(bin_network[24:32], 2),
    ]

    # Wildcard mask
    w1, w2, w3, w4 = [
        int(bin_wild_mask[0:8], 2),
        int(bin_wild_mask[8:16], 2),
        int(bin_wild_mask[16:24], 2),
        int(bin_wild_mask[24:32], 2),
    ]
    return print(templates.template.format(0, ip1, ip2, ip3, ip4),
                 templates.template_mask.format(mask, m1, m2, m3, m4),
                 templates.template_wild_mask.format(0, w1, w2, w3, w4),
                 templates.template_network.format(0, n1, n2, n3, n4),
                 templates.template_broadcast.format(0, b1, b2, b3, b4),
                 templates.template_min.format(0, min1, min2, min3, min4),
                 templates.template_max.format(0, max1, max2, max3, max4),
                 f"Total usable host's: {value_of_hosts}"
                 )
