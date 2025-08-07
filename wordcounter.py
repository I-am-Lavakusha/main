#This is the program to count the number of words in a sentence.

def count_words(sentence):
    words = sentence.split()
    return len(words)
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    word_count = count_words(sentence)
    print(f"The number of words in the sentence is: {word_count}")
    