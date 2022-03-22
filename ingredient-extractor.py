import csv
import os

# Directory to analyze
directory = os.path.join('.', 'output', 'Antipasti')

files_to_analyze = dict()
terms = dict()

# Add all ingredients files to the to-be-analyzed list
for file_index, file in enumerate(os.listdir(os.fsencode(directory))):
    filename = os.fsdecode(file)
    if filename.endswith('.ingredients'):
        files_to_analyze[file_index] = os.path.join(directory, filename)

ingredient_set = set()

for file_index, file in files_to_analyze.items():
    with open(file) as f:
        ingredients = f.readlines()
        full_ingredients_list = [[j.strip() for j in i.strip().split('  ') if j] for i in ingredients if i.strip()]
        for ingredient in full_ingredients_list:
            ingredient_set.add(ingredient[0])
        with open(os.path.splitext(file)[0] + '.csv', 'w', newline='') as output_csv:
            csv_writer = csv.writer(output_csv)
            csv_writer.writerows(full_ingredients_list)
        # Do we care about ingredient amounts? If not, then first object of each list suffices
        # for ingredients_list in full_ingredients_list:
        #     amt_term = ingredients_list[-1]
        #     amt_anchor = [True if term.isnumeric() else False for term in amt_term.split()].index(True)
        #     ingredients_list = ingredients_list[:-1] + [' '.join(amt_term.split()[:amt_anchor]),
        #                                                 ' '.join(amt_term.split()[amt_anchor:])]

ingredient_list = [[i + 1, ingredient_name] for i, ingredient_name in enumerate(sorted(list(ingredient_set)))]
with open('ingredients.csv', 'w', newline='') as ingredients_file:
    csv_writer = csv.writer(ingredients_file)
    csv_writer.writerows(ingredient_list)
