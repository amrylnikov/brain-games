from brain_games.scripts.engine import run
from brain_games.games import brain_calc_game


def main():
    print('DECS: ', brain_calc_game.DESCRIPTION)
    run(brain_calc_game.DESCRIPTION, brain_calc_game.calc)


if __name__ == '__main__':
    main()
