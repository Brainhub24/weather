from src import *

url = Urls.join("https://weather.rambler.ru/world/", "rossiya/")
soup = Parser.parse(url)

print(soup.find("a", {"href": "/v-moskve/"}))