import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_question_and_answer():
    progression_length = random.randint(5, 10)
    first_number = random.randint(0, 10)
    progression_step = random.randint(0, 10)
    hidden_index = random.randint(0, progression_length - 1)

    progression_list = [
        str(first_number + progression_step * (i + 1))
        for i in range(progression_length)
    ]
    answer = progression_list[hidden_index]
    progression_list[hidden_index] = '..'
    question = ' '.join(progression_list)
    return question, answer
