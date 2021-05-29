#!/usr/bin/python3

from hashlib import sha256
from sys import exit
import os
import getpass


def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = open('banner.txt', 'r').read()
    print(banner)


def hashing(s):
    welcome()

    print(sha256(s.encode()).hexdigest())


def main():
    welcome()

    m = input('$ Hash Mode $\n\n[1] File\n[2] Text\n\n> ').lower()

    if m == '1' or m == 'file' or m == 'f':
        welcome()

        # get current dir
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

        # open & read the file
        try:
            s = open(i, 'r', encoding='cp850').read()
        except:
            print("\nCan't open the file...")
            exit()

    elif m == '2' or m == 'text' or m == 't':
        welcome()
        s = input('\n[+] Text: ')

    else:
        exit()

    hashing(s)


if __name__ == '__main__':
    main()
