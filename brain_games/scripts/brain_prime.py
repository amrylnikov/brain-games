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
                  '\nLet\'s try again, ', name, '!', sep='')
            break
    if counter == 3:
        print('Congratulations, ', name, '!', sep='')


def is_prime(a):
    Flag = False
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            Flag = True
    if (Flag):
        return 'no'
    else:
        return 'yes'


def prime():
    number = random.randint(0, 100)
    true_answer = is_prime(number)
    return number, true_answer


def main():
    condition = ('Answer \"yes\" if given number\
                  is prime. Otherwise answer \"no\".')
    input_type = 'string'
    game_body(condition, input_type, prime)


if __name__ == '__main__':
    main()
