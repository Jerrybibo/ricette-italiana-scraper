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

