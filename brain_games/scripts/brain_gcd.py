import random
import math
import prompt


def game_body(condition_outrut, input_type, generation_func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print(condition_outrut)
    counter = 0
    while counter < 3:
        # condition
        number, true_answer = generation_func()
        print('Question:', number)
        if input_type == 'string':
            answer = prompt.string('Your answer: ')
        else:
            answer = prompt.integer('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            counter += 1
        else:
            print('\'', answer,
                  '\' is wrong answer ;(. Correct answer was \'',
                  true_answer, '\'.',
                  '\nLet\'s try again, ', name, '!', sep='')
            break
    if counter == 3:
        print('Congratulations, ', name, '!', sep='')


def gcd_brain():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    number = str(number1) + ' ' + str(number2)
    true_answer = math.gcd(number1, number2)
    return number, true_answer


def main():
    condition = 'Find the greatest common divisor of given numbers.'
    input_type = 'integer'
    game_body(condition, input_type, gcd_brain)


if __name__ == '__main__':
    main()
