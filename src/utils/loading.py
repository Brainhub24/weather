from IPython.display import clear_output

from typing import Optional


class LoadingAnimations:

    @staticmethod
    def progress_bar(
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
    def loading_animation(idx: int, data: str = "") -> None:
        animation = ["|", "/", "-", "\\"]

        print(data + animation[idx % len(animation)], end="\r")