import time

quiz_questions = [("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2), ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3), ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1)]

score = 0
for question in quiz_questions:
    print(question[0])
    for index, option in enumerate(question[1]):
        print(f'{index + 1}. {option}')
    option = int(input('Your answer (1/2/3/4): '))

    if option == question[2]:
        print('Correct!')
        score += 1
    else:
        print(f'Wrong! The correct answer was {question[2]}. {question[1][question[2] - 1]}')
    
    time.sleep(1)
    

print(f'Final score: {score}')