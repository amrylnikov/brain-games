import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return find_gcd(b, a % b)


def generate_question_and_answer():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    question = f'{number1} {number2}'
    answer = find_gcd(number1, number2)
    return question, str(answer)
