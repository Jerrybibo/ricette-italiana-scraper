# Settings file.
from os import path

# URL to scrape from. Probably don't want to change this.
BASE_URL = "https://www.giallozafferano.it/"

# The driver path.
# Changes needed if OS is not Windows.
DRIVER_PATH = "chromedriver"

# Output directory.
OUTPUT_ROOT = path.join(".", "output")

# Whether to write ingredients into a separate file or not.
WRITE_INGREDIENTS = True
