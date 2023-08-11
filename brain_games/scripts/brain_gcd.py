import random
import math

from brain_games.scripts.engine import game_body


def gcd_brain():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    number = str(number1) + ' ' + str(number2)
    true_answer = math.gcd(number1, number2)
    return number, true_answer


def main():
    condition = 'Find the greatest common divisor of given numbers.'
    input_type = 'integer'
    game_body(condition, input_type, gcd_brain)


if __name__ == '__main__':
    main()
