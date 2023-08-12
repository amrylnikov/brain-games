import prompt


def run(module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print(module.DESCRIPTION)
    for _ in range(3):
        question, true_answer = module.generate_question_and_answer()
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
