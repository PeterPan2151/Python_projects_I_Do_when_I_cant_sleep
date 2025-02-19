mylist = ['a', 'b', 'c']
new_list = []

for i, j in enumerate(mylist):
    new_list.append((j, i))

print(new_list)