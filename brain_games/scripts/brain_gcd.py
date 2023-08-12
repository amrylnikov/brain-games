import random
import math

from brain_games.scripts.engine import run


def gcd_brain():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    question = str(number1) + ' ' + str(number2)
    true_answer = math.gcd(number1, number2)
    return question, str(true_answer)


def main():
    condition = 'Find the greatest common divisor of given numbers.'
    run(condition, gcd_brain)


if __name__ == '__main__':
    main()
