import prompt


# переименовать в run
# надо передавать... модуль?
def run(condition_output, generation_func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print(condition_output)
    counter = 0
    # вместо while -> for i in range 3
    while counter < 3:
        question, true_answer = generation_func()
        print('Question:', question)
        # без инпут тайпа, всегда стринг передавай и выдавай
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            counter += 1
        else:
            # переписать в строковом варианте (f который)
            print('\'', answer,
                  '\' is wrong answer ;(. Correct answer was \'',
                  true_answer, '\'.',
                #   И это вторым принтом через f, ибо читается проще
                  '\nLet\'s try again, ', name, '!', sep='')
            break
    if counter == 3:
        print('Congratulations, ', name, '!', sep='')
