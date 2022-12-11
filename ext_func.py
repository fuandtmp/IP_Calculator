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
