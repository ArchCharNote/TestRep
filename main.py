# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'https://donateall.online/#/rating/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

print(soup)