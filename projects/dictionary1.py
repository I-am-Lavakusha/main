# program to find the frequency of the characters present in a string using dictionary

str1="cisco"
dict1={"in":2, "out":40, "mid":{
  1:"a", 2:"ab", 3:"abc"
}}
for word in str1:
  if word in dict1:
    dict1[word]+=1
  else:
    dict1[word]=1
for i, j in dict1.items():
  if isinstance(j, dict):
    for l, k in j.items():
      print(l,k)
  print(i,j)

