import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    question = random.randint(0, 100)
    true_answer = 'yes' if question % 2 == 0 else 'no'
    return question, true_answer
