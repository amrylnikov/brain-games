#!/usr/bin/env python3
import os
import sys
import inspect
import random
import prompt

currentdir = os.path.dirname(os.path.abspath
                             (inspect.getfile
                              (inspect.currentframe(
                              ))))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = random.randint(0,100)
        if number % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'
        print('Question: ', number)
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            counter += 1
        else:
            print('\'', answer, '\' is wrong answer ;(. Correct answer was \'', true_answer, '\'.', 
                  '\nLet\'s try again, ', name, sep = '')
            break


if __name__ == '__main__':
    main()
