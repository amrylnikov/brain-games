import random

from brain_games.scripts.engine import run


def progression():
    progression_length = random.randint(5, 10)
    first_number = random.randint(0, 10)
    progression_step = random.randint(0, 10)
    hidden_index = random.randint(0, progression_length - 1)

    # можно переписать попитонистей
    display_list = [0] * progression_length
    question = ''
    for i in range(progression_length):
        display_list[i] = str(first_number + progression_step * (i + 1))
        if i == hidden_index:
            question += '..' + ' '
        else:
            question += display_list[i] + ' '

    true_answer = int(display_list[hidden_index])
    display_list[hidden_index] = '..'
    return question, str(true_answer)


def main():
    condition = 'What number is missing in the progression?'
    run(condition, progression)


if __name__ == '__main__':
    main()
