import random

from brain_games.scripts.engine import game_body


def is_prime(a):
    Flag = False
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            Flag = True
    if (Flag):
        return 'no'
    else:
        return 'yes'


def prime():
    number = random.randint(0, 100)
    true_answer = is_prime(number)
    return number, true_answer


def main():
    c = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
    input_type = 'string'
    game_body(c, input_type, prime)


if __name__ == '__main__':
    main()
