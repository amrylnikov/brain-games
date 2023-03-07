#!/usr/bin/env python3
import os
import sys
import inspect
import prompt

currentdir = os.path.dirname(os.path.abspath
                             (inspect.getfile
                              (inspect.currentframe(
                              ))))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# from cli import welcome_user


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    return name


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
