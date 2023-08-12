import random
import math

DESCRIPTION = (
    "Answer \"yes\" if given number is prime. Otherwise answer "
    "\"no\"."
)


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_prime():
    question = random.randint(0, 100)
    true_answer = 'yes' if is_prime(question) else 'no'
    return question, true_answer