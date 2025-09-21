# this is the program that is been asked to divya in the review

import re
input1="""
Interface              IP-Address      OK? Method Status        Protocol
GigabitEthernet0/0     192.168.1.1     YES manual up            up
GigabitEthernet0/1     unassigned      YES unset  administratively down down
FastEthernet0/0        10.0.0.1        YES manual up            up
Loopback0              127.0.0.1       YES manual up            up
Vlan1                  172.16.0.1      YES manual down          down
Serial0/0/0            unassigned      YES unset  down          down
"""

search=r"(\S+\d+)\s+\S+\s+\S+\s+\S+\s+(administratively down|up|down)"
result=re.findall(search, input1, re.MULTILINE)
result1=[]
for interface, status in result:
  result1.append({"interface":interface, "status":status})

print(result1)