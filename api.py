import requests

base_url = "https://api.jikan.moe/v4"
url_top = "/top/anime"


class ApiError(Exception):
    def __init__(self, status, message):
        self.status = status
        self.message = message
        super().__init__(f"API Error {status}: {message}")


def get_airing(nsfw=False):
    response = requests.get(
        base_url + url_top, params={"filter": "airing", "sfw": str(not nsfw).lower()}
    )
    if response.status_code != 200:
        raise ApiError(response.status_code, response.reason)

    data = response.json()
    return data


def get_top(nsfw=False):
    response = requests.get(
        base_url + "/top/anime", params={"sfw": str(not nsfw).lower()}
    )
    if response.status_code != 200:
        raise ApiError(response.status_code, response.reason)

    data = response.json()
    return data


def search_anime(query):
    response = requests.get(base_url + "/anime", params={"q": query})
    if response.status_code != 200:
        raise ApiError(response.status_code, response.reason)

    data = response.json()
    return data


def search_anime_full(id):
    response = requests.get(base_url + "/anime/" + str(id) + "/full")

    if response.status_code != 200:
        raise ApiError(response.status_code, response.reason)

    data = response.json()
    return data


def get_genres():
    response = requests.get(base_url + "/genres/anime")

    if response.status_code != 200:
        raise ApiError(response.status_code, response.reason)

    data = response.json
    return data
