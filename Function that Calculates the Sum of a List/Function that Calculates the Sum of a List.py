# Version 1
# def sum_numbers(nums: list):
#     total = 0
#     for n in nums:
#         total += int(n)
#     return total

# numbers_list = input('Enter numbers seperated by a comma: ').split(',')
# print(sum_numbers(numbers_list))

# Version 2
def sum_numbers(nums: list):
    numbers = [int(n) for n in nums]
    return sum(numbers)

numbers_list = input('Enter numbers seperated by a comma: ').split(',')
print(sum_numbers(numbers_list)) 