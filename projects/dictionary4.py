# this is the program to find the maximum marks and minimum marks in a dictionary
marks = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
min=marks.get("Alice")
print(min)
max=-1
maxkey, minkey="", ""
for i,j in marks.items():
  if j>max:
    max=j
    maxkey=i
  if min>j:
    min=j
    minkey=i

print(f"the mea marks is {max} and the person scored is {maxkey}")
print(f"the min marks is {min} and the person scored is {minkey}")