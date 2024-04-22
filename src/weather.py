import json

from .parse import Parser
from .links import Urls

from typing import Optional
from IPython.display import clear_output


class WeatherParser:

    @staticmethod
    def __print_progress_bar(
            iteration: int, total: int, length: int = 30,
            fill='█', main_data: Optional[str] = None, info: Optional[str] = None
    ) -> None:
        percent = "{0:.1f}".format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '—' * (length - filled_length)

        if main_data is None: main_data = ""
        if info is None: info = ""

        clear_output()
        print(f'\r{main_data} : |{bar}| {percent}% -> {info}', end='\r')

        # completed
        if iteration == total: print()

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
    def get_url_by_name(cls, __name: str) -> Optional[str]:
        return cls.__load_regions_data().get(__name)
