num1 = 1202
num2 = 45
num3 = 320

highest_number = 0

if num1 > num2 and num1 > num3:
    highest_number = num1
elif num2 > num1 and num2 > num3:
    highest_number = num2
else:
    highest_number = num3

print(f"The largest number is: {highest_number}")
