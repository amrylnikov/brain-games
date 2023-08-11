import random

from brain_games.scripts.engine import game_body


def even():
    number = random.randint(0, 100)
    if number % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return number, true_answer


def main():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    input_type = 'string'
    game_body(condition, input_type, even)


if __name__ == '__main__':
    main()
