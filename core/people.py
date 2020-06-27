import requests
from bs4 import BeautifulSoup as bs
import os
import sys
import time
import random
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from colorama import Fore, Back, Style
from colorama import init
from constants import *
sys.path.append('PyTyphon')
init()



# Don't Edit this update checking
class main:
    page = requests.get(dunge)
    soup = bs(page.text, 'html.parser')
    ver = soup.find(class_='de1')
    b = [ver.text]

    if b == a:
        print()
    else:
        print(Fore.RED,  Style.BRIGHT + 'Theres a new update waiting for you please update the script')
        time.sleep(0.2)
        print(Fore.GREEN, Style.BRIGHT + up)
        time.sleep(1)
        print(Style.RESET_ALL)
        sys.exit()

# UserAgent
ua = UserAgent()
hdr = {'User-Agent': ua.random,
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


#### WARNING ####
# This is where the main stuff happens
# Editing anything here without knowldege can break the script

class llama:
    # Useless function
    def clear_text(text):
        if '\n' in text:
            text = text.replace('\n', '')
        if '\xa0' in text:
            text = text.replace('\xa0', '')
            return text
    os.system('clear')
    print(Fore.RED+'  You have choosen Reverse people search option|Type "help" for more info')
    time.sleep(1)

    while True:
        print(Fore.GREEN, Style.BRIGHT + ' |')
        print('  |')
        samantha = input(Fore.GREEN + Style.BRIGHT +
                         '  [--]' + Fore.BLUE + Style.BRIGHT + '@' + Fore.GREEN + '[--] ')
        if samantha in ('help','h'):
            print('')
            print(Fore.GREEN, Style.BRIGHT + '  Type', Style.BRIGHT +
                  Fore.RED + 'B', Style.BRIGHT + Fore.GREEN+'fetches addres number age name email | can narrow down to state and city')
            time.sleep(0.1)

            print(Fore.GREEN + Style.BRIGHT + '  Type', Style.BRIGHT +
                  Fore.RED + 'T', Style.BRIGHT, Fore.GREEN + 'fetches name age number email | can narrow down to state only')
            time.sleep(0.1)

            print(Fore.GREEN, Style.BRIGHT + '  Type', Style.BRIGHT +
                  Fore.RED + 'L', Style.BRIGHT + Fore.GREEN+'fetches name age number email IP | can narrow down to state and city')
            time.sleep(0.1)

            print(Fore.GREEN + Style.BRIGHT + '  Type', Style.BRIGHT + Fore.RED + 'X', Style.BRIGHT + Fore.GREEN+'to return to main menu')
            time.sleep(0.1)

            print(Fore.GREEN, Style.BRIGHT + '  Type', Style.BRIGHT + Fore.RED + 'C', Style.BRIGHT, Fore.GREEN+'will clear your screen')
            time.sleep(0.1)

            print(Fore.RED + Style.BRIGHT + '  Type exit to close')
            print(Style.RESET_ALL)


        elif samantha == 'B':
            os.system('clear')
            print(Fore.RED + Style.BRIGHT + '  BE SURE TO USE HYPHEN(-) WHEN ENETERING NAME')
            msgstr1 = f'  AFTER ENTERING INPUT IF IT SHOWS BLANK OR NONE THEN USER NOT FOUND'
            # time.sleep(3)
            print(msgstr1)
            print(Style.RESET_ALL)

            name = input(Fore.GREEN+'  Type the first & last name | example: james-charles: ')
            state = input('  Type State | example: ca,pa,tx: ')
            city = input('  Type City | example: los-angeles: ')
            print(Style.RESET_ALL)
            # time.sleep(9)
            # r = requests.get(URL, headers=hdr)
            # soup = bs(r.content, features='html.parser')
            # body = soup.body
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            driver.get(been + name + fw + state + fw + city + fw)
            for resu in driver.find_elements_by_class_name('search-result'):
                button_text = resu.find_element_by_class_name('search-result__button').text
                text = resu.text.replace(button_text, '')
                print(Fore.GREEN, Style.BRIGHT + text + Style.RESET_ALL)
                time.sleep(random.randint(1, 3))
                print(Fore.YELLOW, Style.BRIGHT + sep + Style.RESET_ALL)



        elif samantha == 'T':
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            print(Fore.RED + Style.BRIGHT + ' BE SURE TO USE HYPHEN(-) WHEN ENETERING NAME')
            msgstr1 = f' AFTER ENTERING INPUT IF IT SHOWS BLANK OR NONE THEN USER NOT FOUND'
            time.sleep(3)
            print(Style.RESET_ALL)

            name = input(Fore.GREEN+' Type the first & last name | example: james-charles: ')
            state = input(' Type State | example: ca,pa,tx: ')
            print(Style.RESET_ALL)
            driver.get(truth + name + '/?state=' + state + fw)
            html = driver.page_source
            soup = bs(html, 'lxml')

            # Scraping here
            print(Fore.YELLOW + Style.BRIGHT + sep)
            for h2 in driver.find_elements_by_tag_name('h2'):
                time.sleep(random.randint(1, 3))
                print(Fore.BLUE + h2.text)
                for p in h2.find_elements_by_xpath('.//parent::div/p'):
                    print(Fore.YELLOW + p.text)
                    print(Style.RESET_ALL)
                print(Fore.YELLOW + Style.BRIGHT + sep)
                print(Style.RESET_ALL)
            driver.quit()


        elif samantha == 'L':
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            print(Fore.RED + Style.BRIGHT + 'BE SURE TO USE HYPHEN(-) WHEN ENETERING NAME')
            msgstr1 = f'AFTER ENTERING INPUT IF IT SHOWS BLANK OR NONE THEN USER NOT FOUND'
            print('Currently this option is only printing Name and address and is lil buggy')
            print('USE VPN AS AFTER TEN SEARCHES YOUR IP WILL BE BLACKLISTED FOR 24 HOURS')
            print(Style.RESET_ALL)

            name = input(Fore.GREEN+'Type the first & last name | example: james-charles: ')
            state = input('Type State | example: ca,pa,tx: ')
            print(Style.RESET_ALL)
            driver.get(them + name + fw + state + fw)
            html = driver.page_source
            soup = bs(html, 'lxml')
            time.sleep(6)
            for element in driver.find_elements_by_class_name('ThatsThem-record-overview'):
                print(Style.RESET_ALL)
                print(Fore.RED + element.text + Style.RESET_ALL)
                print(Style.RESET_ALL)
                time.sleep(1)
                # dl=driver.find_element_by_xpath('//dl')
                # print(dl.text)
            # blo = driver.find_element_by_tag_name('h3').text
            # if blo:
            #     print(Fore.GREEN + '  ip', Fore.RED + 'BLOCKED', Fore.GREEN + 'Time to change your location' + Style.RESET_ALL)
            #         driver.quit()
            # else:
            #     pass


        # donations
        elif samantha == 'd':
            print(Fore.RED + Style.BRIGHT+'Thank you for being generous')
            print('my btc addres is : ')
            print(Style.RESET_ALL)

        # clear screen
        elif samantha in ('clear','c','cl','C'):
            os.system('clear')

        # return to main menu
        elif samantha == 'X':
            from pytyphon import stevell

        # exit the script
        elif samantha == 'exit':
            sys.exit()

        # you know
        else:
            print(Fore.RED + '\n  Check your input')
            print(Style.RESET_ALL)


obj = llama()
