import random

from brain_games.scripts.functions.game_body import game_body


def calc():
    number1 = random.randint(0, 20)
    number2 = random.randint(0, 10)
    options = '+', '-', '*'
    operator = random.choice(options)
    number = str(number1) + ' ' + operator + ' ' + str(number2)
    if operator == '+':
        true_answer = number1 + number2
    elif operator == '-':
        true_answer = number1 - number2
    else:
        true_answer = number1 * number2
    return number, true_answer


def main():
    condition = 'What is the result of the expression?'
    input_type = 'integer'
    game_body(condition, input_type, calc)


if __name__ == '__main__':
    main()
