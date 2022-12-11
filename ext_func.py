# This function to convert mask to wildcard mask
def to_revert_mask(mask_of_network):
    i = 0
    wild_mask = ''
    while i < 32:
        if '1' in mask_of_network[i]:
            wild_mask += mask_of_network[i].join('0')
            i += 1
        else:
            wild_mask += mask_of_network[i].join('1')
            i += 1
    return wild_mask


def to_check_ip_address(ip_address):
    if ip_address.strip().replace(".", "").isdigit():
        split_address = ip_address.split(".")
        first_octet = int(split_address[0])
        i = 0
        while i < 4:
            if -1 < int(split_address[i]) < 256:
                i += 1
            else:
                return False
        if first_octet <= 0:
            return False
        return True
    else:
        return False
