import re

input1="""
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, * - candidate default

Gateway of last resort is 192.168.1.1 to network 0.0.0.0

C    192.168.1.0/24 is directly connected, FastEthernet0/0
L    192.168.1.1/32 is directly connected, FastEthernet0/0
O    10.0.0.0/8 [110/2] via 192.168.1.2, 00:00:12, FastEthernet0/1
S    172.16.0.0/16 [1/0] via 192.168.1.3
C    192.168.2.0/24 is directly connected, FastEthernet0/2
"""

pattern1=r"\S+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d+)"
networks=re.findall(pattern1, input1, re.MULTILINE)
print(networks)

