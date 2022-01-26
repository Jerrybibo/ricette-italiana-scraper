# Based on https://github.com/Jerrybibo/webscraper/blob/master/main.py
# Code written by Jerrybibo, 1/26/2022. © 2022

from os import getcwd, path, listdir
from concurrent.futures import ProcessPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
from time import time

BASE_URL = "https://www.fragolosi.it/glossario/"
DRIVER_PATH = "chromedriver.exe"

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
    print('Processing', term.get('title'))
    driver.get(term.get('href'))
    soup = bs4.BeautifulSoup(driver.page_source, features='html.parser')
    return soup.find('div', {'class': 'col-md-9'}).find('p').get_text()


def main():
    # Obtain rendered HTML data
    driver.get(BASE_URL)

    # Begin parsing using BS4
    soup_file = driver.page_source
    soup = bs4.BeautifulSoup(soup_file, features='html.parser')

    # Find the table with all the glossary terms
    glossary_list = soup.find('ul', {'class': 'listglossaryid'})
    terms = glossary_list.find_all('a')

    term_names = [i.get('title') for i in terms]

    # Runtime testing (list comp vs map)
    start_time = time()

    # # of terms that starts with 'A': 218
    # map() took ~121.17 seconds to process all terms starting with 'A' on Jerry's machine + Internet from Emory (run 1)
    # List comprehension took ~49.98 seconds for same task... suspicious of caching (run 2)

    # # of terms that starts with 'B': 143
    # List comprehension took ~113.81 seconds (run 1)
    # map() took ~33.41 seconds. As suspected, caching speeds up the process by a large amount. (run 2)

    # Both aren't good enough! Will be looking into multithreading + other means...
    # Expected run time as of now on a normal computer: Approximately 1 hour for all terms
    definitions = zip(term_names, list(map(get_definition, terms)))

    print("Took", time() - start_time, "seconds")
    print(definitions)


main()
