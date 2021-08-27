#!/usr/bin/python3
# hsha v1.0

# Dependencies
from hashlib import sha256
from sys import exit

import os
import getpass


# Welcome
def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = open('banner.txt', 'r').read()
    print(banner)


# Hash Function
def hashing(s):
    welcome()

    print(sha256(s.encode()).hexdigest())


# Main
if __name__ == '__main__':
    welcome()

    choice = input('$ Hash Mode $\n\n[1] File\n[2] Text\n\n> ').lower()

    if choice == '1' or choice == 'file' or choice == 'f':
        welcome()

        # Get current dir
        os.chdir(os.path.dirname(__file__))
        d = os.getcwd()

        print(f'Current directory:\n{d}')

        while True:
            it = input(f'\n[+] File route: ').lower().replace(' ', '')

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
            print("\nCan't open the file...")
            exit()

    elif choice == '2' or choice == 'text' or choice == 't':
        welcome()
        s = input('\n[+] Text: ')

    else:
        exit()

    hashing(s)
