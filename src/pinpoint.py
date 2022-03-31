from google.cloud import language_v1
from google.oauth2 import service_account
import csv
import os
from settings import *

# Set up Google Cloud natural language client
# Save application credentials to environment variable
credentials = service_account.Credentials.from_service_account_file(GCLOUD_CREDENTIALS)
client = language_v1.LanguageServiceClient(credentials=credentials)

# Directory to analyze
directory = os.path.join('..', 'output', 'Antipasti')

# Remove location entities of low relative importance in text
SALIENCE_THRESHOLD = 0.001

# Locations filename (contains actual location data)
output_filename = os.path.join('..', 'output', 'locations.csv')

# Catalog filename (contains the input txt file names; used for lookup)
catalog_filename = os.path.join('..', 'output', 'file_indices.csv')

files_to_analyze = dict()

for file_index, file in enumerate(os.listdir(os.fsencode(directory))):
    filename = os.fsdecode(file)
    if filename.endswith('.txt'):
        files_to_analyze[file_index] = os.path.join(directory, filename)

file_count = len(files_to_analyze)
entity_id = 0

with open(catalog_filename, 'w', newline='') as output_csv:
    csv_writer = csv.writer(output_csv)
    csv_writer.writerow(['id', 'file'])
    for file_index, file in files_to_analyze.items():
        csv_writer.writerow([file_index, file])


with open(output_filename, 'w', newline='') as output_csv:
    csv_writer = csv.writer(output_csv)
    csv_writer.writerow(['id', 'location', 'file_index'])
    for file_index, file in files_to_analyze.items():
        print(f"\rProcessing file {file_index+1}/{file_count+1}", end='')
        with open(file, 'r', encoding='cp1252') as f:
            document = language_v1.Document(content=''.join(f.readlines()), type_=language_v1.Document.Type.PLAIN_TEXT)
            entities = client.analyze_entities(document=document).entities
            for entity in entities:
                # Remove entities that are of low salience (prominence) and are not locations
                if entity.type == language_v1.Entity.Type.LOCATION and entity.salience >= SALIENCE_THRESHOLD:
                    csv_writer.writerow([entity_id, entity.name, file_index])
                    entity_id += 1
    print(f"\rProcessing has finished. ({file_count+1} files)")
