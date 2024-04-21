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
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '—' * (length - filled_length)

        if main_data is None: main_data = ""
        if info is None: info = ""

        clear_output()
        print(f'\r{main_data} : |{bar}| {percent}% -> {info}', end='\r')

        # completed
        if iteration == total: print()

    @staticmethod
    def __load_towns_data() -> dict:
        with open('data/towns.json', 'r', encoding="utf-8") as file:
            data = json.load(file)

        return data

    @classmethod
    def load_countries(cls) -> None:
        ...

    @classmethod
    def load_regions(cls, __country_url: str = "rossiya/") -> None:
        url = Urls.join("https://weather.rambler.ru/world/", __country_url)
        soup = Parser.parse(url)

        regions_data = soup.find_all("a", {"class": "kgSF"})
        count_regions: int = len(regions_data)
        all_towns: dict = {}

        _progress: int = 0
        for entry in regions_data:
            region_url = entry.get("href")

            std_url = Urls.join(url, region_url)
            soup = Parser.parse(std_url)

            for town in soup.find_all("a", {"class": "MJZ5"}):
                all_towns[town.find("span", class_="lC50").text] = town.get("href")

            _progress += 1
            cls.__print_progress_bar(_progress, count_regions, main_data="Loading towns", info=entry.text)

        with open('data/towns.json', 'w', encoding="utf-8") as outfile:
            json.dump(all_towns, outfile, indent=4, ensure_ascii=False)

    @classmethod
    def get_url_by_name(cls, __name: str) -> Optional[str]:
        return cls.__load_towns_data().get(__name)
