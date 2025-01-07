# Project Description
# This project involves creating a program that takes a sentence as input and counts the number of words in that sentence. The program will also identify the longest word in the sentence.


sentence = input("Enter your sentence: ")
words_list = sentence.split(" ")
word_count = len(words_list)
longest_word_length = 0
longest_word = None

for i, j in enumerate(words_list):
    if len(j) > longest_word_length:
        longest_word_length = len(j)
        longest_word = words_list[i]

print(f"There are {word_count} word in the sentence.")
print(f"The longest word is '{longest_word}', with {longest_word_length} characters.")