#program to count the number of letters in a string
def count_letters(string):
    count = 0
    for char in string:
        if char.isalpha():  
            count += 1
    return count
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    letter_count = count_letters(input_string)
    print(f"The number of letters in the string is: {letter_count}")
# This program counts the number of letters in a given string, ignoring spaces and punctuation.