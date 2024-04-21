import requests
from bs4 import BeautifulSoup

from src import *


url = "https://weather.rambler.ru/world/rossiya/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

regions: list[str] = [i.get("href") for i in soup.find_all("a", {"class": "kgSF"})]
print(Urls.join(url, regions[0]))