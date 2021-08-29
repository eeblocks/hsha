#!/usr/bin/python3
# hsha v1.2

# Dependencies
from hashlib import sha256
from sys import exit
from time import sleep, time

import os
import getpass
import argparse

# Colors
class Colors:
    WHITE = "\033[37m"
    RED = "\033[31m"
    GREEN = "\033[32m"


# Welcome
def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = open('banner.txt', 'r', encoding='utf-8').read()
    print(f'{Colors.GREEN}{banner}{Colors.WHITE}\n')


welcome()


# Argument Settings
parser = argparse.ArgumentParser(description='Hash your Files/Text to SHA-256', add_help=True)
parser.add_argument('-t', '--text', action='store', required=False, dest='text', help='Text to SHA-256')
parser.add_argument('-f', '--file', action='store', required=False, dest='file', help='File to SHA-256')
args = parser.parse_args()


# Hash Function
def hashing(s):

    welcome()

    start_time = time()
    encoded = sha256(s.encode()).hexdigest()
    end_time = time()

    elapsed = end_time - start_time

    print(encoded)
    print(f'\nTime elapsed: {Colors.GREEN}{round(elapsed, 2)}s{Colors.WHITE}')
    

# Text Function
def text(t):
    hashing(t)

def file(f):

    try:
        file_open = open(f, 'r', encoding='cp850').read()
        hashing(file_open)
    except:
        print(f'{Colors.RED}Needs to specify the exact path...{Colors.WHITE}')
        exit()

# Main
if __name__ == '__main__':

    if args.text:
        text(args.text)
        exit()

    elif args.file:
        file(args.file)
        exit()

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

        print('\n(help*)')
        while True:
            
            it = input(f'\n[+] File route: ').lower()

            if it == 'help*' or it == 'h*':
                welcome()
                print(' \ndownloads* / d* > Goes to the download directory')

            elif it == 'downloads*' or it == 'd*':
                welcome()

                print(f'Current directory:\nC:/Users/{getpass.getuser()}/Downloads/\n')
                
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
