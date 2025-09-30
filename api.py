import requests

base_url = "https://api.jikan.moe/v4"
url_top = "/top/anime"


def get_airing(nsfw=False):
    response = requests.get(
        base_url + url_top, params={"filter": "airing", "sfw": str(not nsfw).lower()}
    )
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 400:
        return "error: 400"


def get_top(nsfw=False):
    response = requests.get(
        base_url + "/top/anime", params={"sfw": str(not nsfw).lower()}
    )
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 400:
        return "error: 400"


def search_anime(query):
    response = requests.get(base_url + "/anime", params={"q": query})
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 400:
        return "error: 400"


def search_anime_full(id):
    response = requests.get(base_url + "/anime/" + str(id) + "/full")

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 400:
        return "error: 400"


def get_genres():
    # response = requests.get(base_url + )
    pass
