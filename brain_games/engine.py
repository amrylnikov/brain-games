import prompt

from brain_games.cli import welcome_user

GAME_MAX_CYCLE_NUMBER = 3


def run(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(GAME_MAX_CYCLE_NUMBER):
        question, answer = game.generate_question_and_answer()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(
                f'\'{user_answer}\' is wrong answer ;(.'
                f'Correct answer was \'{answer}\'.'
                f'\nLet\'s try again, {name}!'
            )
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
