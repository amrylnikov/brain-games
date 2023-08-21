import random

DESCRIPTION = 'What is the result of the expression?'


def generate_question_and_answer():
    number1 = random.randint(0, 20)
    number2 = random.randint(0, 20)
    options = ('+', '-', '*')
    operator = random.choice(options)
    question = f'{number1} {operator} {number2}'
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return question, str(answer)
