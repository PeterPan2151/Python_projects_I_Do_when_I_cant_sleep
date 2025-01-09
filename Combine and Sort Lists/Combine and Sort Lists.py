list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

full_list = list1 + list2
unique_items_list = []
for i in full_list:
    if i not in unique_items_list:
        unique_items_list.append(i)

unique_items_list.sort()
print(unique_items_list)
