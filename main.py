from src import *

from translate import Translator
import json


translator = Translator(from_lang="english", to_lang="russian")
url = "https://weather.rambler.ru/world/rossiya/"
soup = Parser.parse(url)

regions: list[str] = [i.get("href") for i in soup.find_all("a", {"class": "kgSF"})]
towns: dict[str, list[str]] = {}
all_towns: dict[str, str] = {}

UserData.update_user_data()

translated_city = translator.translate(UserData.get_user_data()["properties"]["city"]).capitalize()
print(translated_city)


# ----------------------------- # temporary_data
# s = 0
#
# for region_url in regions:
#     std_url = Urls.join(url, region_url)
#     soup = Parser.parse(std_url)
#
#     # towns[region_url] = [i.get("href") for i in soup.find_all("a", {"class": "MJZ5"})]
#     for town in soup.find_all("a", {"class": "MJZ5"}):
#         all_towns[town.find("span", class_="lC50").text] = town.get("href")
#
#     s += 1
#     print(f"Completed: {s}/89.")
#
# with open('data/towns.json', 'w', encoding="utf-8") as outfile:
#     json.dump(all_towns, outfile, indent=4, ensure_ascii=False)
