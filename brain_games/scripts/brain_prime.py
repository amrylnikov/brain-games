import random

from brain_games.scripts.engine import run


def is_prime(num):
    # считает и отрицательные, а низзя.
    is_prime = False
    # Можно сделать алгоритм проще. Погугли
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            (is_prime) = True
            # если нашёл ретёрн делай
    # иначе ретёрн фалс
    if (is_prime):
        # Пусть отдаёт логические значегия, иначе грустно
        return 'no'
    else:
        return 'yes'


def prime():
    question = random.randint(0, 100)
    true_answer = is_prime(question)
    return question, true_answer


def main():
    # неправильно перенёс, погугли как надо
    condition = 'Answer \"yes\" if given number is prime. Otherwise answer ' \
                '\"no\".'
    run(condition, prime)


if __name__ == '__main__':
    main()
