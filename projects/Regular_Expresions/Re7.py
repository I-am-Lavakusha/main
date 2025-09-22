# this is the program to find the ip, neighbour id, dead time , and interfaces

import re

input1="""
Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:34    192.168.1.2     FastEthernet0/0
3.3.3.3           1   FULL/BDR        00:00:39    192.168.1.3     FastEthernet0/1
4.4.4.4           1   2WAY/DROTHER    00:00:32    192.168.1.4     FastEthernet0/2
"""
lines=input1.strip().splitlines()[1:]
data="\n".join(lines)
print(data)

neighbour_id=re.findall(r"^(\S+\d+)", data, re.MULTILINE)
print(neighbour_id)

ospf_states=re.findall(r"^\S+\s+\S+\s+(\S+/\S+)", data, re.MULTILINE)
print(ospf_states)

dead_times=re.findall(r"\d+:\d+:\d+", data, re.MULTILINE)
print(dead_times)

neighbour_ip=re.findall(r"^\S+\s+\S+\s+\S+\s+\S+\s+(\S+\d+)", data, re.MULTILINE)
print(neighbour_ip)

interfaces=re.findall(r"(\S+\d+)$", data, re.MULTILINE)
print(interfaces)