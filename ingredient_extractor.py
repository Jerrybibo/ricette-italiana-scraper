import csv
import os

TITLE_ROW = ['id', 'name']

# Directories to analyze
directories = [os.path.join('.', 'output_backups', 'Antipasti'),
               os.path.join('.', 'output_backups', 'Primi'),
               os.path.join('.', 'output_backups', 'Secondi'),
               os.path.join('.', 'output_backups', 'Dolci')]

files_to_analyze = dict()
terms = dict()

# Add all ingredients files to the to-be-analyzed list
for directory in directories:
    for file_index, file in enumerate(os.listdir(os.fsencode(directory))):
        filename = os.fsdecode(file)
        if filename.endswith('.ingredients'):
            files_to_analyze[file_index] = os.path.join(directory, filename)

ingredient_set = set()

# Read all ingredients files and add all ingredients to the set
for file_index, file in files_to_analyze.items():
    with open(file, encoding='utf-16') as f:
        ingredients = f.readlines()
        full_ingredients_list = [[j.strip() for j in i.strip().split('  ') if j] for i in ingredients if i.strip()]
        for ingredient in full_ingredients_list:
            ingredient_set.add(ingredient[0])
        with open(os.path.splitext(file)[0] + '.csv', 'w', newline='') as output_csv:
            csv_writer = csv.writer(output_csv)
            csv_writer.writerows(full_ingredients_list)

# Write the set of ingredients to a file
ingredient_list = [[i + 1, ingredient_name] for i, ingredient_name in enumerate(sorted(list(ingredient_set)))]
with open('ingredients.csv', 'w', newline='') as ingredients_file:
    csv_writer = csv.writer(ingredients_file)
    csv_writer.writerow(TITLE_ROW)
    csv_writer.writerows(ingredient_list)
