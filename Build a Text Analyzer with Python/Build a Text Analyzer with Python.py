text_details = {}
text = input('Enter a block of text for analysis: ')
text_details['Total Characters'] = len(text)
words = text.split(' ')
sentences = text.split('.')
text_details['Total Setences'] = len(sentences)

frequent_word_count = 0
frequent_word = ''
for w in words:
    if words.count(w) > frequent_word_count:
        frequent_word_count = words.count(w)
        frequent_word = w

text_details['Most Frequent Word'] = frequent_word

word_lengths = []
for w in words:
    word_lengths.append(len(w))
average_word_len = sum(word_lengths) / len(words)
text_details['Average word length'] = average_word_len

sentence_length = []
for s in sentences:
    words = s.split(' ')
    sentence_len = len(words)
    sentence_length.append(sentence_len)
average_sentence_len = sum(sentence_length) / len(sentences)
text_details['Avergae Sentence length'] = average_sentence_len

for i, j in text_details.items():
    print(f'{i}: {j}')


