# Version 0.2.0
# In future this will be telegram bot
import ip_calc

# Get IP address and mask from user
entered_address = input('Please, enter the address: ')
entered_mask = input('Please, choose the mask: ')
# To calculate entered IP and mask
ip_calc.ip_calculator(entered_address, entered_mask)
