shopping_list = ["apples", "bananas", "oranges", "milk", "bananas", "bread", "apples"]

new_list = []
for i in shopping_list:
    if i not in new_list:
        new_list.append(i)

print(sorted(new_list))