# this is the program to find the vlan mac address and the ports using regular expressions
import re
input1="""
Vlan    Mac Address       Type        Ports
  10    00a1.b2c3.d4e5    DYNAMIC     Fa0/1
  20    00b2.c3d4.e5f6    DYNAMIC     Fa0/2
  30    00c3.d4e5.f6g7    DYNAMIC     Fa0/3
  10    00a1.b2c3.d4e6    DYNAMIC     Fa0/4
  20    00b2.c3d4.e5f7    DYNAMIC     Fa0/5
  30    00c3.d4e5.f6g8    DYNAMIC     Fa0/6
  10    00a1.b2c3.d4e9    DYNAMIC     Fa0/7
"""
mac=r"(\S+\.\S+)"
pattern1=re.findall(mac, input1)
print(pattern1)

vlan=r"^\s*(\d+)"
pattern2=re.findall(vlan, input1, re.MULTILINE)
print(pattern2)

interface=r"(\S+\d+)$"
pattern3=re.findall(interface, input1, re.MULTILINE)
print(pattern3)
