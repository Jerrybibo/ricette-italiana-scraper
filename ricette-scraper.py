# Based on https://github.com/Jerrybibo/webscraper/blob/master/main.py
# Code written by Jerrybibo, 1/29/2022. © 2022

from os import getcwd, path, listdir, makedirs
from shutil import rmtree
from concurrent.futures import ProcessPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
from time import time

BASE_URL = "https://www.giallozafferano.it/"
DRIVER_PATH = "chromedriver.exe"
OUTPUT_ROOT = path.join(".", "output")

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


def soupify(url):
    # Helper method to get soup object from URL
    driver.get(url)
    soup_file = driver.page_source
    return bs4.BeautifulSoup(soup_file, features='html.parser')


def get_categories(soup):
    # We first need to get all the categories of cuisine. (e.g., Pane, Pasta, Carne, etc.)
    # Find the relevant table and return all the linked URLs
    category_list = soup.find('section', {'class': 'gz-caciopepe'})
    categories = [[i.get('title'), i.get('href')] for i in category_list.find_all('a')]
    return categories


def get_recipes(category):
    # Then we need to grab all the recipes available under one category.
    category_name, category_url = category
    soup = soupify(category_url)

    # Figure out total page count for category
    total_pages = soup.find('span', {'class': 'total-pages'})
    # Some pages do not have total-pages element; for these, get last element in page list
    if not total_pages:
        total_pages = soup.find('div', {'class': 'gz-pages'}).find_all('a')[-1]
    total_pages = int(total_pages.get_text())
    print(f"Obtaining recipes for category {category_name} ({total_pages} pages) at {category_url}...")
    makedirs(path.join(OUTPUT_ROOT, category_name))

    recipe_urls = []

    # Get the URL for all the pages for the category
    for i in range(total_pages + 1):
        page_url = category_url.split('/')
        page_url.insert(4, f'page{i}')
        page_url = '/'.join(page_url)
        soup = soupify(page_url)
        recipe_urls += [i.find('a').get('href') for i in soup.find_all('article', {'class': 'gz-card'})]
        print('*', end='')
    print(f' Completed. ({len(recipe_urls)} recipes)')

    # For each URL, grab all body paragraphs and their associated titles, then output to file
    for recipe_url in recipe_urls:
        soup = soupify(recipe_url)
        recipe_title = soup.find('h1', {'class': 'gz-title-recipe'}).get_text()
        print(f"Processing {category_name} - {recipe_title}... ", end='')
        # Magic; don't question it
        recipe_text = [list(section)
                       for section in list(zip([i.get_text().strip() + '\n\n'
                                                for i in soup.find_all('h2', {'class': 'gz-title-section'})],
                                               ['\n'.join([j.get_text() for j in i.find_all('p')]) + '\n\n'
                                                for i in soup.find_all('div', {'class': 'gz-content-recipe'})]))]
        recipe_output = sum(recipe_text, [recipe_title + '\n\n'])
        with open(path.join(OUTPUT_ROOT, category_name, recipe_title) + '.txt', 'w') as recipe_file:
            recipe_file.writelines(recipe_output)
        print("Done.")


def main():
    skip_output_check = True
    # Create output folder
    if path.exists(OUTPUT_ROOT):
        if skip_output_check:
            replace_output = 'y'
            print(f'Output directory {OUTPUT_ROOT} already exists, but skip_output_check is True. Skipping user input')
        else:
            replace_output = input(f'Output directory {OUTPUT_ROOT} already exists. Replace? (y/n): ').lower()
        while not replace_output.startswith(('y', 'n')):
            replace_output = input('Please enter y or n (y/n): ').lower()
        if replace_output.startswith('n'):
            print("Exiting.")
            exit(0)
        elif replace_output.startswith('y'):
            print(f'Previous output folder located at {OUTPUT_ROOT} will be overwritten.')
            rmtree(OUTPUT_ROOT)
            makedirs(OUTPUT_ROOT)
    else:
        print(f'Created output directory {OUTPUT_ROOT}.')
        makedirs(OUTPUT_ROOT)

    # Obtain rendered HTML and parse using BS4
    soup = soupify(BASE_URL)

    # Obtain all available categories
    categories = get_categories(soup)

    for category in categories:
        get_recipes(category)
        return


main()
