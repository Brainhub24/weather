import requests
from bs4 import BeautifulSoup


class Parser:

    @staticmethod
    def parse(__url: str) -> BeautifulSoup:
        response = requests.get(__url)
        soup = BeautifulSoup(response.text, "lxml")

        return soup