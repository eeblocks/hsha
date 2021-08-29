#!/usr/bin/python3
# hsha v1.3

# Dependencies
from hashlib import sha256
from sys import exit
from time import time

import os
import getpass
import argparse

if os.name == 'nt':
    import win32clipboard

# Colors
class Colors:
    WHITE = "\033[37m"
    RED = "\033[31m"
    GREEN = "\033[32m"

# Set title on the terminal
os.system('title hsha' if os.name == 'nt' else 'echo -en "\033]0;hsha\a"')

# Clear terminal
def refresh():
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = open('banner.txt', 'r', encoding='utf-8').read()
    print(f'{Colors.GREEN}{banner}{Colors.WHITE}\n')


refresh()


# Argument Settings
parser = argparse.ArgumentParser(description='Hash your Files/Text to SHA-256', add_help=True)
parser.add_argument('-t', '--text', action='store', required=False, dest='text', help='Text to SHA-256')
parser.add_argument('-f', '--file', action='store', required=False, dest='file', help='File to SHA-256')
args = parser.parse_args()


# Hash Function
def hashing(s):

    refresh()

    start_time = time()
    encoded = sha256(s.encode()).hexdigest()
    end_time = time()

    elapsed = end_time - start_time

    print(encoded)
    print(f'\nTime elapsed: {Colors.GREEN}{round(elapsed, 2)}s{Colors.WHITE}')
    
    if os.name == 'nt':
        
        # Access to the Windows clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()

        # Set hash to Windows clipboard
        win32clipboard.SetClipboardText(encoded)

        # Close the windows clipboard
        win32clipboard.CloseClipboard()

        print('\n(Hash copied to clipboard)')
    

# Args Text Function
def text(t):
    hashing(t)

# Args File Function
def file(f):

    try:
        file_open = open(f, 'r', encoding='cp850').read()
        hashing(file_open)
    except:
        print(f'{Colors.RED}Needs to specify the exact path...{Colors.WHITE}')
        exit()

# Main
if __name__ == '__main__':

    # Check args
    if args.text:
        text(args.text)
        exit()

    elif args.file:
        file(args.file)
        exit()

    # Normal mode
    print('-------------')
    print('$ Hash Mode $')
    print('-------------\n')

    print('[1] File')
    print('[2] Text\n\n> ', end='')

    choice = input().lower()

    # File Option
    if choice == '1' or choice == 'file' or choice == 'f':
        refresh()

        # Get current dir
        os.chdir(os.path.dirname(__file__))
        d = os.getcwd()

        print(f'Current directory:\n{d}')

        print('\n(help*)')

        while True:
            
            iroute = input(f'\n[+] File route: ').lower()

            # Help command
            if iroute == 'help*' or iroute == 'h*':
                refresh()
                print(' \ndownloads* / d* > Goes to the download directory')

            # Go to the downloads directory
            elif iroute == 'downloads*' or iroute == 'd*':
                refresh()

                print(f'Current directory:\nC:/Users/{getpass.getuser()}/Downloads/\n')
                
                down = input('[+] Download name: ')
                route = f'C:/Users/{getpass.getuser()}/Downloads/{down}'
                break

            else:
                route = iroute
                break


        # Open & Read the file
        try:
            content = open(route, 'r', encoding='cp850').read()
        except:
            print(f"\n{Colors.RED}Can't open the file...{Colors.WHITE}")
            exit()

    # Text Option
    elif choice == '2' or choice == 'text' or choice == 't':
        refresh()
        content = input('[+] Text: ')

    # Exit Option
    else:
        exit()
    
    hashing(content)
    
