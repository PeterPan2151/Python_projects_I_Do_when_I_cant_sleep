while True:
    word = input('Enter a word in Language 1 (or type "done" to finish): ')
    if word == 'done':
        break
    elif word:
        translation = input(f'Enter the translation of \'{word}\'in Language 2: ')

        with open('./Easy Bilingual Vocabulary with Python/words.txt', 'r') as file:
            content = file.readlines()

        line = '\n' + f'{word} - {translation}'
        content.append(line)

        with open('./Easy Bilingual Vocabulary with Python/words.txt', 'w') as file:
            file.writelines(content)
    else:
        print('Please enter a word')