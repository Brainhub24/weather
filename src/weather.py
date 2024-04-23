import json

from .parse import Parser
from .links import Urls

from typing import Optional
from dataclasses import dataclass

from .utils.loading import LoadingAnimations


@dataclass
class Weather:
    now: str
    night: str
    morning: str
    day: str

    # data
    where: str
    when: str
    some_data: str
    feels: str

    def __repr__(self) -> str:
        return f"Weather({self.now}, {self.night}, {self.day}, {self.morning})"


class WeatherParser:

    @staticmethod
    def __load_regions_data() -> dict:
        with open('data/towns.json', 'r', encoding="utf-8") as file:
            data = json.load(file)

        return data

    @staticmethod
    def check_country_exists(country: str) -> bool:
        return country in WeatherParser.__load_regions_data().keys()

    @classmethod
    def get_country_url_by_name(cls, __country_name: str) -> Optional[str]:
        soup = Parser.parse("https://weather.rambler.ru/world/")

        for entry in soup.find_all("a", {"class": "uErA"}):
            if entry.text == __country_name:
                return entry.get("href")

    @classmethod
    def load_towns(
            cls, __url: str, locality: str, data: dict
    ) -> dict:
        soup = Parser.parse(Urls.join(__url, locality))
        std_towns = soup.find_all("a", {"class": "MJZ5"})

        if len(std_towns) != 0:  # region || country
            for town in std_towns:
                data[town.find("span", class_="lC50").text] = town.get("href")
        
        else:  # town
            soup = Parser.parse(__url)
            data[soup.find("a", {"href": locality}).text] = locality

        return data

    @classmethod
    def load_localities_of_country(cls, __country_url: str = "rossiya/", __country_name: str = "Россия") -> None:
        url = Urls.join("https://weather.rambler.ru/world/", __country_url)
        soup = Parser.parse(url)

        regions_data = soup.find_all("a", {"class": "kgSF"})
        count_regions: int = len(regions_data)
        res: dict = {}

        if count_regions != 0:
            for entry in regions_data:
                res = cls.load_towns(url, entry.get("href"), res)

        else:
            res = cls.load_towns(
                "https://weather.rambler.ru/world/", __country_url, res
            )

        data = cls.__load_regions_data()
        data[__country_name] = res

        with open('data/towns.json', 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)

    @classmethod
    def get_url_by_name(cls, __country_name: str, __name: str) -> Optional[str]:
        return cls.__load_regions_data().get(__country_name).get(__name)
    
    @classmethod
    def load_weather(cls, __url: str) -> Weather:
        soup = Parser.parse(__url)

        # weather data
        now: str = soup.find("div", {"class": "HhSR MBvM"}).text
        night, morning, day, *rest = [i.text for i in soup.find_all("span", {"class": "kJ4q"})]

        # titles
        where: str = soup.find("div", {"class": "rICO"}).text
        when: str = soup.find("div", {"class": "w4bT"}).text
        some_data: str = soup.find("div", {"class": "TWnE"}).text
        feels: str = soup.find("span", {"class": "iO0y"}).text

        return Weather(now, night, morning, day, where, when, some_data, feels)
