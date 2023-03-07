import random
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
                  '\nLet\'s try again, ', name, '!', sep = '')
            break
    if counter == 3:
        print('Congratulations, Sam!')


def calc():
    number1 = random.randint(0,20)
    number2 = random.randint(0,10)
    options = '+','-','*'
    operator = random.choice(options)
    print (operator)
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
