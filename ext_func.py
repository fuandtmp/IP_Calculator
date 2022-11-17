# Some legacy shit
# import re
# def is_correct_ip_address(address):
#     pattern_of_address = re.compile(
#         r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|('
#         r'[1-9]?\d))))')
#     if pattern_of_address.search(address) is not None:
#         return True
#     else:
#         return False
# def is_correct_mask(mask):
#     if (mask < 0) or (mask > 32):
#         return False
#     else:
#         return True

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
