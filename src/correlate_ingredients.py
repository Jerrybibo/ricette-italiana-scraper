# Given a list of indexed ingredients and a list of recipes (both csv files),
# return a list of relationships between the ingredients and recipes.
import csv
import os
from settings import *

# Directories to analyze
directories = [os.path.join('..', 'output', 'Antipasti'),
               os.path.join('..', 'output', 'Primi'),
               os.path.join('..', 'output', 'Secondi'),
               os.path.join('..', 'output', 'Dolci')]

files_to_analyze = []

# Add all ingredients files to the to-be-analyzed list
for directory in directories:
    for file_index, file in enumerate(os.listdir(os.fsencode(directory))):
        filename = os.fsdecode(file)
        if filename.endswith('.ingredients'):
            files_to_analyze.append(os.path.join(directory, filename))

# Load csv into dict but flip the keys and values
ingredients_dict = {}
with open(os.path.join('..', 'output', 'ingredients.csv'), 'r', encoding='utf-16') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'id':
            continue
        ingredients_dict[row[1]] = row[0]

# List of tuples that relate a recipe to its ingredients
recipe_ingredients = []

for file in files_to_analyze:
    with open(file, 'r', encoding='utf-16') as ingredients_file:
        ingredients = ingredients_file.readlines()
        full_ingredients_list = [[j.strip() for j in i.strip().split('  ') if j][0] for i in ingredients if i.strip()]
    for ingredient in ingredients_dict:
        if ingredient in full_ingredients_list:
            recipe_ingredients.append((ingredients_dict[ingredient], os.path.splitext(file)[0] + '.txt'))

with open(RECIPE_INGREDIENTS_OUTPUT, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(RECIPE_INGREDIENTS_TITLE_ROW)
    writer.writerows(recipe_ingredients)
