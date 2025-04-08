sentence_1 = input('Enter sentence 1: ')
sentence_2 = input('Enter sentence 2: ')
sentence_3 = input('Enter sentence 3: ')

sentences = [sentence_1 + '\n-----------\n', sentence_2 + '\n-----------\n', sentence_3 ]

with open('./Store multiple lines in text file with Python/user_sentences.txt', 'w') as file:
    file.writelines(sentences)

print(sentences)
