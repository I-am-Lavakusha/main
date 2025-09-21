# this is the program to find the ip and to print the ip that has the count more than one
import re
input1="""
2025-09-10 12:01:45 INFO User login from 192.168.1.10
2025-09-10 12:03:21 ERROR Failed connection attempt from 10.0.0.5
2025-092025-09-10 12:01:45 INFO User login from 192.168.1.10
2025-09-10 12:03:21 ERROR Failed connection attempt from 10.0.0.5
2025-09-10 12:05:12 INFO User logout from 172.16.0.7
2025-09-10 12:07:33 WARN Suspicious traffic from 192.168.
"""
pattern=r"\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+(\S+\d+)"

list1=re.findall(pattern, input1)

dict1={}

for ip in list1:
  if ip in dict1:
    dict1[ip]+=1
  else:
    dict1[ip]=1

for count in dict1:
  if dict1[count]>1:
    print(f"the {count} have count {dict1[count]}")

