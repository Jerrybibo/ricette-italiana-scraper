# Settings file.
from os import path, environ

# URLs to scrape from. Probably don't want to change this.
RECIPE_BASE_URL = "https://www.giallozafferano.it/"
GLOSSARY_BASE_URL = "https://www.fragolosi.it/glossario/"
RECIPE_CATEGORIES = [('Antipasti', 'https://www.giallozafferano.it/ricette-cat/Antipasti/'),
                     ('Primi', 'https://www.giallozafferano.it/ricette-cat/Primi/'),
                     ('Secondi', 'https://www.giallozafferano.it/ricette-cat/Secondi/'),
                     ('Dolci', 'https://www.giallozafferano.it/ricette-cat/Dolci/')]

# Whether to overwrite existing output files by default or not.
SKIP_OUTPUT_CHECK = False

# Google Cloud credentials path.
GCLOUD_CREDENTIALS = environ['GOOGLE_APPLICATION_CREDENTIALS']
# Google Maps credentials path.
GMAPS_CREDENTIALS = environ['GOOGLE_MAPS_API_KEY']


# The driver path.
# Changes needed if the Chrome version does not match driver, or differing OS.
DRIVER_PATH = path.join("..", "driver", "chromedriver.exe")

# Output directory.
OUTPUT_ROOT = path.join("..", "output")

# Output file names.
GLOSSARY_OUTPUT = path.join(OUTPUT_ROOT, "culinary_terms.csv")
INGREDIENTS_OUTPUT = path.join(OUTPUT_ROOT, "ingredients.csv")

# Directory to the SQLite database.
DB_FILE = path.join('..', 'sqlite', 'ricette_italiana.db')

# Title rows for CSV files.
GLOSSARY_TITLE_ROW = ['id', 'name', 'description']
INGREDIENTS_TITLE_ROW = ['id', 'name']

# Specify output map name for mapify routine
MAP_FILENAME = 'mapify_img.png'
# Specify output map dimensions
MAP_DIMENSIONS = (1920, 1080)

# Whether to write ingredients into a separate file or not.
WRITE_INGREDIENTS = True
