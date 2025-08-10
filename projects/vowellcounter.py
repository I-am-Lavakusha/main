#Count Vowels in a String
s = "hello world"
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print("Vowel count:", count)