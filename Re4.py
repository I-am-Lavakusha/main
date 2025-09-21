# this is the program to find the ip address and the interfaces also found the status and protocol coloums and all this done using the regular expressions.
import re
input1=""""
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        192.168.1.1     YES manual up                    up
FastEthernet0/1        unassigned      YES unset administratively down down
FastEthernet0/2        192.168.1.2     YES manual up                    up
FastEthernet0/3        192.168.1.3     YES manual down                  down
GigabitEthernet0/0     10.0.0.1        YES manual up                    up
"""

pattern1=r"^(\S+\d+)"
interfaces=re.findall(pattern1, input1, re.MULTILINE)
print(interfaces)

pattern2=r"^\S+\s+(\S+\d+ | unassigned)"
ip=re.findall(pattern2, input1, re.MULTILINE)
print(ip)

pattern3=r"^(\S+)\s+\S+\s+\S+\s+\S+\s+(administratively down|up|down)\s+(\S+)"
active=re.findall(pattern3, input1, re.MULTILINE)
print(active)

dict1={}
for interface, status, protocol in active:
  if status=="up" and protocol=="up":
    print(f"The interface{interface} status is {status} and protocols is {protocol}")

for interface, status, protocol in active:
  dict1[interface]={"status": status, "protocol":protocol}

print(dict1)