import json

from src import *

from translate import Translator
import os


translator = Translator(from_lang="english", to_lang="russian")
url = "https://weather.rambler.ru/world/rossiya/"

if not os.path.exists("temporary_data/user_data.json"):
    UserData.update_user_data(UserData.get_ip_address())

country = translator.translate(UserData.get_user_data()["country"])
print(country)

if not WeatherParser.check_country_exists(country):
    WeatherParser.load_localities_of_country(
        WeatherParser.get_country_url_by_name(country), country
    )

# translated_city = translator.translate(UserData.get_user_data()["properties"]["city"]).capitalize()
# print(WeatherParser.get_url_by_name(translated_city))
