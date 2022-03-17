Roadmap for Spring 2022
----
**Project commit history are stored [here](https://github.com/Jerrybibo/ricette-italiana-scraper/commits/master).**

Completed so far:
* Core tools to extract from recipes:
  * Glossary terms
  * Ingredients
  * Location data
* Globally available configuration file
* Visualization

| Week      | Target                                                                                                                                                                                          |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3/13-3/19 | Complete README.md for available scripts<br/>Complete `ingredient-extractor.py`<br/>Enable output for `glossario-scraper.py`                                                                    |
| 3/20-3/26 | Initialize SQLite DB<br/>Compose schema for available data (correlate recipe, location, ingredient)<br/>Run scraping routine on full dataset<br/>Begin work on basic initialization SQL scripts |
| 3/27-4/2  | Continued work on SQLite DB<br/>Re-document all files and create interactive guide/tool for usage<br/>Refactor `settings.py`                                                                    |
| 4/3-4/9   | Continued work on SQLite DB<br/>Compose test queries for data retrieval<br/>Optionally: Redo `pinpoint` and `mapify` routines to use HTML                                                       |
| 4/10-4/16 | Robust testing and completion of SQLite DB<br/>Detailed documentation of the DB and usage (publication-quality)                                                                                 |
| 4/17-4/23 | TBD (review)                                                                                                                                                                                    |
| 4/24-end  | TBD (review)                                                                                                                                                                                    |
