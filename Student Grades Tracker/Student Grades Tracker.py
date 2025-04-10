grades = {}

while True:
    print('Menu:')
    print('1. Add a student and their grade\n2. View all students and their grades\n3. exit')
    option = int(input('Choose an option (1-3): '))

    if option == 3:
        break
    elif option == 1:
        student_name = input('Enter the student\'s name: ')
        grade = input(f'Enter {student_name}\'sgrade: ')
        grades[student_name] = grade
        print(f'{student_name}\'s grade has been added')

    elif option == 2:
        print(grades)