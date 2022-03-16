# Utilizes https://adrien.barbaresi.eu/blog/simple-multilingual-lemmatizer-python.html for lemmatization.
import simplemma
import csv
import os

# Directory to analyze
directory = os.path.join('.', 'output', 'Antipasti')

files_to_analyze = dict()
terms = dict()

for file_index, file in enumerate(os.listdir(os.fsencode(directory))):
    filename = os.fsdecode(file)
    if filename.endswith('.ingredients'):
        files_to_analyze[file_index] = os.path.join(directory, filename)

for file_index, file in files_to_analyze.items():
    with open(file) as f:
        ingredients = f.readlines()
        full_ingredients_list = [[j.strip() for j in i.strip().split('  ') if j] for i in ingredients if i.strip()]
        # Do we care about ingredient amounts? If not, then first object of each list suffices
        # for ingredients_list in full_ingredients_list:
        #     amt_term = ingredients_list[-1]
        #     amt_anchor = [True if term.isnumeric() else False for term in amt_term.split()].index(True)
        #     ingredients_list = ingredients_list[:-1] + [' '.join(amt_term.split()[:amt_anchor]),
        #                                                 ' '.join(amt_term.split()[amt_anchor:])]
        print(full_ingredients_list)

print(files_to_analyze)
