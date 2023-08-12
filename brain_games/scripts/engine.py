import prompt


# надо передавать... модуль?
def run(module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print(module.DESCRIPTION)

    function = None

    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if callable(attr):
            function = attr
            break

    if function is None:
        print("No callable function found in the module!")
        return

    for _ in range(3):
        question, true_answer = function()
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
