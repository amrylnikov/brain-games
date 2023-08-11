import random

from brain_games.scripts.engine import game_body


def is_prime(var):
    is_prime = False
    for i in range(2, var // 2 + 1):
        if (var % i == 0):
            (is_prime) = True
    if (is_prime):
        return 'no'
    else:
        return 'yes'


def prime():
    question = random.randint(0, 100)
    true_answer = is_prime(question)
    return question, true_answer


def main():
    condition = 'Answer \"yes\" if given number is prime. Otherwise answer ' \
                '\"no\".'
    input_type = 'string'
    game_body(condition, input_type, prime)


if __name__ == '__main__':
    main()
