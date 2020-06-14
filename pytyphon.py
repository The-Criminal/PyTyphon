#!/usr/bin/env python3
# This will not run on online IDE
# credits: Me,StackOverflow & GOOGLE OFC

from colorama import init
import requests
import os
import sys
import time
from bs4 import BeautifulSoup as bs
from colorama import Fore, Back, Style
sys.path.append('core')
from constants import *

# internet and update check
class main:
    def __init__(self):
        try:
            r = requests.get(google)
        except:
            print(Fore.RED, Style.BRIGHT +
                  'Err it looks like your internet is not working' + Style.RESET_ALL)
            time.sleep(2)
            sys.exit()

    def update(self):
        page = requests.get(dunge)
        soup = bs(page.text, 'html.parser')

        ver = soup.find(class_='de1')

        b = [ver.text]
        if b == a: 
            print()
        else:
            print(Fore.RED,  Style.BRIGHT +
                  'Theres a new update waiting for you please update the script')
            time.sleep(0.2)
            print(Fore.GREEN, Style.BRIGHT + up)
            time.sleep(1)
            print(Style.RESET_ALL)
            sys.exit()


# aggrement
os.system('clear')
if 'no' in open('agree.txt').read():
    print(Fore.RED + Style.BRIGHT +
          'NOTE: WITH GREAT POWERS COMES GREAT RESPONSIBILITY')
    time.sleep(3)
    print(Fore.RED + Style.BRIGHT+'Do not use this tool for Stalking, Threatning, Cyber Bullying extra. whatever you do with this you are doing it on your own RESPONSIBILITY.')
    print(Style.RESET_ALL)
    time.sleep(4)
    agree = input(
        Fore.BLUE + 'Do you agree to these terms and conditions?|yes or no: ')
    print(Style.RESET_ALL)

    if agree in ('yes', 'Y', 'yes'):
        print(Back.RED + 'Thanks!')
        print(Style.RESET_ALL)
        time.sleep(3)
        FILE = open("agree.txt", "w")
        FILE.write('yes')
        FILE.close()
        os.system('clear')
    else:
        print(Fore.RED+"[!] You have to agree!")
        time.sleep(3)
        sys.exit()
        print(Style.RESET_ALL)


# Main stuff
class testo():
    def banner(self):
        import banner

    def steve(self):
        while True:
            try:
                try:
                    print(Fore.GREEN, Style.BRIGHT +
                          ' Enter Your Input|or type "help"')
                    print('  |')
                    print('  |')
                    # print('  |')
                    obs = input(Fore.GREEN + Style.BRIGHT +
                                '  [--]' + Fore.BLUE + Style.BRIGHT + '!' + Fore.GREEN + '[--] ')
                    print(Style.RESET_ALL)

                    if obs == 'help':
                        print(Fore.GREEN, Style.BRIGHT + " Type", Style.BRIGHT + Fore.RED +
                              'P', Style.BRIGHT + Fore.GREEN+'for people search ')
                        time.sleep(0.3)
                        print(Fore.GREEN, Style.BRIGHT + " Type", Style.BRIGHT + Fore.RED +
                              'N', Style.BRIGHT + Fore.GREEN+'for reverse number search ')
                        time.sleep(0.3)

                        print(Fore.RED + Style.BRIGHT + '  Type exit to close')
                        time.sleep(3)
                        print(Style.RESET_ALL)

                    elif obs == 'P':
                        import people
                        obj = people.llama()  # calling people saercher file

                    elif obs == 'N':
                        import number
                        obj = number.ender()  # calling number saercher file

                    elif obs == 'exit':
                        os.system('clear')
                        print(Fore.RED, Style.BRIGHT +
                              'GoodBye' + Style.RESET_ALL)
                        # print (Style.RESET_ALL)
                        time.sleep(1)
                        os.system('clear')
                        sys.exit()

                    elif obs == 'clear' or main == 'c' or main == 'C':
                        os.system('clear')

                    else:
                        print(Fore.RED, Style.BRIGHT +
                              ' check your input\n' + Style.RESET_ALL)

                except KeyboardInterrupt:
                    print(
                        Fore.RED + "\n  Ctrl+C Pressed! Use 'exit' to close the tool!" + Style.RESET_ALL)

            except EOFError:
                print(
                    Fore.RED + "\n  Ctrl+D Pressed! closing the tool" + Style.RESET_ALL)
                time.sleep(1)
                sys.exit()


obj = main()
obj.update()
obj = testo()
obj.banner()
obj.steve()
