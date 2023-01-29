import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.imdb.com/list/ls055592025/')
soup = BeautifulSoup(page.text, 'html.parser')
films = soup.find_all('h3', {'class': 'lister-item-header'})
print ([film.text for film in films])
