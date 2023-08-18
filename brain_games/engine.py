import prompt

from brain_games.cli import welcome_user

CYCLE_NUMBER = 3


def run(game_module):
    name = welcome_user()
    print(game_module.DESCRIPTION)
    for _ in range(CYCLE_NUMBER):
        question, answer = game_module.generate_question_and_answer()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"\'{user_answer}\' is wrong answer ;(. Correct ", end="")
            print(f"answer was \'{answer}\'.\nLet\'s try again, {name}!")
            return
        print('Correct!')
    print('Congratulations, ', name, '!', sep='')
