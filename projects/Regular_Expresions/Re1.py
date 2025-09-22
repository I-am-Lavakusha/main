# this is the program to find the networks, nexthops, interrfaces and the hopcount using regular expressions
import re

input1="""
R    10.1.0.0/16 [120/1] via 192.168.1.2, 00:00:12, FastEthernet0/0
R    172.16.0.0/16 [120/2] via 192.168.1.3, 00:00:22, FastEthernet0/1
R    192.168.2.0/24 [120/1] via 192.168.1.4, 00:00:15, FastEthernet0/2
R    192.168.3.0/24 [120/3] via 192.168.1.5, 00:00:30, FastEthernet0/3
"""

destination=re.findall(r"^\S+\s+(\S+\d+)", input1, re.MULTILINE)
print(destination)

nexthop=re.findall(r"^\S+\s+\S+\s+\S+\s+\S+\s+(\S+)", input1, re.MULTILINE)
print(nexthop)

interfaces=re.findall(r"(\S+\d+)$", input1, re.MULTILINE)
print(interfaces)

hopcount=re.findall(r"^\S+\s+\S+\s+\S+/(\d+)", input1, re.MULTILINE)
print(hopcount)




