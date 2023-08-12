import prompt


# надо передавать... модуль?
def run(condition_output, generation_func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print(condition_output)
    for _ in range(3):
        question, true_answer = generation_func()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
        else:
            return print(
                f"\'{answer}\' is wrong answer ;(. Correct answer was "
                f"\'{true_answer}\'."
                f"\nLet\'s try again, {name}!"
            )
    print('Congratulations, ', name, '!', sep='')
