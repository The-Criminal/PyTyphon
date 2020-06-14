import os
import sys
import time
import random
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from colorama import Fore, Back, Style
from colorama import init
from constants import *
init()

# How to fix common problems.
# Not found error 
# Use vpn ip banned for 24 hours

os.system('clear')


class ender:
    def draco(self):
        print(Fore.RED+'  You have choosen Reverse phone number search option|Type "help" for more info')
        while True:
            print(Fore.GREEN, Style.BRIGHT + ' |')
            print('  |')
            cin = input(Fore.GREEN + Style.BRIGHT +
                        '  [--]' + Fore.BLUE + Style.BRIGHT + '#' + Fore.GREEN + '[--] ')
            if cin == 'help' or cin == 'h':
                print(Fore.GREEN + Style.BRIGHT + '\n  Type', Style.BRIGHT + Fore.RED + 'Z', Style.BRIGHT +
                      Fore.GREEN+'fetches addres, age, name')
                time.sleep(0.1)
                print(Fore.GREEN + Style.BRIGHT + '  Type', Style.BRIGHT + Fore.RED + 'V', Style.BRIGHT +
                      Fore.GREEN + Style.BRIGHT +'fetches ar. code, serivce provider, coverage ar. etc etc \n')

            elif cin == 'Z':
                options = Options()

                # This will make your browser window hidden 
                # setting it false will show you the browser window
                options.headless = True
                driver = webdriver.Firefox(options=options)
                print(Style.RESET_ALL)
                phone = input(Fore.GREEN + Style.BRIGHT + 'Enter phone number|US ONLY: ')
                print (Style.RESET_ALL)
                driver.get(zab + phone)

                html = driver.page_source
                soup = bs(html, 'lxml')
                elems = driver.find_element_by_class_name('result-person-info')
                time.sleep(random.randint(1, 3))
                print(Fore.YELLOW, Style.BRIGHT + sep + Style.RESET_ALL)
                print(Fore.GREEN + elems.text + Style.RESET_ALL)
                print(Fore.YELLOW, Style.BRIGHT + sep + Style.RESET_ALL)
                driver.quit()
                # its messy here i know still working


            elif cin == 'V':
                options = Options()
                options.headless = True
                driver = webdriver.Firefox(options=options)
                print(Style.RESET_ALL)
                #phone = input(Fore.GREEN + Style.BRIGHT + 'Enter phone number|US ONLY: ')
                time.sleep(5)
                print(Style.RESET_ALL)
                #driver.get(rev + phone + fw)
                driver.get(rev)
                html = driver.page_source
                soup = bs(html, 'lxml')
                wither = driver.find_element_by_xpath('//td/div/div/span')
                print(Fore.YELLOW, Style.BRIGHT + sep + Style.RESET_ALL)
                print(Fore.GREEN + 'Name: ' + wither.text)
                skel = driver.find_element_by_xpath('//div/div[2]')
                print ('Area: ' + skel.text+'\n' + Style.RESET_ALL)
                tl = driver.find_element_by_xpath('//fieldset[2]/div')
                print (tl.text + Style.RESET_ALL)
                print(Fore.YELLOW, Style.BRIGHT + sep + Style.RESET_ALL)
                driver.quit()

            elif cin == 'X':
                from pytyphon import steve

            elif cin in ('exit','ex'):
                sys.exit()

            else:
                print('check output')


obj = ender()
obj.draco()
