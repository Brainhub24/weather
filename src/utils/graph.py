from colorama import Fore, Style

from ..weather import Weather


class WeatherGraph:

    @staticmethod
    def print_weather(__weather: Weather) -> None:
        print(Style.BRIGHT + Fore.BLUE + __weather.where + Style.RESET_ALL, Fore.BLUE + __weather.when + Style.RESET_ALL, sep=", ")
        print(Fore.LIGHTGREEN_EX, __weather.some_data.strip(" "), Style.RESET_ALL)

        print(Fore.YELLOW + "\n", f"Сейчас: {__weather.now}" + Style.RESET_ALL, end="")
        print(Fore.LIGHTBLACK_EX + f" : {__weather.feels}" + Style.RESET_ALL)
        print(Fore.YELLOW, f"Ночью: {__weather.night}, Днём: {__weather.day}")
