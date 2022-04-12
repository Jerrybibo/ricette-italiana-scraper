## Welcome to `ricette-italiana-scraper`

This project is currently in pre-production. 

To get started, double-click on the `ricette-italiana-scraper.exe` file, stored in the [`src/dist`](../src/dist) folder.

Table of Contents
----
- [Index Page (this page)](./index.md)
- [Getting Started and Troubleshooting](./quickstart.md)
- [Scrapers](./scrapers)
  - [Overview](./scrapers/scrapers.md)


## Internal Script Description

Note: Will be refactored into each individual script's description file.

* The `glossario_scraper.py` script sources [FraGolosi](https://www.fragolosi.it/), an independent recipe aggregation
  site to obtain culinary terms (e.g., “padellare” – “to fry”) and save them, including their definitions,
  to a text or comma-separated values file.
* `ingredient_extractor.py` takes as input recipes outputted by the `ricette_scraper.py` and return a large document
  containing a set of ingredients (without duplicates), and a separate CSV containing where a specific ingredient has
  appeared in the recipes database and its amount.
* `ricette_scraper.py` above contains a simple script that scrapes [Giallo Zafferano](https://www.giallozafferano.it/),
  another third-party commercial recipe aggregator, and saves all recipes found in every searchable category into 
  text files in subdirectory organization.
* `pinpoint.py` and `mapify.py` extract all location data from the recipes, preferably those outputted by the
  `ricette_scraper.py`, and reverse-geocodes them into physical coordinates (done through `pinpoint.py`);
  then, `mapify.py` uses the outputted coordinates and displays the results on a JPG-representation of a map.