import json

from src import *

from translate import Translator
import os


translator = Translator(from_lang="english", to_lang="russian")

if not os.path.exists("temporary_data/user_data.json"):
    UserData.update_user_data(UserData.get_ip_address())

country = translator.translate(UserData.get_user_data()["country"])
city = translator.translate(UserData.get_user_data()["city"])

if not WeatherParser.check_country_exists(country):
    WeatherParser.load_localities_of_country(
        WeatherParser.get_country_url_by_name(country), country
    )

url = Urls.join("https://weather.rambler.ru/", WeatherParser.get_url_by_name(country, city))
print(WeatherParser.load_weather(url))
