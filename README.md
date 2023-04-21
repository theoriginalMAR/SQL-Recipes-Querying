# SQL-Recipes-Querying
in this repository, I display how I have scraped data from, an open-source recipe website, 'purewow.com', added the extracted file into a MySQL table for better data visualisation, and performed SQL queries that answer questions posed by someone that may looking for specific dietary conditions and needs to find an accommodating recipe.

# Web Scraper
In the ws.py file, you can find a webscraper that I created that uses the Python library Beautiful Soup to collect recipe data. Not every recipe follows the same format, so the webscraper is programmed to account for these changes.

Each recipe comes with 10 properties, those being: recipe name, prep time, cook time, total time, serving portions, calories, fat in grams, carbs in grams, protein in grams and sugars in grams. I decided to choose this website as a source since it provides handy properties for each recipe, that can one can use to filter recipes to either dietary or portional preferences.

# MySQLWorkbench
After I extract the data & convert it into a CSV file, I decided to use MySQL Workbench in order to convert my file into an SQL table in order for me to run some SQL commands. In the table below, I have listed some sample questions that are meant to filter table results according to my own personal preferences. On the right column, you can find specific SQL commands ran in order to filter the table results accordingly. Hopefully this table can give the user an idea of how to utilise simple SQL commands to cater to ones own personal preferences.

Posed Question | SQL Command 
--- | --- 
If someone wants to make a last minute (quick) meal that can serve at least 6 people | SELECT * FROM recipe where total = (SELECT MIN(total) FROM recipe WHERE serve >= 6) AND serve>=6
If someone wants to make a meal that can cook while he’s out for a while (gym, errands etc) and has a higher than average protein (show the top 3 selections) | SELECT * FROM recipe where protein > (SELECT AVG(protein) FROM recipe) ORDER BY total DESC LIMIT 3
If someone wants to lose weight but is actively exercising & needs at least 30g of protein (show the top 2 selections) | SELECT * FROM recipe where protein > 30 ORDER BY calories ASC LIMIT 2
If someone is making a dinner party for 6-8 (himself included) & the guests do not consume sugar | SELECT * FROM recipe where serve BETWEEN 6 AND 8 ORDER BY sugars ASC LIMIT 1
If someone works all day & wants to come back & cook a quick meal with minimum prep that can meets or surpasses his required intake of calories (650) | SELECT * FROM recipe where prep = (SELECT MIN(prep) FROM recipe WHERE calories>650)
If someone wants to make a recipe that will feed just 4 people and fill them up as much as possible (highest calories per serving) | SELECT * FROM recipe WHERE serve = 4 ORDER BY calories DESC LIMIT 1
