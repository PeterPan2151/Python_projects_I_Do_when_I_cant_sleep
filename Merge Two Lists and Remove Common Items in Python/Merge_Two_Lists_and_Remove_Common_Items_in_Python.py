list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged_list = list1 + list2
final_list = []
for i in merged_list:
    if merged_list.count(i) > 1:
        continue
    else:
        final_list.append(i)


print(final_list)
