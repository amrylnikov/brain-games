import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    question = str(number1) + ' ' + str(number2)
    true_answer = math.gcd(number1, number2)
    return question, str(true_answer)
