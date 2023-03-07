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
            print('\'', answer, '\' is wrong answer ;(. Correct answer was \'', true_answer, '\'.', 
                  '\nLet\'s try again, ', name, '!', sep = '')
            break

def progression():
    progression_length = random.randint(5, 10)
    first_number = random.randint(0, 10)
    progression_step = random.randint(0, 10)
    hidden_number = random.randint(0, progression_length - 1)
    a = [0]*progression_length
    question_string = ''
    for i in range (progression_length):
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