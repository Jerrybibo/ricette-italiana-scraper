# Utilizes https://adrien.barbaresi.eu/blog/simple-multilingual-lemmatizer-python.html for lemmatization.
import simplemma
import csv
import os

# Directory to analyze
directory = '.\\output\\Antipasti'

files_to_analyze = dict()
terms = dict()

for file_index, file in enumerate(os.listdir(os.fsencode(directory))):
    filename = os.fsdecode(file)
    if filename.endswith('.ingredients'):
        files_to_analyze[file_index] = os.path.join(directory, filename)

for file_index

print(files_to_analyze)