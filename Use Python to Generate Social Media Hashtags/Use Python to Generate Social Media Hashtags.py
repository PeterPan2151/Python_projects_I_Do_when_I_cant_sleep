hashtag = input('Enter a Phrase for your hastag: ').split(' ')
message = []
for word in hashtag:
    message.append(word.capitalize())

print(f'#{''.join(message)}')