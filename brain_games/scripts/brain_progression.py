import random

from brain_games.scripts.engine import game_body


def progression():
    progression_length = random.randint(5, 10)
    first_number = random.randint(0, 10)
    progression_step = random.randint(0, 10)
    hidden_number = random.randint(0, progression_length - 1)
    a = [0] * progression_length
    question_string = ''
    for i in range(progression_length):
        a[i] = str(first_number + progression_step * (i + 1))
        if i == hidden_number:
            question_string += '..' + ' '
        else:
            question_string += a[i] + ' '

    true_answer = int(a[hidden_number])
    a[hidden_number] = '..'
    return question_string, true_answer


def main():
    condition = 'What number is missing in the progression?'
    input_type = 'integer'
    game_body(condition, input_type, progression)


if __name__ == '__main__':
    main()
