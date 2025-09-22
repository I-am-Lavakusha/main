# this is the program to find the ospf router and extracted the set of pattern in the output
import re

input1="""
            OSPF Router with ID (1.1.1.1) (Process ID 1)

                Router Link States (Area 0)

Link ID         ADV Router      Age     Seq#       Checksum Link count
2.2.2.2         2.2.2.2         1200    0x80000001 0x00AB   3
3.3.3.3         3.3.3.3         1190    0x80000002 0x00AC   4
4.4.4.4         4.4.4.4         1180    0x80000003 0x00AD   2
"""

lines=input1.strip().splitlines()[5:]
data="\n".join(lines)
print(data)

link_id=re.findall(r"^(\S+\d+)", data, re.MULTILINE)
print(link_id)

adv_routers=re.findall(r"^\S+\s+(\S+\d+)", data, re.MULTILINE)
print(link_id)

link_adv=re.findall(r"^(\S+\d+)\s+(\S+\d+)", data, re.MULTILINE)
liad=[]
for id, adv in link_adv:
  liad.append({"link id":id, "adv_router":adv})
print(liad)

age=re.findall(r"^\S+\s+\S+\s+(\S+\d+)", data, re.MULTILINE)
print(age)

seq=re.findall(r"^\S+\s+\S+\s+\S+\s+(\S+)", data, re.MULTILINE)
print(seq)

checksum=re.findall(r"(\S+)\s+\d+$", data, re.MULTILINE)
print(checksum)

link_count=re.findall(r"^(\S+\d+).*\s(\d+)$", data, re.MULTILINE)
print(link_count)
for linkcount, count in link_count:
  if int(count)>2:
    print(f"The {linkcount} count is {count}")
