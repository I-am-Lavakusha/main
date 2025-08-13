def list_of_list(input_str):
  lines=input_str.strip().split("\n")
  first_line=lines[0]
  result=[]

  for i in range (1, len(lines), 2):
    sublist=[first_line]

    if i<len(lines):
      sublist.append(lines[i])
    
    if i+1<len(lines):
      sublist.append(lines[i+1])

    result.append(sublist)
  return result

input_str="""first line
second line
third line
fourth line
fifth line
india
karnataka
tamilnaadu"""

output=list_of_list(input_str)
print(output)