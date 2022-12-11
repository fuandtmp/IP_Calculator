# Version 0.2.0
# In future this will be telegram bot
import ip_calc
import ext_func

# This flag is required to enter the IP address and mask indefinitely until the correct value is entered.
flag = True
while flag:
    # Get IP address and mask from user
    entered_address = input('Please, enter the address: ')
    entered_mask = input('Please, choose the mask: ')
    try:
        # Checking if the entered IP address is correct
        if ext_func.to_check_ip_address(entered_address):
            # To calculate entered IP and mask
            ip_calc.ip_calculator(entered_address, entered_mask)
            # After calculating the correctly entered IP address, exit the calculator
            flag = False
        else:
            # Notify the user that the entered IP is incorrect and it is necessary to enter the correct address in the
            # required format
            print(f'Please enter a valid IP value in the format "192.168.0.1". Previously entered = {entered_address}')
    except IndexError:
        print(f'Please do not enter null or empty value. Previously entered = {entered_address}')


