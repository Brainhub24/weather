from src import *

import json


url = "https://weather.rambler.ru/world/rossiya/"
soup = Parser.parse(url)

regions: list[str] = [i.get("href") for i in soup.find_all("a", {"class": "kgSF"})]
towns: dict[str, list[str]] = {}

s = 0

for region_url in regions:
    std_url = Urls.join(url, region_url)
    soup = Parser.parse(std_url)

    towns[region_url] = [i.get("href") for i in soup.find_all("a", {"class": "MJZ5"})]

    s += 1
    print(f"Completed: {s}/89.")

with open('towns.json', 'w') as outfile:
    json.dump(towns, outfile, indent=4, ensure_ascii=False)
