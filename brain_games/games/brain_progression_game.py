import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_question_and_answer():
    progression_length = random.randint(5, 10)
    first_number = random.randint(0, 10)
    progression_step = random.randint(0, 10)
    hidden_index = random.randint(0, progression_length - 1)

    question = ' '.join([
        str(first_number + progression_step * (i + 1))
        if i != hidden_index else '..'
        for i in range(progression_length)
    ])
    true_answer = str(first_number + progression_step * (hidden_index + 1))
    return question, true_answer
