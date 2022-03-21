# Based on https://github.com/Jerrybibo/webscraper/blob/master/main.py
# Code written by Jerrybibo, 1/26/2022. © 2022
import csv
from os import getcwd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
from settings import *

BASE_URL = "https://www.fragolosi.it/glossario/"

OUTPUT_FILE = 'culinary_terms.csv'

# Adding options for Selenium.
# Headless argument allows Selenium to use the Chrome driver without opening a discrete window.
opts = Options()
opts.add_argument(' --headless')

# Check for Chrome driver
chrome_driver_path = getcwd() + '/' + DRIVER_PATH

if not path.exists(chrome_driver_path):
    print('''Chrome driver was not found.
Please go to https://chromedriver.chromium.org/downloads and download the correct driver for your OS and Chrome.
Place the downloaded Chrome driver in the same folder as the Python file and set settings.py accordingly.
NOTE! The driver version must be equal to the current version of Google Chrome you are using!
To check your Chrome version, go to chrome://version/ and check the top entry; it should be of format xx.x.xxxx.xx.''')
    exit(-1)

driver = webdriver.Chrome(options=opts, executable_path=chrome_driver_path)


def get_definition(term):
    driver.get(term.get('href'))
    soup = bs4.BeautifulSoup(driver.page_source, features='html.parser')
    result = soup.find('div', {'class': 'col-md-9'}).find('p').get_text() + ' '
    result += ' '.join([i.get_text() for i in soup.find('div', {'class': 'col-md-9'}).find_all('li')])
    return result.strip()


def main():
    # Check if previously output file exists, and confirm that the user wants to overwrite
    if path.exists(OUTPUT_FILE):
        replace_output = input(f'Output file {OUTPUT_FILE} already exists. Overwrite? (y/n): ').lower()
        while not replace_output.startswith(('y', 'n')):
            replace_output = input('Please enter y or n (y/n): ').lower()
        if replace_output.startswith('n'):
            print("Exiting.")
            exit(0)
        elif replace_output.startswith('y'):
            print(f'Previous output file will be overwritten.')

    # Obtain rendered HTML data
    driver.get(BASE_URL)

    # Begin parsing using BS4
    soup_file = driver.page_source
    soup = bs4.BeautifulSoup(soup_file, features='html.parser')

    # Find the table with all the glossary terms
    glossary_list = soup.find('ul', {'class': 'listglossaryid'})
    terms = glossary_list.find_all('a')

    # Extract all the terms and their definitions and save to a 2d-list
    definitions = []
    for index, term in enumerate(terms):
        print(f'Processing {index + 1}/{len(terms)}: {term.get("title")}')
        definitions.append([index + 1, term.get('title'), get_definition(term)])

    # Now we have the terms, save them to a CSV file
    with open(OUTPUT_FILE, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(definitions)


main()
