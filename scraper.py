import requests
from bs4 import BeautifulSoup

url_to_scrap = 'https://foodviva.com/curry-recipes/aloo-matar-curry/'

response = requests.get(url_to_scrap)

soup = BeautifulSoup(response.content, 'html.parser')

ingredients_section = soup.find('table', class_ ='css_fv_recipe_table')

ingredients_text = ingredients_section.get_text()

directions_section = soup.find('div', id ='css_fv_recipe_method')

directions_text = directions_section.get_text()

print(ingredients_text)
print(directions_text)
