import random
import math

from brain_games.scripts.engine import run


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def prime():
    question = random.randint(0, 100)
    true_answer = 'yes' if is_prime(question) else 'no'
    return question, true_answer


def main():
    condition = (
        "Answer \"yes\" if given number is prime. Otherwise answer "
        "\"no\"."
    )
    run(condition, prime)


if __name__ == '__main__':
    main()
