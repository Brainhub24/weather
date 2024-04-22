import requests
import json


class UserData:

    @staticmethod
    def get_ip_address() -> str:
        response = requests.get('https://api.ipify.org')
        return response.text

    @staticmethod
    def update_user_data(__ip: str) -> None:
        response = requests.get(f"http://ip-api.com/json/{__ip}")

        with open('temporary_data/user_data.json', 'w', encoding="utf-8") as outfile:
            json.dump(response.json(), outfile, ensure_ascii=False, indent=4)

    @staticmethod
    def get_user_data() -> dict:
        with open('temporary_data/user_data.json', 'r', encoding="utf-8") as infile:
            data = json.load(infile)

        return data