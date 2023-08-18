import prompt

from brain_games.cli import welcome_user


def run(game_module):
    name = welcome_user()
    print(game_module.DESCRIPTION)
    for _ in range(3):
        question, true_answer = game_module.generate_question_and_answer()
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
