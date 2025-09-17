# this is the program to swap the key and values in 2 different dictionaries and making it to a single dictionary

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3={}
for i, j in dict1.items():
  dict3[j]=i
for k, l in dict2.items():
  dict3[l]=k

print(dict3)
