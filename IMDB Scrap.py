# install beautifulsoup4, requests
from bs4 import BeautifulSoup
import requests

# URL of the IMDB page to scrape
try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status() # Check if the request was successful or not

    soup= BeautifulSoup(source.text, 'html.parser') # Create a BeautifulSoup object to parse the HTML content
    #print(soup)
    movies=soup.find('tbody', class_='lister-list') # Find the table body with class 'lister-list' and then find all 'tr' elements (each movie is in a 'tr' element)
    print(movies)

except Exception as e:
    print(e)