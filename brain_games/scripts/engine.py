import prompt


def game_body(condition_output, input_type, generation_func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print(condition_output)
    counter = 0
    while counter < 3:
        question, true_answer = generation_func()
        print('Question:', question)
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
