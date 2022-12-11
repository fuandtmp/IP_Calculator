# IP Calculator

My first small python project. During the study of python I will add functionality and fix bugs.


## Features

- Displays netmask, wildcard, network, broadcast, hostmin, hostmax, and hosts in use.
- Displays binary values

## Known bugs

- Incorrect value of the maximum and minimum IP address with a mask of 31 and 32.
- There is no validation of the entered mask.


## Usage

Download the project

```sh
git clone https://github.com/fuandtmp/IP_Calculator.git
cd IP_Calculator
```

After that execute main.py:

```sh
python3 main.py
```
and follow the command:
```sh
Please, enter the address: 192.168.0.1
Please, choose the mask: 24
```
Get the result:
```sh
IP Address: 192.168.0.1
Bin IP 11000000.10101000.00000000.00000001
 
CIDR: /24
Mask: 255.255.255.0
Bin mask: 11111111.11111111.11111111.00000000
 
Wildcard: 0.0.0.255
Bin wildcard mask: 00000000.00000000.00000000.11111111
 
Network: 192.168.0.0
Bin network: 11000000.10101000.00000000.00000000
 
Broadcast address: 192.168.0.255
Bin address 11000000.10101000.00000000.11111111
 
Min IP Address: 192.168.0.1
Bin min IP 11000000.10101000.00000000.00000001
 
Max IP Address: 192.168.0.254
Bin max IP 11000000.10101000.00000000.11111110
 Total usable host's: 254
```
README.md Made by https://dillinger.io/
