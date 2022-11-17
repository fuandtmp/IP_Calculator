template_network = '''
Network: {1}.{2}.{3}.{4}
Bin network: {1:08b}.{2:08b}.{3:08b}.{4:08b}
'''
template_mask = '''
CIDR: /{0}
Mask: {1}.{2}.{3}.{4}
Bin mask: {1:08b}.{2:08b}.{3:08b}.{4:08b}
'''
template_wild_mask = '''
Wildcard: {1}.{2}.{3}.{4}
Bin wildcard mask: {1:08b}.{2:08b}.{3:08b}.{4:08b}
'''
template = '''
IP Address: {1}.{2}.{3}.{4}
Bin IP {1:08b}.{2:08b}.{3:08b}.{4:08b}
'''
template_broadcast = '''
Broadcast address: {1}.{2}.{3}.{4}
Bin address {1:08b}.{2:08b}.{3:08b}.{4:08b}
'''
template_min = '''
Min IP Address: {1}.{2}.{3}.{4}
Bin min IP {1:08b}.{2:08b}.{3:08b}.{4:08b}
'''
template_max = '''
Max IP Address: {1}.{2}.{3}.{4}
Bin max IP {1:08b}.{2:08b}.{3:08b}.{4:08b}
'''