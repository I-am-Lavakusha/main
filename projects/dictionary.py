# this is the program to create a dictionary using the 2 lists

Keys = ['name', 'age', 'city']
Values = ['Lavkumar', 23, 'Bengaluru']
dict1={}
for key in range(len(Keys)):
  if key in dict1:
    dict1[Keys[key]]=Values[key]
  else:
    dict1[Keys[key]]=Values[key]
print(dict1)
