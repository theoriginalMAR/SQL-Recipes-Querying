from bs4 import BeautifulSoup
import requests

response_html = requests.get('https://www.purewow.com/food/easy-dinner-recipes-for-beginners').text
soup = BeautifulSoup(response_html, 'lxml')
recipes = soup.find_all('div', class_='image-text-wrapper standard')

f = open("cookingfile.txt", "w")

for recipe in recipes:
    title = recipe.find('a', class_='large-image-link').find('h2').find('a').text
    link = recipe.find('a', class_='large-image-link').get('href')
    recipe_html = BeautifulSoup(requests.get(link).text, 'lxml')
    # If the link is not broken, then proceed 
    if not recipe_html.find('div', class_="not-found"):
        time_array = []
        prep_time = recipe_html.find('div',class_="recipe-time-byline-bottom").find('div', class_="prep").find('span').text
        cook_time = recipe_html.find('div',class_="recipe-time-byline-bottom").find('div', class_="cook").find('span').text
        total_time = recipe_html.find('div',class_="recipe-time-byline-bottom").find('div', class_="total").find('span').text
        time_array.extend([prep_time, cook_time, total_time])
        serving = recipe_html.find('div',class_="recipe-time-byline-bottom").find('div', class_="serves").find('span').text
        nutrients = recipe_html.find_all('li', class_='nutrient')
        time_minute_array = []

        # Convert string timings, to int timing in minutes
        for timing in time_array:
            time = timing.split()
            if len(time) == 1:
                time_in_mins = time[0]
            elif time[1] != 'min':
                hour = int(time[0])
                if len(time) > 2:
                    time_in_mins = (hour*60) + int(time[2])
                else:
                    time_in_mins = (hour*60)
            else: 
                time_in_mins = time[0]
            time_minute_array.append(str(time_in_mins))
        
        prep_time = time_minute_array[0]
        cook_time = time_minute_array[1]
        total_time = time_minute_array[2]
        
        # If theres is only 1 nutrients' list, then proceed
        if len(nutrients) < 8:

            f.write(title)
            f.write('|')
            f.write(prep_time)
            f.write('|')
            f.write(cook_time)
            f.write('|')
            f.write(total_time)
            f.write('|')
            f.write(serving)
            f.write('|')

            for nutrient in nutrients:
                # If the nutrient tag is not empty, then proceed
                if nutrient.find('p'):
                    nut = nutrient.find('p').text
                    f.write(nut)
                    f.write('|')
            # Start new line for new entry
            f.write('\n')

f.close()
