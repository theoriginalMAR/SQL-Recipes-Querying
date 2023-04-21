# SQL-Recipes-Querying
in this repository, I display how I have scraped data from, an open-source recipe website, 'purewow.com', added the extracted file into a MySQL table for better data visualisation, and performed SQL queries that answer questions posed by someone that may looking for specific dietary conditions and needs to find an accommodating recipe.

# Web Scraper
In the ws.py file, you can find a webscraper that I created that uses the Python library Beautiful Soup to collect recipe data. Not every recipe follows the same format, so the webscraper is programmed to account for these changes.

Each recipe comes with 10 properties, those being: recipe name, prep time, cook time, total time, serving portions, calories, fat in grams, carbs in grams, protein in grams and sugars in grams. I decided to choose this website as a source since it provides handy properties for each recipe, that can one can use to filter recipes to either dietary or portional preferences.

# MySQLWorkbench
After I extract the data & converted it into a CSV file, I decided to use MySQL Workbench in order to convert my file into an SQL table in order for me to run some SQL commands.
