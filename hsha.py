#!/usr/bin/python3
# hsha v1.0

# Dependencies
from hashlib import sha256
from sys import exit

import os
import getpass


# Colors
class Colors:
    WHITE = "\033[37m"
    RED = "\033[31m"
    MAGENTA = "\033[32m"


# Welcome
def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = open('banner.txt', 'r').read()
    print(f'{Colors.MAGENTA}{banner}{Colors.WHITE}\n')


# Hash Function
def hashing(s):
    welcome()

    print(sha256(s.encode()).hexdigest())


# Main
if __name__ == '__main__':
    welcome()

    print('-------------')
    print('$ Hash Mode $')
    print('-------------\n')
    print('[1] File')
    print('[2] Text\n\n> ', end='')
    choice = input().lower()

    if choice == '1' or choice == 'file' or choice == 'f':
        welcome()

        # Get current dir
        os.chdir(os.path.dirname(__file__))
        d = os.getcwd()

        print(f'Current directory:\n{d}')

        while True:
            it = input(f'\n[+] File route: ').lower()

            if it == 'help*' or it == 'h*':
                print(' \ndownloads* / d* > Goes to the download directory')

            elif it == 'downloads*' or it == 'd*':
                down = input('[+] Download name: ')
                i = f'C:/Users/{getpass.getuser()}/Downloads/{down}'
                break

            else:
                i = it
                break


        # Open & Read the file
        try:
            s = open(i, 'r', encoding='cp850').read()
        except:
            print(f"\n{Colors.RED}Can't open the file...{Colors.WHITE}")
            exit()

    elif choice == '2' or choice == 'text' or choice == 't':
        welcome()
        s = input('[+] Text: ')

    else:
        exit()

    hashing(s)
    
