#!/usr/bin/env python3
import prompt
import os
import sys
import inspect

#sys.path.insert(1, r'C:\Users\Алексей\PycharmProjects\python-project-49\brain_games')
#from cli import welcome_user

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import cli

def main():
    print('Welcome to the Brain Games!')
    cli.welcome_user()

if __name__ == '__main__':
    main()
