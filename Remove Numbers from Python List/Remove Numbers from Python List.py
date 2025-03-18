# Project Description
# Imagine you have a list of ages or transaction amounts, but you want to remove all the numbers that are below a certain threshold—like filtering out low amounts from financial transactions. This project is about removing unwanted numbers and cleaning up your data.

# How the Program Works
# Start the program by defining this list at the top of the script:

# numbers = [23, 45, 12, 67, 89, 10, 4, 33]
# Then, add some code that prints out the list without the numbers that are less than 20.

numbers = [23, 45, 12, 67, 89, 10, 4, 33]
valid_numbers = []

for i in numbers:
    if i >= 20:
        valid_numbers.append(i)
print(valid_numbers)
