import requests

base_url = "https://api.jikan.moe/v4"
url_top = "/top/anime"


def get_airing(nsfw=False):
    response = requests.get(
        base_url + url_top, params={"filter": "airing", "sfw": str(not nsfw).lower()}
    )
    data = response.json()
    return data


def get_top(nsfw=False):
    response = requests.get(
        base_url + "/top/anime", params={"sfw": str(not nsfw).lower()}
    )
    data = response.json()
    return data


def search_anime(query):
    response = requests.get(base_url + "/anime", params={"q": query})
    data = response.json()
    return data


def search_anime_full(id):
    response = requests.get(base_url + "/anime/" + str(id) + "/full")
    data = response.json()
    return data
