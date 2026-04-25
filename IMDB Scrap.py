# install beautifulsoup4, requests
from bs4 import BeautifulSoup
import requests

# URL of the IMDB page to scrape
try:
    source = requests.get("https://www.imdb.com/chart/23top123456/")
    source.raise_for_status() # Check if the request was successful or not

    soup= BeautifulSoup(source.text, 'html.parser') # Create a BeautifulSoup object to parse the HTML content
    print(soup)
except Exception as e:
    print(f"Error fetching the webpage: {e}")