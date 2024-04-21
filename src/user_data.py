import geocoder
import json


class UserData:

    @staticmethod
    def update_user_data() -> None:
        data = geocoder.ip("me").geojson["features"][0]

        with open('temporary_data/user_data.json', 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)

    @staticmethod
    def get_user_data() -> dict:
        with open('temporary_data/user_data.json', 'r', encoding="utf-8") as infile:
            data = json.load(infile)

        return data