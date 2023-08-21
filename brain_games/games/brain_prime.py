import random
import math

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_question_and_answer():
    question = random.randint(2, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
