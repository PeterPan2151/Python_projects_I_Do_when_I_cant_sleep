list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged_list = list1 + list2
final_list = [i for i in merged_list if merged_list.count(i) == 1]

print(final_list)
