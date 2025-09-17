# this ia the program to find the frequency of the strings that are present in a sentence using dictionary
sentence="if you love something set it free if it comes back it is yours if not it never was"
words=sentence.split()
freq={}
for w in words:
  if w in freq:
    freq[w]+=1
  else:
    freq[w]=1
print(freq)