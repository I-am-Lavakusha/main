# this is the program to find the ip address, ip address with their type and traversed to find the type and also mac address
import re
input2="""
  Internet Address      Physical Address      Type
  192.168.1.1          00-14-22-01-23-45     dynamic
  192.168.1.10         3c-52-82-6b-7f-1a     dynamic
  192.168.1.20         00-25-96-ab-cd-ef     dynamic
  192.168.1.100        08-00-27-12-34-56     static
"""

pattern1=r"(\S+\d+)\s+\S+\s+"
pattern2=r"(\S+\d+)\s+\S+\s+(dynamic|static)"
result1=re.findall(pattern1, input2)
result2=re.findall(pattern2, input2)
dict1={}
for ip in result1:
  if ip in dict1:
    dict1[ip]+=1
  else:
    dict1[ip]=1

print(dict1)

dict2=dict(result2)
for key2 in dict2:
  if dict2[key2]=="static":
    print(f"the ip addresses that are static are {key2}")
  else:
    print(f"the ip addresses that are dynamic are {key2}")

print(dict2)

dict3={}

search3=r"\S+\s+(\S+\-\S+)\s+\S+"
pattern3=re.findall(search3, input2)

for search in pattern3:
  if search in dict3:
    dict3[search]+=1

  else:
    dict3[search]=1
print(dict3)



# dict1={
#   "name":"lava",
#   "brand":"mybrand"
# }
# for key1 in dict1:
#   print(dict1[key1])