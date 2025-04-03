full_name = input('Please enter your full name: ')
print(f'Your name in uppercase: {full_name.upper()}')
print(f'Your name in lowercase: {full_name.lower()}')
spaces = full_name.count(' ')
characters = len(full_name) - spaces
print(f'Total number of characters(excluding spaces): {characters}')
print(f'Your name reversed: {full_name[::-1]}')