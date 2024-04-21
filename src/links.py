from urllib.parse import urljoin, quote


class Urls:

    @staticmethod
    def join(*links: str) -> str:
        result_url: str = ""

        for link in links:
            result_url = urljoin(result_url, link)

        return result_url