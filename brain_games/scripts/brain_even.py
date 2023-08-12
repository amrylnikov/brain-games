import random

from brain_games.scripts.engine import run


def even():
    question = random.randint(0, 100)
    # в одну строчку, он как-то сделал
    true_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), true_answer


def main():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    run(condition, even)


if __name__ == '__main__':
    main()
