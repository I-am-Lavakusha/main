# this is the program to find the character that has more frequency using dictionary
string="forgot"
dict={}
max=0
for w in string:
  if w in dict:
    dict[w]+=1
  else:
    dict[w]=1
for i, j in dict.items():
  if j>max:
    max=j
    maxkey=i
print(f"The max key is {maxkey} and maxvalue is {max}")